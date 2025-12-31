"""
Unit tests for the TaskManager service.
"""

import pytest
from src.models.task import Task, TaskStatus
from src.services.task_manager import TaskManager


class TestTaskManager:
    """Unit tests for the TaskManager class."""
    
    def test_initialization(self):
        """Test initializing a TaskManager."""
        tm = TaskManager()
        
        assert len(tm.tasks) == 0
        assert tm._next_id == 1
    
    def test_add_task(self):
        """Test adding a new task."""
        tm = TaskManager()
        
        task = tm.add_task("Test task")
        
        assert len(tm.tasks) == 1
        assert task.id == 1
        assert task.description == "Test task"
        assert task.status == TaskStatus.PENDING
        assert tm._next_id == 2
    
    def test_add_multiple_tasks(self):
        """Test adding multiple tasks with unique IDs."""
        tm = TaskManager()
        
        task1 = tm.add_task("First task")
        task2 = tm.add_task("Second task")
        
        assert len(tm.tasks) == 2
        assert task1.id == 1
        assert task2.id == 2
        assert tm._next_id == 3
    
    def test_get_task_found(self):
        """Test getting an existing task."""
        tm = TaskManager()
        added_task = tm.add_task("Test task")
        
        retrieved_task = tm.get_task(added_task.id)
        
        assert retrieved_task is not None
        assert retrieved_task.id == added_task.id
        assert retrieved_task.description == added_task.description
    
    def test_get_task_not_found(self):
        """Test getting a non-existing task."""
        tm = TaskManager()
        
        retrieved_task = tm.get_task(999)
        
        assert retrieved_task is None
    
    def test_get_all_tasks_empty(self):
        """Test getting all tasks when the list is empty."""
        tm = TaskManager()
        
        tasks = tm.get_all_tasks()
        
        assert tasks == []
    
    def test_get_all_tasks_with_tasks(self):
        """Test getting all tasks when the list has tasks."""
        tm = TaskManager()
        task1 = tm.add_task("First task")
        task2 = tm.add_task("Second task")
        
        tasks = tm.get_all_tasks()
        
        assert len(tasks) == 2
        assert task1 in tasks
        assert task2 in tasks
    
    def test_update_task_description(self):
        """Test updating a task's description."""
        tm = TaskManager()
        original_task = tm.add_task("Original task")
        
        updated_task = tm.update_task(original_task.id, "Updated task")
        
        assert updated_task is not None
        assert updated_task.id == original_task.id
        assert updated_task.description == "Updated task"
        assert tm.get_task(original_task.id).description == "Updated task"
    
    def test_update_task_not_found(self):
        """Test updating a non-existing task."""
        tm = TaskManager()
        
        result = tm.update_task(999, "Updated task")
        
        assert result is None
    
    def test_update_task_empty_description(self):
        """Test updating a task with an empty description."""
        tm = TaskManager()
        original_task = tm.add_task("Original task")
        
        with pytest.raises(ValueError):
            tm.update_task(original_task.id, "")
    
    def test_delete_task_found(self):
        """Test deleting an existing task."""
        tm = TaskManager()
        task = tm.add_task("Test task")
        
        result = tm.delete_task(task.id)
        
        assert result is True
        assert tm.get_task(task.id) is None
        assert len(tm.tasks) == 0
    
    def test_delete_task_not_found(self):
        """Test deleting a non-existing task."""
        tm = TaskManager()
        
        result = tm.delete_task(999)
        
        assert result is False
    
    def test_mark_complete_found(self):
        """Test marking an existing task as complete."""
        tm = TaskManager()
        task = tm.add_task("Test task")
        
        result = tm.mark_complete(task.id)
        
        assert result is not None
        assert result.id == task.id
        assert result.status == TaskStatus.COMPLETED
        assert tm.get_task(task.id).status == TaskStatus.COMPLETED
    
    def test_mark_complete_not_found(self):
        """Test marking a non-existing task as complete."""
        tm = TaskManager()
        
        result = tm.mark_complete(999)
        
        assert result is None
    
    def test_mark_pending_found(self):
        """Test marking an existing task as pending."""
        tm = TaskManager()
        task = tm.add_task("Test task")
        # First mark as complete
        tm.mark_complete(task.id)
        
        result = tm.mark_pending(task.id)
        
        assert result is not None
        assert result.id == task.id
        assert result.status == TaskStatus.PENDING
        assert tm.get_task(task.id).status == TaskStatus.PENDING
    
    def test_mark_pending_not_found(self):
        """Test marking a non-existing task as pending."""
        tm = TaskManager()
        
        result = tm.mark_pending(999)
        
        assert result is None
    
    def test_get_next_id(self):
        """Test getting the next available ID."""
        tm = TaskManager()
        
        next_id = tm.get_next_id()
        
        assert next_id == 1
        
        # Add a task to increment the ID
        tm.add_task("Test task")
        
        next_id = tm.get_next_id()
        
        assert next_id == 2