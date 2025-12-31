"""
Unit tests for the Task model.
"""

import pytest
from src.models.task import Task, TaskStatus


class TestTask:
    """Unit tests for the Task class."""
    
    def test_task_creation(self):
        """Test creating a new task with valid parameters."""
        task = Task(task_id=1, description="Test task")
        
        assert task.id == 1
        assert task.description == "Test task"
        assert task.status == TaskStatus.PENDING
    
    def test_task_creation_with_status(self):
        """Test creating a new task with a specific status."""
        task = Task(task_id=1, description="Test task", status=TaskStatus.COMPLETED)
        
        assert task.id == 1
        assert task.description == "Test task"
        assert task.status == TaskStatus.COMPLETED
    
    def test_task_creation_empty_description(self):
        """Test creating a task with an empty description raises ValueError."""
        with pytest.raises(ValueError):
            Task(task_id=1, description="")
    
    def test_task_creation_whitespace_description(self):
        """Test creating a task with whitespace-only description raises ValueError."""
        with pytest.raises(ValueError):
            Task(task_id=1, description="   ")
    
    def test_task_creation_strips_whitespace(self):
        """Test creating a task strips leading/trailing whitespace from description."""
        task = Task(task_id=1, description="  Test task  ")
        
        assert task.description == "Test task"
    
    def test_mark_completed(self):
        """Test marking a task as completed."""
        task = Task(task_id=1, description="Test task")
        
        task.mark_completed()
        
        assert task.status == TaskStatus.COMPLETED
    
    def test_mark_pending(self):
        """Test marking a task as pending."""
        task = Task(task_id=1, description="Test task", status=TaskStatus.COMPLETED)
        
        task.mark_pending()
        
        assert task.status == TaskStatus.PENDING
    
    def test_update_description(self):
        """Test updating a task's description."""
        task = Task(task_id=1, description="Original task")
        
        task.update_description("Updated task")
        
        assert task.description == "Updated task"
    
    def test_update_description_empty(self):
        """Test updating a task's description with empty string raises ValueError."""
        task = Task(task_id=1, description="Original task")
        
        with pytest.raises(ValueError):
            task.update_description("")
    
    def test_update_description_whitespace(self):
        """Test updating a task's description with whitespace-only raises ValueError."""
        task = Task(task_id=1, description="Original task")
        
        with pytest.raises(ValueError):
            task.update_description("   ")
    
    def test_update_description_strips_whitespace(self):
        """Test updating a task's description strips leading/trailing whitespace."""
        task = Task(task_id=1, description="Original task")
        
        task.update_description("  Updated task  ")
        
        assert task.description == "Updated task"
    
    def test_to_dict(self):
        """Test converting a task to dictionary representation."""
        task = Task(task_id=1, description="Test task", status=TaskStatus.COMPLETED)
        
        task_dict = task.to_dict()
        
        expected = {
            "id": 1,
            "description": "Test task",
            "status": "COMPLETED"
        }
        
        assert task_dict == expected
    
    def test_str_representation(self):
        """Test string representation of a task."""
        pending_task = Task(task_id=1, description="Pending task", status=TaskStatus.PENDING)
        completed_task = Task(task_id=2, description="Completed task", status=TaskStatus.COMPLETED)

        assert str(pending_task) == "[O] 1: Pending task"
        assert str(completed_task) == "[X] 2: Completed task"
    
    def test_repr_representation(self):
        """Test detailed string representation of a task."""
        task = Task(task_id=1, description="Test task", status=TaskStatus.COMPLETED)
        
        expected = "Task(id=1, description='Test task', status=TaskStatus.COMPLETED)"
        
        assert repr(task) == expected