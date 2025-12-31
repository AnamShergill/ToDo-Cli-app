from src.cli.main import TodoCLI

# Create a CLI instance
cli = TodoCLI()

# Add a task
result = cli.add_task("Test rich task")
print("Add result:", result)

# Add another task
result = cli.add_task("Another rich task")
print("Add result:", result)

# View tasks (this will print the table)
print("Viewing tasks:")
cli.view_tasks()

# Mark a task as complete
result = cli.mark_complete("1")
print("Mark complete result:", result)

# View tasks again
print("Viewing tasks after marking complete:")
cli.view_tasks()