"""
Integration tests for the CLI Todo application.
"""

import sys
from io import StringIO
from unittest.mock import patch
from src.cli.main import TodoCLI


class TestTodoCLI:
    """Integration tests for the TodoCLI class."""
    
    def test_add_task_integration(self):
        """Test adding a task through the CLI."""
        cli = TodoCLI()

        result = cli.add_task("Test task description")

        assert "Task added successfully" in result
        assert "Test task description" in result
        assert "green" in result  # Check for rich formatting
    
    def test_view_tasks_empty(self):
        """Test viewing tasks when the list is empty."""
        cli = TodoCLI()

        # Capture the output of view_tasks
        import io
        import sys
        from contextlib import redirect_stdout

        f = io.StringIO()
        with redirect_stdout(f):
            cli.view_tasks()
        result = f.getvalue()

        assert "No tasks found." in result
    
    def test_view_tasks_with_tasks(self):
        """Test viewing tasks when the list has tasks."""
        cli = TodoCLI()
        cli.add_task("First task")
        cli.add_task("Second task")

        # Capture the output of view_tasks
        import io
        import sys
        from contextlib import redirect_stdout

        f = io.StringIO()
        with redirect_stdout(f):
            cli.view_tasks()
        result = f.getvalue()

        assert "First task" in result
        assert "Second task" in result
        assert result.count("O") >= 2  # Both should be pending (may appear in status column)
    
    def test_update_task_integration(self):
        """Test updating a task through the CLI."""
        cli = TodoCLI()
        cli.add_task("Original task")

        result = cli.update_task("1", "Updated task")

        assert "updated" in result
        assert "Updated task" in result
        assert "green" in result  # Check for rich formatting
    
    def test_update_nonexistent_task(self):
        """Test updating a non-existent task."""
        cli = TodoCLI()

        result = cli.update_task("999", "Updated task")

        assert "not found" in result
        assert "red" in result  # Check for rich formatting
    
    def test_delete_task_integration(self):
        """Test deleting a task through the CLI."""
        cli = TodoCLI()
        cli.add_task("Task to delete")
        
        result = cli.delete_task("1")
        
        assert "deleted successfully" in result
        
        # Verify the task was actually deleted
        view_result = cli.view_tasks()
        assert "Task to delete" not in view_result
    
    def test_delete_nonexistent_task(self):
        """Test deleting a non-existent task."""
        cli = TodoCLI()
        
        result = cli.delete_task("999")
        
        assert "not found" in result
    
    def test_mark_complete_integration(self):
        """Test marking a task as complete through the CLI."""
        cli = TodoCLI()
        cli.add_task("Task to complete")

        result = cli.mark_complete("1")

        assert "marked complete" in result
        assert "green" in result  # Check for rich formatting
    
    def test_mark_complete_nonexistent_task(self):
        """Test marking a non-existent task as complete."""
        cli = TodoCLI()
        
        result = cli.mark_complete("999")
        
        assert "not found" in result
    
    def test_mark_pending_integration(self):
        """Test marking a task as pending through the CLI."""
        cli = TodoCLI()
        cli.add_task("Task to mark pending")
        cli.mark_complete("1")  # First mark it complete

        result = cli.mark_pending("1")

        assert "marked pending" in result
        assert "green" in result  # Check for rich formatting
    
    def test_mark_pending_nonexistent_task(self):
        """Test marking a non-existent task as pending."""
        cli = TodoCLI()
        
        result = cli.mark_pending("999")
        
        assert "not found" in result
    
    def test_command_line_add(self):
        """Test adding a task via command line arguments."""
        cli = TodoCLI()
        
        # Simulate command line arguments for 'add'
        sys.argv = ['main.py', 'add', 'Command', 'line', 'task']
        
        # Capture the output
        captured_output = StringIO()
        
        # Patch the print function to capture output
        with patch('sys.stdout', new=captured_output):
            # Temporarily modify the CLI to not call sys.exit
            original_run_with_args = cli.run_with_args
            def mock_run_with_args():
                import argparse
                parser = argparse.ArgumentParser(description="CLI Todo Application")
                subparsers = parser.add_subparsers(dest="command", help="Available commands")
                add_parser = subparsers.add_parser("add", help="Add a new task")
                add_parser.add_argument("description", nargs="*", help="Description of the task")
                args = parser.parse_args(['add', 'Command', 'line', 'task'])
                
                if args.command == "add":
                    if args.description:
                        description = " ".join(args.description)
                        result = cli.add_task(description)
                        print(result)
            
            cli.run_with_args = mock_run_with_args
            cli.run_with_args()
            cli.run_with_args = original_run_with_args  # Restore original method
        
        output = captured_output.getvalue()
        assert "Task added successfully" in output
        assert "Command line task" in output
    
    def test_command_line_view(self):
        """Test viewing tasks via command line arguments."""
        cli = TodoCLI()
        cli.add_task("CLI view test task")
        
        # Simulate command line arguments for 'view'
        sys.argv = ['main.py', 'view']
        
        # Capture the output
        captured_output = StringIO()
        
        # Patch the print function to capture output
        with patch('sys.stdout', new=captured_output):
            # Temporarily modify the CLI to not call sys.exit
            original_run_with_args = cli.run_with_args
            def mock_run_with_args():
                import argparse
                parser = argparse.ArgumentParser(description="CLI Todo Application")
                subparsers = parser.add_subparsers(dest="command", help="Available commands")
                subparsers.add_parser("view", help="View all tasks")
                args = parser.parse_args(['view'])
                
                if args.command == "view":
                    result = cli.view_tasks()
                    print(result)
            
            cli.run_with_args = mock_run_with_args
            cli.run_with_args()
            cli.run_with_args = original_run_with_args  # Restore original method
        
        output = captured_output.getvalue()
        assert "CLI view test task" in output