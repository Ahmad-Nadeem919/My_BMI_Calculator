import streamlit as st

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

st.title(" Simple To-Do List")

# Input and add button
task = st.text_input("Enter a task")
if st.button("Add"):
    if task:
        st.session_state.tasks.append(task)
        st.success("Task added!")
    else:
        st.warning("Please enter a task.")

st.write("---")

# Show tasks
st.subheader("Your Tasks")
if st.session_state.tasks:
    for i, t in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.8, 0.2])
        col1.write(f" {t}")
        if col2.button("Delete", key=i):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()
else:
    st.info("No tasks added yet.")





