from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Task:
    task_id: int
    title: str
    task_type: str
    due_time: datetime
    priority: int
    completed: bool = False
    recurring: bool = False

    def mark_complete(self):
        pass

    def update_priority(self, priority):
        pass


@dataclass
class Pet:
    pet_id: int
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task):
        pass

    def remove_task(self, task_id):
        pass

    def get_tasks(self):
        pass


@dataclass
class Owner:
    owner_id: int
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet):
        pass

    def remove_pet(self, pet_id):
        pass

    def get_pets(self):
        pass


class Scheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        pass

    def remove_task(self, task_id):
        pass

    def sort_tasks(self):
        pass

    def detect_conflicts(self):
        pass

    def get_today_tasks(self):
        pass