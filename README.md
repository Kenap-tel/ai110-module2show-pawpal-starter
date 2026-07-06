# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
=== Today's Schedule ===
08:00 AM | Morning Walk | Walk | Priority: 1
09:00 AM | Feed Breakfast | Feeding | Priority: 2
10:00 AM | Give Medicine | Medication | Priority: 1
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your test output here
==================================================
test session starts
==================================================
collected 4 items

test_pawpal.py::test_mark_complete PASSED
test_pawpal.py::test_add_task PASSED
test_pawpal.py::test_recurring_task_daily PASSED
test_pawpal.py::test_sort_tasks PASSED

==================== 4 passed =====================
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting |Scheduler.sort_tasks()|Sorts tasks by due time and priority|
| Filtering | |Scheduler.filter_tasks() |Filters completed or incomplete tasks|
| Conflict handling ||Scheduler.detect_conflicts()| Detects tasks scheduled at the same time|
| Recurring tasks |Task.mark_complete() |Daily and weekly recurring tasks automatically update their due date|

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. Enter the owner's name and pet information.
2. Add one or more pet care tasks with a title, duration, and priority.
3. Click **Add Task** to add tasks to the schedule.
4. Click **Generate Schedule** to organize tasks by time and priority.
5. View the generated schedule and any conflict warnings displayed by the app.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
