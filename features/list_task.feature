Feature: List all tasks in the to-do list

    @listTasks
    Scenario: List all tasks in the to-do list
        Given the to-do list contains tasks
        | ID | Description | Status  |
        | 1  | Almuerzo    | Pending |
        | 2  | Cena        | Pending |
        When the user lists all tasks
        Then the output should contain
        | ID | Description | Status  |
        | 1  | Almuerzo    | Pending |
        | 2  | Cena        | Pending |

