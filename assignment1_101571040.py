"""
Author: Jenifa Joseph
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton"     # Data type - String
preferred_weight_kg = 20.5      # Data type - Float
highest_reps = 25               # Data type - Integer
membership_active = True        # Data type - Boolean

# Step c: Create a dictionary named workout_stats
# Dictionary Data type - Keys => Strings, Values => Tuples of Integers
workout_stats = {
    "Peter": (30, 45, 20),
    "Betty": (45, 50, 30),
    "Jane": (30, 60, 30)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend, minutes in list(workout_stats.items()):
    total_minutes = sum(minutes)
    workout_stats[f"{friend}_Total"] = total_minutes

# Step e: Create a 2D nested list called workout_list
workout_list = [
    list(workout_stats["Peter"]),
    list(workout_stats["Betty"]),
    list(workout_stats["Jane"])
]

# Step f: Slice the workout_list
print("Yoga and running minutes for all friends: ")
for row in workout_list:
    print(row[0:2])

print("\nWeightlifting minutes for last two friend: ")
for row in workout_list[1:]:
    print(row[2])    

# Step g: Check if any friend's total >= 120
for friend in ["Peter", "Betty", "Jane"]:
    total = workout_stats[f"{friend}_Total"]
    if total >= 120:
        print(f"Great job staying active, {friend}!")

# Step h: User input to look up a friend
user_name = input("Enter a friend's name: ")

if user_name in workout_stats:
    if isinstance(workout_stats[user_name], tuple):
        yoga, running, weightlifting = workout_stats[user_name]
        total = workout_stats[f"{user_name}_Total"]

        print(f"\nWorkout details for {user_name}:")
        print(f"Yoga: {yoga} minutes")
        print(f"Running: {running} minutes")
        print(f"Weightlighting: {weightlifting} minutes")
        print(f"Total: {total} minutes")

else:
        print(f"Friend {user_name} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
totals = {
    "Peter": workout_stats["Peter_Total"],
    "Betty": workout_stats["Betty_Total"],
    "Jane": workout_stats["Jane_Total"]
}

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print(f"\nHighest total workout minutes: {highest_friend}")
print(f"Lowest total workout minutes: {lowest_friend}")
