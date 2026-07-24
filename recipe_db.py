"""Curated dataset of healthy, quick (<30m prep) recipes for ChefAgent."""

from typing import List
from schemas import DietCategory, Ingredient, MealType, Recipe

SAMPLE_RECIPES: List[Recipe] = [
    # --- BREAKFAST ---
    Recipe(
        recipe_id="bf_01",
        title="Greek Yogurt Berry Protein Bowl",
        meal_type=MealType.BREAKFAST,
        diet_category=DietCategory.HIGH_PROTEIN,
        prep_time_minutes=5,
        cook_time_minutes=0,
        calories=340,
        protein_g=28.0,
        carbs_g=38.0,
        fat_g=8.0,
        sodium_mg=85.0,
        ingredients=[
            Ingredient("Greek Yogurt 0%", 200, "g", "dairy"),
            Ingredient("Mixed Berries", 100, "g", "produce"),
            Ingredient("Chia Seeds", 10, "g", "pantry"),
            Ingredient("Honey", 1, "tsp", "pantry"),
            Ingredient("Walnuts", 15, "g", "pantry"),
        ],
        instructions=[
            "Scoop Greek yogurt into a serving bowl.",
            "Top with fresh mixed berries, chia seeds, and chopped walnuts.",
            "Drizzle with honey and serve immediately.",
        ],
    ),
    Recipe(
        recipe_id="bf_02",
        title="Avocado Spinach Egg Scramble",
        meal_type=MealType.BREAKFAST,
        diet_category=DietCategory.BALANCED,
        prep_time_minutes=5,
        cook_time_minutes=7,
        calories=380,
        protein_g=21.0,
        carbs_g=14.0,
        fat_g=26.0,
        sodium_mg=290.0,
        ingredients=[
            Ingredient("Eggs", 2, "large", "dairy"),
            Ingredient("Egg Whites", 2, "large", "dairy"),
            Ingredient("Baby Spinach", 50, "g", "produce"),
            Ingredient("Avocado", 0.5, "medium", "produce"),
            Ingredient("Olive Oil", 1, "tsp", "pantry"),
            Ingredient("Whole Wheat Toast", 1, "slice", "bakery"),
        ],
        instructions=[
            (
                "Whisk eggs and egg whites in a bowl with sea salt and black"
                " pepper."
            ),
            (
                "Heat olive oil in non-stick skillet, wilt baby spinach for 1"
                " minute."
            ),
            (
                "Pour in eggs and scramble gently over medium-low heat for 3-4"
                " minutes."
            ),
            "Serve over toasted whole wheat bread sliced with ripe avocado.",
        ],
    ),
    Recipe(
        recipe_id="bf_03",
        title="Overnight High-Fiber Cinnamon Oats",
        meal_type=MealType.BREAKFAST,
        diet_category=DietCategory.VEGETARIAN,
        prep_time_minutes=5,
        cook_time_minutes=0,
        calories=360,
        protein_g=16.0,
        carbs_g=52.0,
        fat_g=9.0,
        sodium_mg=110.0,
        ingredients=[
            Ingredient("Rolled Oats", 50, "g", "pantry"),
            Ingredient("Unsweetened Almond Milk", 180, "ml", "dairy"),
            Ingredient("Flaxseed Ground", 1, "tbsp", "pantry"),
            Ingredient("Cinnamon", 0.5, "tsp", "spices"),
            Ingredient("Apple sliced", 0.5, "medium", "produce"),
            Ingredient("Protein Powder Vanilla", 15, "g", "pantry"),
        ],
        instructions=[
            (
                "Combine oats, almond milk, flaxseed, cinnamon, and protein"
                " powder in a mason jar."
            ),
            "Refrigerate overnight (at least 6 hours).",
            "Top with crisp sliced apples before eating.",
        ],
    ),
    # --- LUNCH ---
    Recipe(
        recipe_id="lh_01",
        title="Mediterranean Quinoa Chicken Bowl",
        meal_type=MealType.LUNCH,
        diet_category=DietCategory.HIGH_PROTEIN,
        prep_time_minutes=10,
        cook_time_minutes=12,
        calories=510,
        protein_g=42.0,
        carbs_g=48.0,
        fat_g=16.0,
        sodium_mg=420.0,
        ingredients=[
            Ingredient("Chicken Breast", 150, "g", "meat"),
            Ingredient("Cooked Quinoa", 120, "g", "pantry"),
            Ingredient("Cucumber diced", 60, "g", "produce"),
            Ingredient("Cherry Tomatoes", 80, "g", "produce"),
            Ingredient("Kalamata Olives", 5, "pieces", "pantry"),
            Ingredient("Feta Cheese", 25, "g", "dairy"),
            Ingredient("Lemon Juice", 1, "tbsp", "produce"),
            Ingredient("Extra Virgin Olive Oil", 1, "tsp", "pantry"),
        ],
        instructions=[
            (
                "Season chicken breast with oregano, garlic powder, salt, and"
                " cook on skillet 6 mins per side."
            ),
            "Slice chicken into strips.",
            (
                "Assemble bowl with base of cooked quinoa, diced cucumber,"
                " cherry tomatoes, olives, and feta."
            ),
            (
                "Top with grilled chicken and dress with lemon juice and olive"
                " oil."
            ),
        ],
    ),
    Recipe(
        recipe_id="lh_02",
        title="Tuscan White Bean & Kale Power Salad",
        meal_type=MealType.LUNCH,
        diet_category=DietCategory.VEGAN,
        prep_time_minutes=10,
        cook_time_minutes=0,
        calories=430,
        protein_g=19.0,
        carbs_g=56.0,
        fat_g=14.0,
        sodium_mg=380.0,
        ingredients=[
            Ingredient("Cannellini Beans canned drained", 200, "g", "pantry"),
            Ingredient("Lacinato Kale chopped", 80, "g", "produce"),
            Ingredient("Sun-dried Tomatoes", 20, "g", "pantry"),
            Ingredient("Pumpkin Seeds Pepitas", 15, "g", "pantry"),
            Ingredient("Garlic minced", 1, "clove", "produce"),
            Ingredient("Balsamic Vinaigrette", 1.5, "tbsp", "pantry"),
        ],
        instructions=[
            (
                "Massage kale leaves with half of vinaigrette for 2 minutes"
                " until tender."
            ),
            "Rinse and drain canned white beans.",
            (
                "Toss kale, white beans, sun-dried tomatoes, and pumpkin seeds"
                " together."
            ),
            (
                "Drizzle remaining balsamic vinaigrette and serve cold or room"
                " temperature."
            ),
        ],
    ),
    Recipe(
        recipe_id="lh_03",
        title="Salmon Edamame Brown Rice Poke Bowl",
        meal_type=MealType.LUNCH,
        diet_category=DietCategory.BALANCED,
        prep_time_minutes=10,
        cook_time_minutes=10,
        calories=540,
        protein_g=36.0,
        carbs_g=50.0,
        fat_g=20.0,
        sodium_mg=460.0,
        ingredients=[
            Ingredient("Wild Salmon Fillet", 140, "g", "meat"),
            Ingredient("Shelled Edamame cooked", 80, "g", "produce"),
            Ingredient("Cooked Brown Rice", 110, "g", "pantry"),
            Ingredient("Nori Seaweed Strips", 2, "sheets", "pantry"),
            Ingredient("Sesame Seeds", 1, "tsp", "pantry"),
            Ingredient("Low Sodium Soy Sauce", 1, "tbsp", "pantry"),
            Ingredient("Grating Ginger", 0.5, "tsp", "produce"),
        ],
        instructions=[
            (
                "Pan-sear salmon fillet skin-side down for 4 minutes, flip and"
                " cook 3 more minutes."
            ),
            "Place warm cooked brown rice in bowl.",
            (
                "Arrange flaked salmon, warm edamame, and crispy nori strips"
                " over rice."
            ),
            "Garnish with toasted sesame seeds and fresh ginger-soy sauce.",
        ],
    ),
    # --- DINNER ---
    Recipe(
        recipe_id="dn_01",
        title="Sheet-Pan Lemon Herb Turkey & Roasted Veggies",
        meal_type=MealType.DINNER,
        diet_category=DietCategory.HIGH_PROTEIN,
        prep_time_minutes=10,
        cook_time_minutes=20,
        calories=490,
        protein_g=44.0,
        carbs_g=28.0,
        fat_g=22.0,
        sodium_mg=390.0,
        ingredients=[
            Ingredient("Turkey Breast Cutlets", 170, "g", "meat"),
            Ingredient("Zucchini sliced", 120, "g", "produce"),
            Ingredient("Red Bell Pepper chopped", 100, "g", "produce"),
            Ingredient("Broccoli Florets", 120, "g", "produce"),
            Ingredient("Olive Oil", 1, "tbsp", "pantry"),
            Ingredient("Dried Thyme and Rosemary", 1, "tsp", "spices"),
            Ingredient("Garlic Powder", 0.5, "tsp", "spices"),
        ],
        instructions=[
            "Preheat oven to 200°C (400°F).",
            (
                "Toss cut zucchini, bell pepper, and broccoli with olive oil,"
                " rosemary, and thyme on sheet pan."
            ),
            "Nestle turkey breast cutlets among vegetables.",
            (
                "Roast for 18-20 minutes until turkey reaches internal temp of"
                " 74°C (165°F)."
            ),
        ],
    ),
    Recipe(
        recipe_id="dn_02",
        title="Lentil Cauliflower Curry with Basmati Rice",
        meal_type=MealType.DINNER,
        diet_category=DietCategory.VEGAN,
        prep_time_minutes=10,
        cook_time_minutes=15,
        calories=460,
        protein_g=22.0,
        carbs_g=68.0,
        fat_g=10.0,
        sodium_mg=340.0,
        ingredients=[
            Ingredient("Brown or Red Lentils cooked", 180, "g", "pantry"),
            Ingredient("Cauliflower Florets", 150, "g", "produce"),
            Ingredient("Light Coconut Milk", 120, "ml", "pantry"),
            Ingredient("Crushed Tomatoes canned", 150, "g", "pantry"),
            Ingredient("Curry Powder Yellow", 1.5, "tbsp", "spices"),
            Ingredient("Basmati Rice cooked", 100, "g", "pantry"),
            Ingredient("Fresh Cilantro", 10, "g", "produce"),
        ],
        instructions=[
            (
                "Sauté yellow curry powder and garlic in deep saucepan for 30"
                " seconds until fragrant."
            ),
            (
                "Add cauliflower florets, crushed tomatoes, light coconut milk,"
                " and cooked lentils."
            ),
            "Simmer covered for 12-15 minutes until cauliflower is tender.",
            "Serve over fluffy steamed basmati rice with cilantro leaves.",
        ],
    ),
    Recipe(
        recipe_id="dn_03",
        title="Garlic Shrimp & Zucchini Noodle Stir-Fry",
        meal_type=MealType.DINNER,
        diet_category=DietCategory.KETO,
        prep_time_minutes=8,
        cook_time_minutes=6,
        calories=350,
        protein_g=34.0,
        carbs_g=11.0,
        fat_g=19.0,
        sodium_mg=410.0,
        ingredients=[
            Ingredient("Jumbo Shrimp peeled devined", 180, "g", "meat"),
            Ingredient(
                "Spiralized Zucchini Noodles Zoodles", 220, "g", "produce"
            ),
            Ingredient("Garlic minced", 3, "cloves", "produce"),
            Ingredient("Butter or Ghee", 1, "tbsp", "dairy"),
            Ingredient("Crushed Red Pepper Flakes", 0.25, "tsp", "spices"),
            Ingredient("Parmesan Grated", 15, "g", "dairy"),
        ],
        instructions=[
            (
                "Melt butter in large skillet over medium-high heat with minced"
                " garlic and red pepper flakes."
            ),
            (
                "Add jumbo shrimp and sauté 2 minutes per side until pink and"
                " opaque."
            ),
            (
                "Toss in spiralized zucchini noodles for just 1.5 minutes so"
                " they remain crisp-tender."
            ),
            "Finish with grated parmesan and freshly cracked black pepper.",
        ],
    ),
]
