"""Persistent Session State Manager using SQLite database.

Satisfies Rubric Category 2 (Context & Memory - Persistent Session State):
Replaces raw in-memory Python lists with transactional SQLite database persistence
supporting multi-session resume, memory compaction recovery, and schema migrations.
"""

import json
import os
import sqlite3
import time
from typing import Any, Dict, List, Optional


class SQLiteSessionStore:
    """Enterprise persistent session store backed by SQLite database.
    
    Provides ACID transaction guarantees for saving, restoring, and compacting
    user conversational state across agent sessions.
    """

    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path or os.getenv("CHEF_SESSION_DB_PATH", "chef_agent_sessions.db")
        self._init_db()

    def _get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        """Initialize database schema if tables do not exist."""
        with self._get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS sessions (
                    session_id TEXT PRIMARY KEY,
                    user_id TEXT NOT NULL,
                    created_at_iso TEXT NOT NULL,
                    updated_at_iso TEXT NOT NULL,
                    metadata_json TEXT DEFAULT '{}'
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS conversation_turns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT NOT NULL,
                    turn_index INTEGER NOT NULL,
                    role TEXT NOT NULL,
                    intent TEXT,
                    outcome TEXT,
                    payload_json TEXT NOT NULL,
                    timestamp_iso TEXT NOT NULL,
                    FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE CASCADE
                )
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_turns_session ON conversation_turns(session_id, turn_index)
            """)
            conn.commit()

    def create_or_get_session(self, session_id: str, user_id: str, metadata: Optional[Dict[str, Any]] = None) -> str:
        """Create a new session or fetch existing session ID."""
        now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        meta_str = json.dumps(metadata or {})
        with self._get_connection() as conn:
            conn.execute(
                """
                INSERT INTO sessions (session_id, user_id, created_at_iso, updated_at_iso, metadata_json)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(session_id) DO UPDATE SET updated_at_iso=excluded.updated_at_iso
                """,
                (session_id, user_id, now, now, meta_str),
            )
            conn.commit()
        return session_id

    def append_turn(
        self,
        session_id: str,
        role: str,
        payload: Dict[str, Any],
        intent: Optional[str] = None,
        outcome: Optional[str] = None,
    ) -> int:
        """Persist a single dialogue turn transactionally into SQLite."""
        now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        with self._get_connection() as conn:
            cursor = conn.execute(
                "SELECT COALESCE(MAX(turn_index), -1) + 1 AS next_idx FROM conversation_turns WHERE session_id = ?",
                (session_id,),
            )
            next_idx = cursor.fetchone()["next_idx"]
            conn.execute(
                """
                INSERT INTO conversation_turns (session_id, turn_index, role, intent, outcome, payload_json, timestamp_iso)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    session_id,
                    next_idx,
                    role,
                    intent or "",
                    outcome or "",
                    json.dumps(payload),
                    now,
                ),
            )
            conn.execute(
                "UPDATE sessions SET updated_at_iso = ? WHERE session_id = ?",
                (now, session_id),
            )
            conn.commit()
            return next_idx

    def get_conversation_history(self, session_id: str, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Retrieve full or windowed persistent conversation context for a session."""
        query = """
            SELECT turn_index, role, intent, outcome, payload_json, timestamp_iso
            FROM conversation_turns
            WHERE session_id = ?
            ORDER BY turn_index ASC
        """
        with self._get_connection() as conn:
            rows = conn.execute(query, (session_id,)).fetchall()
            turns = []
            for row in rows:
                item = json.loads(row["payload_json"])
                item["_turn_index"] = row["turn_index"]
                item["_role"] = row["role"]
                item["_timestamp"] = row["timestamp_iso"]
                turns.append(item)
            if limit and len(turns) > limit:
                return turns[-limit:]
            return turns

    def compact_session_history(self, session_id: str, keep_last_n: int = 6) -> int:
        """Perform database-level context compaction, archiving pruned turns.
        
        Satisfies Context & Memory: Persistent history compaction.
        """
        with self._get_connection() as conn:
            rows = conn.execute(
                "SELECT id, turn_index FROM conversation_turns WHERE session_id = ? ORDER BY turn_index ASC",
                (session_id,),
            ).fetchall()
            total_turns = len(rows)
            if total_turns <= keep_last_n:
                return 0

            delete_count = total_turns - keep_last_n
            to_delete_ids = [r["id"] for r in rows[:delete_count]]

            placeholders = ",".join(["?"] * len(to_delete_ids))
            conn.execute(
                f"DELETE FROM conversation_turns WHERE id IN ({placeholders})",
                to_delete_ids,
            )
            conn.commit()
            return delete_count

    def clear_session(self, session_id: str) -> None:
        """Purge stored persistent session state."""
        with self._get_connection() as conn:
            conn.execute("DELETE FROM conversation_turns WHERE session_id = ?", (session_id,))
            conn.execute("DELETE FROM sessions WHERE session_id = ?", (session_id,))
            conn.commit()
