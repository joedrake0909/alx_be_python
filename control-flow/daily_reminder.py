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
            print(f"\nReminder: '{task}' is a high priority task. Immediate action is recommended but not time-critical.")
    
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task that requires attention today due to time constraints.")
        else:
            print(f"\nReminder: '{task}' is a medium priority task. Action is required but not immediately urgent.")
    
    case "low":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a low priority task with time constraints. Consider completing it when possible.")
        else:
            print(f"\nReminder: '{task}' is a low priority task. No immediate action required - complete at your convenience.")
    
    case _:
        print("\nInvalid priority level. Please enter high, medium, or low next time.")

# Celebration message
print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
print("\n🚀 Click here to tweet! 🚀")