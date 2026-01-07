# app.py

from orchestrator import supervisor_router

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    print(supervisor_router(user_input))

