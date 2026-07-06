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
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
PawPal+ is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.
"""
    )

st.divider()

# ---------------- INPUTS ----------------
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.subheader("Tasks")

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
        {
            "title": task_title,
            "duration": int(duration),
            "priority": priority
        }
    )

# ---------------- DISPLAY TASKS ----------------
if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

# ---------------- SCHEDULER ----------------
st.subheader("Build Schedule")

if st.button("Generate schedule"):

    scheduler = Scheduler()

    # Convert UI tasks → Task objects
    for i, t in enumerate(st.session_state.tasks):
        task = Task(
            task_id=i,
            title=t["title"],
            task_type="General",
            due_time=datetime.now(),
            priority=1 if t["priority"] == "high" else 2
        )
        scheduler.add_task(task)

    # Sort tasks
    scheduler.sort_tasks()

    st.success("Schedule Generated!")

    st.subheader("📅 Today's Schedule")

    st.table([
        {
            "Task": task.title,
            "Time": task.due_time.strftime("%H:%M"),
            "Priority": task.priority
        }
        for task in scheduler.tasks
    ])

    # Conflict detection
    conflicts = scheduler.detect_conflicts()

    if conflicts:
        st.warning("⚠️ Conflicts detected!")

        for t1, t2 in conflicts:
            st.write(f"{t1.title} conflicts with {t2.title}")