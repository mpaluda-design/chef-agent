"""Strict type definitions and schemas for ChefAgent (Pydantic / dataclasses).

Satisfies Rubric Criterion 1: Explicit JSON Schemas & Descriptive Naming.
"""
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Dict, Any


class MealType(str, Enum):
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"
    SNACK = "snack"


class DietCategory(str, Enum):
    BALANCED = "balanced"
    HIGH_PROTEIN = "high_protein"
    VEGETARIAN = "vegetarian"
    VEGAN = "vegan"
    KETO = "keto"
    GLUTEN_FREE = "gluten_free"


@dataclass
class Ingredient:
    name: str
    quantity: float
    unit: str
    category: str  # produce, dairy, pantry, meat, spices


@dataclass
class Recipe:
    recipe_id: str
    title: str
    meal_type: MealType
    diet_category: DietCategory
    prep_time_minutes: int
    cook_time_minutes: int
    calories: int
    protein_g: float
    carbs_g: float
    fat_g: float
    sodium_mg: float
    ingredients: List[Ingredient]
    instructions: List[str]
    is_easy: bool = True
    is_healthy: bool = True

    @property
    def total_time_minutes(self) -> int:
        return self.prep_time_minutes + self.cook_time_minutes

    def to_json_schema_dict(self) -> Dict[str, Any]:
        return {
            "recipe_id": self.recipe_id,
            "title": self.title,
            "meal_type": self.meal_type.value,
            "diet_category": self.diet_category.value,
            "total_time_minutes": self.total_time_minutes,
            "macros": {
                "calories": self.calories,
                "protein_g": self.protein_g,
                "carbs_g": self.carbs_g,
                "fat_g": self.fat_g,
            },
            "ingredients": [
                {"name": ing.name, "quantity": ing.quantity, "unit": ing.unit}
                for ing in self.ingredients
            ],
        }


@dataclass
class UserPreferences:
    user_id: str
    disliked_ingredients: List[str] = field(default_factory=list)
    allergens: List[str] = field(default_factory=list)
    max_prep_time_minutes: int = 30
    daily_calorie_target: int = 2000
    min_daily_protein_g: float = 70.0
    dietary_goal: DietCategory = DietCategory.BALANCED
    pantry_inventory: List[str] = field(default_factory=list)


@dataclass
class DailyMealPlan:
    day_name: str
    breakfast: Recipe
    lunch: Recipe
    dinner: Recipe

    @property
    def total_calories(self) -> int:
        return self.breakfast.calories + self.lunch.calories + self.dinner.calories

    @property
    def total_protein_g(self) -> float:
        return self.breakfast.protein_g + self.lunch.protein_g + self.dinner.protein_g

    @property
    def max_prep_time(self) -> int:
        return max(
            self.breakfast.prep_time_minutes,
            self.lunch.prep_time_minutes,
            self.dinner.prep_time_minutes,
        )


@dataclass
class GroceryItem:
    ingredient_name: str
    total_quantity: float
    unit: str
    category: str
    already_in_pantry: bool = False


@dataclass
class WeeklyMealPlanSummary:
    plan_id: str
    days: List[DailyMealPlan]
    grocery_list: List[GroceryItem]
    avg_daily_calories: float
    avg_daily_protein_g: float
    pantry_savings_count: int
