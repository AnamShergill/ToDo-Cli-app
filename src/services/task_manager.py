"""
TaskManager service for the CLI Todo application.

This module provides business logic for managing tasks in memory.
"""

from typing import Dict, List, Optional
from src.models.task import Task, TaskStatus


class TaskManager:
    """
    Manages tasks in memory with CRUD operations.
    
    This service handles all business logic related to task management,
    including adding, viewing, updating, deleting, and marking tasks as complete.
    """
    
    def __init__(self):
        """Initialize the TaskManager with an empty task storage."""
        self.tasks: Dict[int, Task] = {}
        self._next_id = 1
    
    def _generate_id(self) -> int:
        """
        Generate a unique ID for a new task.
        
        Returns:
            int: Unique ID for the new task
        """
        new_id = self._next_id
        self._next_id += 1
        return new_id
    
    def add_task(self, description: str) -> Task:
        """
        Add a new task to the task list.
        
        Args:
            description (str): Description of the task
            
        Returns:
            Task: The newly created task
            
        Raises:
            ValueError: If the description is empty or contains only whitespace
        """
        new_id = self._generate_id()
        task = Task(task_id=new_id, description=description)
        self.tasks[new_id] = task
        return task
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.
        
        Args:
            task_id (int): ID of the task to retrieve
            
        Returns:
            Task or None: The task if found, None otherwise
        """
        return self.tasks.get(task_id)
    
    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the task list.
        
        Returns:
            List[Task]: List of all tasks
        """
        return list(self.tasks.values())
    
    def update_task(self, task_id: int, new_description: Optional[str] = None) -> Optional[Task]:
        """
        Update a task's description.
        
        Args:
            task_id (int): ID of the task to update
            new_description (str, optional): New description for the task
            
        Returns:
            Task or None: The updated task if found, None otherwise
            
        Raises:
            ValueError: If the new description is empty or contains only whitespace
        """
        task = self.get_task(task_id)
        if task is None:
            return None
        
        if new_description is not None:
            task.update_description(new_description)
        
        return task
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.
        
        Args:
            task_id (int): ID of the task to delete
            
        Returns:
            bool: True if the task was deleted, False if it didn't exist
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False
    
    def mark_complete(self, task_id: int) -> Optional[Task]:
        """
        Mark a task as complete.
        
        Args:
            task_id (int): ID of the task to mark as complete
            
        Returns:
            Task or None: The updated task if found, None otherwise
        """
        task = self.get_task(task_id)
        if task is None:
            return None
        
        task.mark_completed()
        return task
    
    def mark_pending(self, task_id: int) -> Optional[Task]:
        """
        Mark a task as pending.
        
        Args:
            task_id (int): ID of the task to mark as pending
            
        Returns:
            Task or None: The updated task if found, None otherwise
        """
        task = self.get_task(task_id)
        if task is None:
            return None
        
        task.mark_pending()
        return task
    
    def get_next_id(self) -> int:
        """
        Get the next available ID without incrementing.
        
        Returns:
            int: The next available ID
        """
        return self._next_id