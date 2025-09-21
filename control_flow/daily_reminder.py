# Personal Daily Reminder

# Prompt user for task information
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is a high priority task. Please address it soon.")
    
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task that should be completed today.")
        else:
            print(f"\nReminder: '{task}' is a medium priority task. Consider completing it this week.")
    
    case "low":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a low priority task with a time constraint. Try to complete it when possible.")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
    
    case _:
        print("\nInvalid priority level. Please enter high, medium, or low next time.")

# Celebration message
print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
print("\n🚀 Click here to tweet! 🚀")