# Simple To-Do Project
# Run: 
#   python todo.py
#   python todo.py --list
#   python todo.py --count
import sys

todos = ["learn git", "create PR", "move issues on board"]

if "--count" in sys.argv:
    print(f"You have {len(todos)} todos")
elif "--list" in sys.argv:
    for i, t in enumerate(todos, 1):
        print(f"#{i} {t}")
else:
    for i, t in enumerate(todos, 1):
        print(f"{i}. {t}")
