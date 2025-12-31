"""
Simple test script to verify the todo application functionality.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.models.task import Task, TaskStatus
from src.services.task_manager import TaskManager
from src.lib.utils import validate_task_description, format_task_list
from src.cli.main import TodoCLI


def test_basic_functionality():
    """Test basic functionality of the todo application."""
    print("Testing basic functionality of the Todo CLI Application...")
    
    # Test Task creation
    print("\n1. Testing Task creation:")
    task = Task(task_id=1, description="Test task")
    print(f"   Created task: {task}")
    assert task.id == 1
    assert task.description == "Test task"
    assert task.status == TaskStatus.PENDING
    
    # Test TaskManager
    print("\n2. Testing TaskManager:")
    tm = TaskManager()
    
    # Add a task
    added_task = tm.add_task("First task to complete")
    print(f"   Added task: {added_task}")
    assert added_task.id == 1
    assert added_task.description == "First task to complete"
    
    # Add another task
    added_task2 = tm.add_task("Second task")
    print(f"   Added task: {added_task2}")
    assert added_task2.id == 2
    
    # Get all tasks
    all_tasks = tm.get_all_tasks()
    print(f"   Total tasks: {len(all_tasks)}")
    assert len(all_tasks) == 2
    
    # Update a task
    updated_task = tm.update_task(1, "Updated first task")
    print(f"   Updated task: {updated_task}")
    assert updated_task.description == "Updated first task"
    
    # Mark a task as complete
    completed_task = tm.mark_complete(1)
    print(f"   Marked task as complete: {completed_task}")
    assert completed_task is not None
    assert completed_task.status == TaskStatus.COMPLETED
    
    # Delete a task
    delete_result = tm.delete_task(2)
    print(f"   Deleted task result: {delete_result}")
    assert delete_result is True
    assert tm.get_task(2) is None
    
    # Test CLI
    print("\n3. Testing CLI:")
    cli = TodoCLI()
    
    # Add a task via CLI
    cli_result = cli.add_task("CLI test task")
    print(f"   CLI add result: {cli_result}")
    assert "Task added successfully" in cli_result
    
    # View tasks via CLI
    view_result = cli.view_tasks()
    print(f"   CLI view result:\n{view_result}")
    assert "CLI test task" in view_result
    
    # Update task via CLI
    update_result = cli.update_task("1", "Updated CLI test task")
    print(f"   CLI update result: {update_result}")
    assert "updated" in update_result
    
    # Mark complete via CLI
    complete_result = cli.mark_complete("1")
    print(f"   CLI mark complete result: {complete_result}")
    assert "marked complete" in complete_result
    
    print("\nAll tests passed! The Todo CLI Application is working correctly.")
    

if __name__ == "__main__":
    test_basic_functionality()