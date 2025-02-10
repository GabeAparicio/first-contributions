# Author: Gabriel Aparicio
# Student id: 101419420
# Assignment: #1

# Creating variables along with their data types
gym_member = "Alex Alliton"  # str
preferred_weight_kg = 20.5   # float
highest_reps = 25           # int
membership_active = True    # bool

# Dictionary containing workout statistics for friends with minutes spent on activities
workout_stats = {
    "Alex": (60, 45, 20),    # (yoga, running, weightlifting)
    "Jamie": (25, 30, 35),   # (yoga, running, weightlifting)
    "Taylor": (40, 25, 15)   # (yoga, running, weightlifting)
}

# Calculate total workout minutes for each friend
for friend in list(workout_stats.keys()):
    total_minutes = sum(workout_stats[friend])
    workout_stats[f"{friend}_Total"] = total_minutes

# 2D list of workout minutes
workout_list = [list(workout_stats[friend]) for friend in ["Alex", "Jamie", "Taylor"]]
# Data type: List of lists containing integers representing number of minutes for each activity

# Slice and print yoga and running minutes for all friends
print("Yoga and running minutes for all friends:")
for friend, minutes in zip(["Alex", "Jamie", "Taylor"], workout_list):
    print(f"{friend}: {minutes[:2]}")

# Print weightlifting minutes for last two friends
print("\nWeightlifting minutes for last two friends:")
for friend, minutes in zip(["Jamie", "Taylor"], workout_list[1:]):
    print(f"{friend}: {minutes[2]}")

# Check for friends with total workout minutes >= 120
for friend in ["Alex", "Jamie", "Taylor"]:
    if workout_stats[f"{friend}_Total"] >= 120:
        print(f"\nGreat job staying active, {friend}!")

# Function to search for a friend's workout data
def search_friend(name):
    if name in workout_stats and isinstance(workout_stats[name], tuple):
        print(f"\nWorkout minutes for {name}:")
        yoga, running, weightlifting = workout_stats[name]
        total = workout_stats[f"{name}_Total"]
        print(f"Yoga: {yoga}")
        print(f"Running: {running}")
        print(f"Weightlifting: {weightlifting}")
        print(f"Total: {total}")
    else:
        print(f"\nFriend {name} not found in the records.")

# Find and print friends with highest and lowest total workout minutes
friends = ["Alex", "Jamie", "Taylor"]
totals = [workout_stats[f"{friend}_Total"] for friend in friends]

max_friend = friends[totals.index(max(totals))]
min_friend = friends[totals.index(min(totals))]

# Allow user to input a friend's name and check if it exists
friend_name = input("\nEnter a friend's name to check their workout stats: ").strip()
search_friend(friend_name)


print(f"\nFriend with highest total workout minutes: {max_friend} ({max(totals)} minutes)")
print(f"Friend with lowest total workout minutes: {min_friend} ({min(totals)} minutes)")
