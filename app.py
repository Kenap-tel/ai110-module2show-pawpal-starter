from pawpal_system import Owner, Pet, Task, Scheduler
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    st.session_state.tasks.append(
        {"title": task_title, "duration_minutes": int(duration), "priority": priority}
    )

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")
    if "owner_obj" not in st.session_state:
       st.session_state.owner_obj = Owner(owner_id=1, name=owner_name)

if "scheduler_obj" not in st.session_state:
    st.session_state.scheduler_obj = Scheduler()
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    scheduler = st.session_state.scheduler_obj

    # clear old tasks
    scheduler.tasks = []

    # convert UI tasks → Task objects
    for i, t in enumerate(st.session_state.tasks):
        task = Task(
            task_id=i,
            title=t["title"],
            task_type="General",
            due_time=datetime.now(),
            priority=1 if t["priority"] == "high" else 2
        )
        scheduler.add_task(task)

    scheduler.sort_tasks()

    st.success("Schedule Generated!")

    st.subheader("Today's Schedule")

    for task in scheduler.tasks:
        st.write(f"{task.title} | Priority: {task.priority}")

    st.markdown(
        """
Suggested approach:
1. Design your UML (draft).
2. Create class stubs (no logic).
3. Implement scheduling behavior.
4. Connect your scheduler here and display results.
"""
    )

    # convert UI tasks → Task objects
    scheduler.tasks = []

    for i, t in enumerate(st.session_state.tasks):
        task = Task(
            task_id=i,
            title=t["title"],
            task_type="General",
            due_time=datetime.now(),
            priority=1 if t["priority"] == "high" else 2
        )
        scheduler.add_task(task)

    scheduler.sort_tasks()

    st.success("Schedule Generated!")

    st.subheader("Today's Schedule")

    for task in scheduler.tasks:
        st.write(
            f"{task.title} | Priority: {task.priority}"
        )
    st.markdown(
        """
Suggested approach:
1. Design your UML (draft).
2. Create class stubs (no logic).
3. Implement scheduling behavior.
4. Connect your scheduler here and display results.
"""
    )
