

meal_names = []
meal_calories = []

num_meals = int(input("How many meals did you have today? "))

for i in range(num_meals):
    meal = input(f"Enter meal name {i+1}: ")
    calories = float(input(f"Enter calories for {meal}: "))
    meal_names.append(meal)
    meal_calories.append(calories)

total_calories = sum(meal_calories)
average_calories = total_calories / len(meal_calories)
daily_limit = float(input("\nEnter your daily calorie limit: "))

if total_calories > daily_limit:
    status = f"⚠️ You ate {total_calories - daily_limit:.2f} calories more than your daily limit!"
else:
    status = f"✅ You are within your limit! You can still eat {daily_limit - total_calories:.2f} calories."

print("\n--------------------------------------")
print("           MEAL SUMMARY")
print("--------------------------------------")
print("Meal Name\tCalories")
print("--------------------------------------")

for i in range(num_meals):
    print(f"{meal_names[i]}\t\t{meal_calories[i]}")

print("--------------------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")
print("--------------------------------------")
print(status)
