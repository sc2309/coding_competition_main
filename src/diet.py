from flask import Blueprint, render_template

diet = Blueprint('diet', __name__)

@diet.route('/diet')
def index():
    veg_diet_powder = ['1. Breakfast:  Veg protein pancakes\n2. Lunch: salad with mixed veggies\n3. Snack: Hummus and raw vegetable sticks\n4. Dinner: vegetable stew with a side of whole grain bread','1. Breakfast: Veg protein smoothie with spinach, banana,almond milk\n2. Lunch: Chickpea salad with lemon\n3. Snack: Mixed nuts and dried fruits\n4. Dinner: chili with beans,roasted chickpeas, and a side of avocado','1. Breakfast: Protein-infused oatmeal with sliced almonds\n2. Lunch: roasted tofu or roasted panner,cucumber with a side of whole grain bread\n3. Snack: Apple slices with almond,butter\n4. Spaghetti with tofu or panner','1. Breakfast: Veg protein muffins with a side of fresh fruit\n2. Lunch: black bean salad with vinegar\n3. Snack: Rice cakes with peanut butter\n4. Dinner: Stir-fried tofu and mixed vegetables, served over brown rice','1. Breakfast: Vegan protein pancakes made with plant-based protein powder.Top with fresh berries and a drizzle of honey.\n2. Lunch: Vegan wrap with falafel, veggies, and tahini sauce\n3. Snack: Carrot and celery sticks with hummus\n4. Dinner: Veg curry with chickpeas and brown rice','1. Breakfast: Vegan protein power bowl with granola, almond yogurt, and fresh fruit\n2. Lunch:  vegetable soup with a side of whole grain bread\n3. protien cookies with milk\n4. Dinner: Veg stir-fry with tofu, broccoli, and a ginger-soy sauce','1. Breakfast: Vegan protein waffles topped with dairy-free yogurt and mixed fruit\n2. Lunch: Vegan burrito bowl with black beans, rice, salsa\n3. Snack: Vegan protein bar or a homemade protein ball\n4. Dinner: roasted soyabean and a side salad']
    veg_diet_nopowder = ['1. Breakfast: Veg yogurt with mixed berries and granola.\n2. Lunch: salad with chickpeas, cucumber, and a tahini dressing.\n3. Snack: Sliced bell peppers with hummus.\n4.Dinner: Eggplant and chickpea stew with a side of whole wheat bread.','1. Breakfast: Avocado toast with cherry tomatoes and a sprinkle of nutritional yeast.\n2. Lunch: Vegan bean and vegetable burrito.\n3. Snack: Mango and chili-lime spiced sticks.\n4. Dinner: Veg chili with kidney beans and a side of brown rice.','1. Breakfast: Vegan rice porridge with coconut milk and a dash of maple syrup.\n2. Lunch: Veg rolls with avocado, cucumber, and sweet potato.\n3. Snack: peas with sea salt and spices.\n4. Dinner: Stir-fried tofu with broccoli and bell peppers in a ginger-soy sauce, served over brown rice.','1. Breakfast: Vegan bruschetta with diced tomatoes, garlic, and basil on whole grain bread.\n2. Lunch: Vegan pasta primavera with mixed vegetables in a tomato-basil sauce.\n3. Snack: Roasted chickpeas.\n4. Dinner: Vegan eggplant Parmesan with a side salad.','Breakfast: Vegan hummus toast with diced cucumbers and cherry tomatoes.\n2.Lunch: Falafel wrap with tahini sauce and a side of salad.\n3.Snack: Sliced oranges with a sprinkle of cinnamon.\n4. congrats on following the diet you can eat whatever you want for dinner today','1. Breakfast: Green smoothie with spinach, banana, almond milk, and a scoop of peanut butter.\n2. Lunch: Veg soup with a side of whole wheat bread.\n3. Snack: Celery and carrot sticks with almond butter.\nDinner: Veg white bean stew with a side of whole grain bread.','1. Breakfast: Vegan breakfast burrito with tofu scramble, black beans, and salsa.\n2. Lunch: Vegan black bean and corn salad with a cilantro-lime vinaigrette.\n3. Snack: Sliced bell peppers with guacamole.\n4. Dinner: Vegan enchiladas with a side of Mexican-style rice.']
    return render_template('daily_diet.html')