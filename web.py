import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    if todo:
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state.new_todo = ""


st.title("My Todo App")
st.subheader("Twój komputer został przejęty hahaha")
st.write("This app is to increase your <b>productivity</b>.", unsafe_allow_html=True)

st.text_input(label="o", placeholder="Add new todo..",
              on_change=add_todo, key="new_todo",
              label_visibility='hidden')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()






