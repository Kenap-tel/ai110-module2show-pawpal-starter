from datetime import datetime
from pawpal_system import Owner, Pet, Task, Scheduler

# Create an owner
owner = Owner(owner_id=1, name="Kena")

# Create pets
dog = Pet(pet_id=1, name="Buddy", species="Dog", age=3)
cat = Pet(pet_id=2, name="Luna", species="Cat", age=2)

# Add pets to owner
owner.add_pet(dog)
owner.add_pet(cat)

# Create tasks
task1 = Task(
    task_id=1,
    title="Morning Walk",
    task_type="Walk",
    due_time=datetime(2026, 7, 6, 8, 0),
    priority=1
)

task2 = Task(
    task_id=2,
    title="Feed Breakfast",
    task_type="Feeding",
    due_time=datetime(2026, 7, 6, 9, 0),
    priority=2
)

task3 = Task(
    task_id=3,
    title="Give Medicine",
    task_type="Medication",
    due_time=datetime(2026, 7, 6, 10, 0),
    priority=1
)

# Add tasks to pets
dog.add_task(task1)
dog.add_task(task2)
cat.add_task(task3)

# Create scheduler
scheduler = Scheduler()

# Add tasks to scheduler
scheduler.add_task(task1)
scheduler.add_task(task2)
scheduler.add_task(task3)

# Sort tasks
scheduler.sort_tasks()

# Print schedule
print("=== Today's Schedule ===")

for task in scheduler.tasks:
    print(
        f"{task.due_time.strftime('%I:%M %p')} | "
        f"{task.title} | "
        f"{task.task_type} | "
        f"Priority: {task.priority}"
    )