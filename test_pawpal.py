from datetime import datetime
from pawpal_system import Task, Pet, Scheduler


def test_mark_complete():
    task = Task(
        task_id=1,
        title="Feed",
        task_type="Feeding",
        due_time=datetime(2026, 7, 5, 8, 0),
        priority=1,
    )

    task.mark_complete()
    assert task.completed is True


def test_add_task():
    pet = Pet(
        pet_id=1,
        name="Buddy",
        species="Dog",
        age=3,
    )

    task = Task(
        task_id=1,
        title="Walk",
        task_type="Walk",
        due_time=datetime(2026, 7, 5, 8, 0),
        priority=1,
    )

    pet.add_task(task)
    assert len(pet.tasks) == 1


def test_recurring_task_daily():
    task = Task(
        task_id=1,
        title="Walk",
        task_type="Walk",
        due_time=datetime(2026, 7, 5, 8, 0),
        priority=1,
        recurring="daily"
    )

    task.mark_complete()

    assert task.due_time == datetime(2026, 7, 6, 8, 0)


def test_sort_tasks():
    scheduler = Scheduler()

    t1 = Task(1, "Late", "Walk", datetime(2026, 7, 6, 10, 0), 2)
    t2 = Task(2, "Early", "Feed", datetime(2026, 7, 6, 8, 0), 1)

    scheduler.add_task(t1)
    scheduler.add_task(t2)

    scheduler.sort_tasks()

    assert scheduler.tasks[0].title == "Early"