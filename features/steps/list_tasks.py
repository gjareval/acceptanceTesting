from behave import given, when, then
from manager import ToDoListManager
from task import Task
import io
import sys

@given('the to-do list contains tasks')
def step_impl(context):
    context.manager = ToDoListManager()
    context.manager.add_task("Almuerzo")
    context.manager.add_task("Cena")

@when('the user lists all tasks')
def step_impl(context):
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    context.manager.list_tasks()
    
    context.output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout

@then('the output should contain')
def step_impl(context):
    expected_output = context.table
    expected_lines = [f"ID: {row['ID']} | Description: {row['Description']} | Status: {row['Status']}" for row in expected_output]
    expected_output_str = "\n".join(expected_lines)
    assert expected_output_str == context.output, f"Expected:\n{expected_output_str}\nBut got:\n{context.output}"
