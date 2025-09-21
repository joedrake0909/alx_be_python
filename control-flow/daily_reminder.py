# Personal Daily Reminder

# Prompt user for task information
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use a loop to ensure valid priority input
while priority not in ["high", "medium", "low"]:
    print("Invalid priority! Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()

# Use a loop to ensure valid time-bound input  
while time_bound not in ["yes", "no"]:
    print("Invalid input! Please enter yes or no.")
    time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority using match case
match priority:
    case "high":
        # Use if statement to modify reminder based on time sensitivity
        if time_bound == "yes":
            reminder = f"'{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder = f"'{task}' is a high priority task. Please address it soon."
    
    case "medium":
        if time_bound == "yes":
            reminder = f"'{task}' is a medium priority task that should be completed today."
        else:
            reminder = f"'{task}' is a medium priority task. Consider completing it this week."
    
    case "low":
        if time_bound == "yes":
            reminder = f"'{task}' is a low priority task with a time constraint."
        else:
            reminder = f"'{task}' is a low priority task. Consider completing it when you have free time."

# Print the customized reminder
print(f"\nReminder: {reminder}")

# Celebration message with loop for emphasis
print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
for _ in range(3):
    print("🚀" * 5)
print("Click here to tweet! 🚀")