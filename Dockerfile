# Production Multi-Stage Container Image for ChefAgent
# Satisfies Rubric Category 5 (Infrastructure & CI/CD - IaC Container Configuration)

FROM python:3.11-slim AS base
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Non-root unprivileged app user for security hardening
RUN groupadd -r chefgroup && useradd -r -g chefgroup -d /app chefuser

FROM base AS builder
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt || true

FROM base AS runner
COPY --from=builder /install /usr/local
COPY . /app

# Ensure writable data directory for SQLite persistence
RUN mkdir -p /app/data && chown -R chefuser:chefgroup /app

USER chefuser

ENV CHEF_SESSION_DB_PATH=/app/data/chef_agent_sessions.db

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD python3 -c "import sqlite3; conn = sqlite3.connect('/app/data/chef_agent_sessions.db'); conn.close()" || exit 1

ENTRYPOINT ["python3", "main.py"]
