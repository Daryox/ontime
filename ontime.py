class Task:
    def __init__(self, duration, priority, description):
        self.duration = duration
        self.priority = priority
        self.description = description


def organize_schedule(tasks, fixed_hours):
    # Sorting tasks based on priority
    sorted_tasks = sorted(tasks, key=lambda x: x.priority, reverse=True)

    # Initialize schedule with available slots for 24 hours
    schedule = ["available"] * 24

    # Mark fixed hours as unavailable
    for start, end, task_name in fixed_hours:
        if end > start:  # Corrected condition
            schedule[start:end] = [f"{task_name}"] * (end - start)
        else:
            # Handle the case where end < start (overnight fixed hours)
            schedule[start:] = [f"{task_name}"] * (24 - start)
            schedule[:end] = [f"{task_name}"] * end

    # Iterate through sorted tasks
    for task in sorted_tasks:
        # Iterate through available slots in the schedule
        for i in range(24):
            # Check if the slot is available for the task's duration
            if all(slot == "available" for slot in schedule[i:i + task.duration]):
                # Schedule the task by marking slots as the task description
                schedule[i:i + task.duration] = [f"{task.description}"] * task.duration
                break  # Break the loop once the task is scheduled

    # Display the schedule
    for i, slot in enumerate(schedule):
        print("{}:00 - {}:00: {}".format(i, i + 1, slot))


# User input for fixed hours with debugging for bad input
fixed_hours = []
while True:
    try:
        task_name = input("\nEnter the name of the fixed task (leave blank to stop): ")
        if not task_name:
            break
        start_time = int(input("Enter start time for fixed task (0-23): "))
        end_time = int(input("Enter end time for fixed task (0-23): "))

        if not (0 <= start_time <= 23) or not (0 <= end_time <= 23):
            raise ValueError("Invalid input. Please enter valid start and end times.")

        fixed_hours.append((start_time, end_time, task_name))

    except ValueError as e:
        print(f"\nError: {e}. Please try again.")

# User input for tasks with debugging for bad input
tasks = []
while True:
    try:
        description = input("\nEnter task description (leave blank to stop): ")
        if not description:
            break
        duration = int(input("Enter duration (in hours): "))
        priority = int(input("Enter priority (higher number is higher priority): "))

        if duration <= 0 or priority < 0:
            raise ValueError("Invalid input. Duration must be greater than 0, and priority must be non-negative.")

        tasks.append(Task(duration=duration, priority=priority, description=description))

    except ValueError as e:
        print(f"\nError: {e}. Please try again.")

# Call the function
organize_schedule(tasks, fixed_hours)