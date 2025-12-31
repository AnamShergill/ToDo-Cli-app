"""
Command-line interface for the Todo application.

This module provides the main CLI interface for interacting with the todo list.
Uses the rich library for colorful and formatted terminal output.
"""

import sys
import argparse
import os
from typing import Optional

# Add the src directory to the Python path to allow imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.prompt import Prompt
from rich.panel import Panel
from rich import print

from src.services.task_manager import TaskManager
from src.lib.utils import (
    validate_task_description,
    format_task_list,
    format_single_task,
    validate_task_id
)

# Initialize rich console
console = Console()


class TodoCLI:
    """
    Command-line interface for the Todo application.
    
    This class handles all CLI interactions and maps commands to the appropriate
    functionality in the TaskManager service.
    """
    
    def __init__(self):
        """Initialize the CLI with a TaskManager instance."""
        self.task_manager = TaskManager()

    def add_task(self, description: str) -> str:
        """
        Add a new task to the list.

        Args:
            description (str): Description of the task to add

        Returns:
            str: Result message
        """
        if not validate_task_description(description):
            return "[red]Error: Task description cannot be empty.[/red]"

        try:
            task = self.task_manager.add_task(description)
            return f"[green]Task added successfully with ID {task.id}: {task.description}[/green]"
        except ValueError as e:
            return f"[red]Error: {str(e)}[/red]"

    def view_tasks(self) -> str:
        """
        View all tasks in the list using a rich table format.

        Returns:
            str: Formatted list of all tasks in a table
        """
        tasks = self.task_manager.get_all_tasks()

        if not tasks:
            console.print("[yellow]No tasks found.[/yellow]")
            return ""

        # Create a rich table for displaying tasks
        table = Table(title="Todo Tasks", title_style="bold blue")
        table.add_column("ID", style="bold cyan", justify="center")
        table.add_column("Title", style="bold white")
        table.add_column("Description", style="white")
        table.add_column("Status", justify="center")

        for task in tasks:
            status_style = "green" if task.status.name == "COMPLETED" else "red"
            status_symbol = "X" if task.status.name == "COMPLETED" else "O"
            status_text = f"[{status_style}]{status_symbol} {task.status.name}[/]"

            table.add_row(
                str(task.id),
                task.description.split()[0] if task.description.split() else task.description,  # Using first word as title
                task.description,
                status_text
            )

        console.print(table)
        return ""

    def update_task(self, task_id_str: str, new_description: str) -> str:
        """
        Update a task's description.

        Args:
            task_id_str (str): String representation of the task ID
            new_description (str): New description for the task

        Returns:
            str: Result message
        """
        task_id = validate_task_id(task_id_str)
        if task_id is None:
            return "[red]Error: Invalid task ID. Please provide a valid number.[/red]"

        if not validate_task_description(new_description):
            return "[red]Error: Task description cannot be empty.[/red]"

        task = self.task_manager.update_task(task_id, new_description)
        if task:
            return f"[green]Task updated: [bold]{task}[/][/green]"
        else:
            return f"[red]Task with ID {task_id} not found.[/red]"

    def delete_task(self, task_id_str: str) -> str:
        """
        Delete a task by its ID.

        Args:
            task_id_str (str): String representation of the task ID

        Returns:
            str: Result message
        """
        task_id = validate_task_id(task_id_str)
        if task_id is None:
            return "[red]Error: Invalid task ID. Please provide a valid number.[/red]"

        if self.task_manager.delete_task(task_id):
            return f"[green]Task with ID {task_id} deleted successfully.[/green]"
        else:
            return f"[red]Task with ID {task_id} not found.[/red]"

    def mark_complete(self, task_id_str: str) -> str:
        """
        Mark a task as complete.

        Args:
            task_id_str (str): String representation of the task ID

        Returns:
            str: Result message
        """
        task_id = validate_task_id(task_id_str)
        if task_id is None:
            return "[red]Error: Invalid task ID. Please provide a valid number.[/red]"

        task = self.task_manager.mark_complete(task_id)
        if task:
            return f"[green]Task marked complete: [bold]{task}[/][/green]"
        else:
            return f"[red]Task with ID {task_id} not found.[/red]"

    def mark_pending(self, task_id_str: str) -> str:
        """
        Mark a task as pending.

        Args:
            task_id_str (str): String representation of the task ID

        Returns:
            str: Result message
        """
        task_id = validate_task_id(task_id_str)
        if task_id is None:
            return "[red]Error: Invalid task ID. Please provide a valid number.[/red]"

        task = self.task_manager.mark_pending(task_id)
        if task:
            return f"[green]Task marked pending: [bold]{task}[/][/green]"
        else:
            return f"[red]Task with ID {task_id} not found.[/red]"
    
    def run_interactive(self):
        """Run the interactive CLI mode."""
        console.print(Panel("[bold blue]Welcome to the Todo CLI Application![/bold blue]", expand=False))
        console.print("[bold]Commands:[/bold] [cyan]add[/cyan], [cyan]view[/cyan], [cyan]update[/cyan], [cyan]delete[/cyan], [cyan]complete[/cyan], [cyan]pending[/cyan], [cyan]help[/cyan], [cyan]exit[/cyan]")
        console.print("[italic]Type 'help' for more information on commands.[/italic]\n")

        while True:
            try:
                command = Prompt.ask("[bold green]Enter command[/bold green]").strip().lower()

                if command == "exit" or command == "quit":
                    console.print("[bold yellow]Goodbye![/bold yellow]")
                    break
                elif command == "help":
                    self.show_help()
                elif command == "add":
                    description = Prompt.ask("[bold cyan]Enter task description[/bold cyan]")
                    result = self.add_task(description)
                    console.print(result)
                elif command == "view":
                    self.view_tasks()
                elif command == "update":
                    task_id = Prompt.ask("[bold cyan]Enter task ID to update[/bold cyan]")
                    new_description = Prompt.ask("[bold cyan]Enter new description[/bold cyan]")
                    result = self.update_task(task_id, new_description)
                    console.print(result)
                elif command == "delete":
                    task_id = Prompt.ask("[bold cyan]Enter task ID to delete[/bold cyan]")
                    result = self.delete_task(task_id)
                    console.print(result)
                elif command == "complete":
                    task_id = Prompt.ask("[bold cyan]Enter task ID to mark complete[/bold cyan]")
                    result = self.mark_complete(task_id)
                    console.print(result)
                elif command == "pending":
                    task_id = Prompt.ask("[bold cyan]Enter task ID to mark pending[/bold cyan]")
                    result = self.mark_pending(task_id)
                    console.print(result)
                else:
                    console.print(f"[red]Unknown command: {command}. Type 'help' for available commands.[/red]")

                console.print()  # Empty line for readability

            except KeyboardInterrupt:
                console.print("\n[bold yellow]Goodbye![/bold yellow]")
                break
            except EOFError:
                console.print("\n[bold yellow]Goodbye![/bold yellow]")
                break
    
    def show_help(self):
        """Display help information for available commands."""
        help_text = """
[bold blue]Available commands:[/bold blue]
  [cyan]add[/cyan]          - Add a new task
  [cyan]view[/cyan]         - View all tasks
  [cyan]update[/cyan]       - Update a task's description
  [cyan]delete[/cyan]       - Delete a task
  [cyan]complete[/cyan]     - Mark a task as complete
  [cyan]pending[/cyan]      - Mark a task as pending
  [cyan]help[/cyan]         - Show this help message
  [cyan]exit/quit[/cyan]    - Exit the application

[bold blue]Examples:[/bold blue]
  [cyan]add[/cyan] - Add a task: Just type 'add' and follow the prompts
  [cyan]view[/cyan] - View all tasks: Type 'view'
  [cyan]complete[/cyan] - Mark task #1 as complete: Type 'complete' and enter '1'
        """
        console.print(Panel(help_text, title="[bold green]Help[/bold green]", expand=False))
    
    def run_with_args(self):
        """Parse command line arguments and execute the appropriate command."""
        parser = argparse.ArgumentParser(description="CLI Todo Application")
        subparsers = parser.add_subparsers(dest="command", help="Available commands")

        # Add command
        add_parser = subparsers.add_parser("add", help="Add a new task")
        add_parser.add_argument("description", nargs="*", help="Description of the task")

        # View command
        subparsers.add_parser("view", help="View all tasks")

        # Update command
        update_parser = subparsers.add_parser("update", help="Update a task")
        update_parser.add_argument("id", help="ID of the task to update")
        update_parser.add_argument("description", nargs="*", help="New description of the task")

        # Delete command
        delete_parser = subparsers.add_parser("delete", help="Delete a task")
        delete_parser.add_argument("id", help="ID of the task to delete")

        # Complete command
        complete_parser = subparsers.add_parser("complete", help="Mark a task as complete")
        complete_parser.add_argument("id", help="ID of the task to mark complete")

        # Pending command
        pending_parser = subparsers.add_parser("pending", help="Mark a task as pending")
        pending_parser.add_argument("id", help="ID of the task to mark pending")

        args = parser.parse_args()

        if args.command == "add":
            if args.description:
                description = " ".join(args.description)
                result = self.add_task(description)
                console.print(result)
            else:
                console.print("[red]Error: Please provide a task description.[/red]")

        elif args.command == "view":
            self.view_tasks()

        elif args.command == "update":
            if args.description:
                new_description = " ".join(args.description)
                result = self.update_task(args.id, new_description)
                console.print(result)
            else:
                console.print("[red]Error: Please provide a new description for the task.[/red]")

        elif args.command == "delete":
            result = self.delete_task(args.id)
            console.print(result)

        elif args.command == "complete":
            result = self.mark_complete(args.id)
            console.print(result)

        elif args.command == "pending":
            result = self.mark_pending(args.id)
            console.print(result)

        elif args.command is None:
            # No command provided, run interactive mode
            self.run_interactive()
        else:
            parser.print_help()


def main():
    """Main entry point for the CLI application."""
    cli = TodoCLI()
    
    # If no command line arguments provided, run interactive mode
    if len(sys.argv) == 1:
        cli.run_interactive()
    else:
        cli.run_with_args()


if __name__ == "__main__":
    main()