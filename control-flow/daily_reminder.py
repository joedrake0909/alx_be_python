# Personal Daily Reminder

# Prompt user for task information
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Ensure valid priority input
while priority not in ["high", "medium", "low"]:
    print("Invalid priority! Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()

# Ensure valid time-bound input
while time_bound not in ["yes", "no"]:
    print("Invalid input! Please enter yes or no.")
    time_bound = input("Is it time-bound? (yes/no): ").lower()

# Build a customized message based on priority and time sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            details = f"'{task}' is a high priority task that requires immediate attention today!"
        else:
            details = f"'{task}' is a high priority task. Please address it soon."
    case "medium":
        if time_bound == "yes":
            details = f"'{task}' is a medium priority task that should be completed today."
        else:
            details = f"'{task}' is a medium priority task. Consider completing it this week."
    case "low":
        if time_bound == "yes":
            details = f"'{task}' is a low priority task with a time constraint."
        else:
            details = f"'{task}' is a low priority task. Consider completing it when you have free time."

# Compute immediate action flag
immediate = "Yes" if time_bound == "yes" else "No"

# ✅ Print a single line that starts with 'Reminder:' and includes priority + immediate flag
print(f"Reminder: Task '{task}' | Priority: {priority} | Immediate action required: {immediate}. {details}")

# Celebration message with loop for emphasis (optional)
print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
for _ in range(3):
    print("🚀" * 5)
print("Click here to tweet! 🚀")
