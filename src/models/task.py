"""
Task model for the CLI Todo application.

This module defines the Task data structure used in the application.
"""

from enum import Enum
from typing import Optional


class TaskStatus(Enum):
    """Enumeration for task status values."""
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"


class Task:
    """
    Represents a single todo item with ID, description, and status.
    
    Attributes:
        id (int): Unique identifier for the task
        description (str): Text content describing the task
        status (TaskStatus): Current completion status of the task
    """
    
    def __init__(self, task_id: int, description: str, status: TaskStatus = TaskStatus.PENDING):
        """
        Initialize a new Task instance.
        
        Args:
            task_id (int): Unique identifier for the task
            description (str): Text content describing the task
            status (TaskStatus): Current completion status of the task (default: PENDING)
        """
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty or contain only whitespace")
        
        self.id = task_id
        self.description = description.strip()
        self.status = status
    
    def mark_completed(self):
        """Mark the task as completed."""
        self.status = TaskStatus.COMPLETED
    
    def mark_pending(self):
        """Mark the task as pending."""
        self.status = TaskStatus.PENDING
    
    def update_description(self, new_description: str):
        """
        Update the task description.
        
        Args:
            new_description (str): New description for the task
        """
        if not new_description or not new_description.strip():
            raise ValueError("Task description cannot be empty or contain only whitespace")
        
        self.description = new_description.strip()
    
    def to_dict(self) -> dict:
        """
        Convert the task to a dictionary representation.
        
        Returns:
            dict: Dictionary representation of the task
        """
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status.value
        }
    
    def __str__(self) -> str:
        """
        String representation of the task for display.

        Returns:
            str: Formatted string representation of the task
        """
        status_symbol = "X" if self.status == TaskStatus.COMPLETED else "O"
        return f"[{status_symbol}] {self.id}: {self.description}"
    
    def __repr__(self) -> str:
        """
        Detailed string representation of the task.
        
        Returns:
            str: Detailed string representation of the task
        """
        return f"Task(id={self.id}, description='{self.description}', status={self.status})"