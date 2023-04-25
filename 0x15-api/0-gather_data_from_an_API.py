#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
returns info about employee TODO progress
Implemented using recursion
"""
import re
import requests
import sys


API = "https://jsonplaceholder.typicode.com"
"""REST API url"""


def get_employee_todo_progress(id: int) -> None:
    """Prints the TODO progress of an employee with the given ID."""
    user_res = requests.get(f"{API}/users/{id}").json()
    todos_res = requests.get(f"{API}/todos").json()
    user_name = user_res.get("name")
    todos = [todo for todo in todos_res if todo.get("userId") == id]
    todos_done = [todo for todo in todos if todo.get("completed")]
    print(
        f"Employee {user_name} is done with tasks \
                ({len(todos_done)}/{len(todos)}):"
    )
    for todo_done in todos_done:
        print(f"\t{todo_done.get('title')}")


if __name__ == "__main__":
    """Documentation"""
    if len(sys.argv) > 1 and re.fullmatch(r"\d+", sys.argv[1]):
        id = int(sys.argv[1])
        get_employee_todo_progress(id)
