# A script to calculate the calories burned based on activity

activity_type = str(input("Enter the activity (\"running\", \"cycling\", \"walking\"): ")).lower()
activity_duration = int(input("Enter the duration for the activity in minutes: "))

match activity_type:
    case "running":
        calory_burn = (10 * activity_duration)
    case "cycling":
        calory_burn = (15 * activity_duration)
    case "walking":
        calory_burn = (8 * activity_duration)
    case _:
        print(f"{activity_type} is not among the listed activities \nSelect an activity listed")

print(f"{(activity_type).title()} for {activity_duration} minutes will burn {calory_burn} calories")