from behave import given, when, then
from manager import ToDoListManager
from task import Task

@given('the to-do list contains tasks')
def step_given_todo_list_contains_tasks(context):
    context.manager = ToDoListManager()
    context.manager.add_task("Almuerzo")
    context.manager.add_task("Cena")

@when('the user lists all tasks')
def step_when_user_lists_all_tasks(context):
    import io
    import sys

    # Redirect stdout to capture print statements
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    context.manager.list_tasks()
    
    # Capture output and reset stdout
    context.output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout

@then('the output should contain')
def step_then_output_should_contain(context):
    expected_output = context.table
    expected_lines = [f"ID: {row['ID']} | Description: {row['Description']} | Status: {row['Status']}" for row in expected_output]
    expected_output_str = "\n".join(expected_lines)
    
    assert expected_output_str == context.output, f"Expected:\n{expected_output_str}\nBut got:\n{context.output}"
