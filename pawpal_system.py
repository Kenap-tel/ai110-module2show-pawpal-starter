from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List

@dataclass
class Task:
    task_id: int
    title: str
    task_type: str
    due_time: datetime
    priority: int
    completed: bool = False
    recurring: str = None  # "daily", "weekly", or None

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True

        # Recurring logic
        if self.recurring == "daily":
            self.completed = False
            self.due_time += timedelta(days=1)

        elif self.recurring == "weekly":
            self.completed = False
            self.due_time += timedelta(weeks=1)

    def update_priority(self, priority):
        """Update the task priority."""
        self.priority = priority


@dataclass
class Pet:
    pet_id: int
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task):
        """Add a task to the pet."""
        self.tasks.append(task)

    def remove_task(self, task_id):
        """Remove a task by its ID."""
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def get_tasks(self):
        """Return all tasks for the pet."""
        return self.tasks


@dataclass
class Owner:
    owner_id: int
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet):
        """Add a pet to the owner."""
        self.pets.append(pet)

    def remove_pet(self, pet_id):
        """Remove a pet by its ID."""
        self.pets = [pet for pet in self.pets if pet.pet_id != pet_id]

    def get_pets(self):
        """Return all pets owned."""
        return self.pets


class Scheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a task to the schedule."""
        self.tasks.append(task)

    def remove_task(self, task_id):
        """Remove a task by its ID."""
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def sort_tasks(self):
     """Sort by time first, then priority (high priority first)."""
     self.tasks.sort(key=lambda task: (task.due_time, -task.priority))

    def detect_conflicts(self):
        """Return tasks that have the same due time."""
        conflicts = []

        for i in range(len(self.tasks)):
            for j in range(i + 1, len(self.tasks)):
                if self.tasks[i].due_time == self.tasks[j].due_time:
                    conflicts.append((self.tasks[i], self.tasks[j]))

        return conflicts

    def get_today_tasks(self):
        """Return today's tasks."""
        today = datetime.now().date()
        return [task for task in self.tasks if task.due_time.date() == today]
    
    def filter_tasks(self, completed=None):
     """Filter tasks by completion status."""
     if completed is None:
        return self.tasks

     return [task for task in self.tasks if task.completed == completed]