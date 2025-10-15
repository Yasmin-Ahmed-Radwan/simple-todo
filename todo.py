# Simple To-Do Project
# Run: python todo.py  OR  python todo.py --list
import sys

todos = ["learn git", "create PR", "move issues on board"]

if "--list" in sys.argv:
    for i, t in enumerate(todos, 1):
        print(f"#{i} {t}")
else:
    for i, t in enumerate(todos, 1):
        print(f"{i}. {t}")
