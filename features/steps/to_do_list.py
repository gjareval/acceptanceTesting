from manager import ToDoListManager
from behave import given, when, then

to_do_list = []
manager = ToDoListManager()

@given('the to-do list is empty')
def step_impl(context):
    manager.clear_tasks()

@when('the user adds a task "{task}"')
def step_impl(context, task):
    manager.add_task(task)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    found = any(t.description == task for t in manager.tasks.values())
    assert  found, f'Task "{task}" not found'