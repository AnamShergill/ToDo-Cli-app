# CLI Todo Application

A command-line todo application that stores tasks in memory. This application allows users to add, view, update, delete, and mark tasks as complete.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13+](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/badge/uv-package%20manager-blue)](https://github.com/astral-sh/uv)

## Features

- Add new tasks with descriptions
- View all tasks with their status in a colorful table format
- Update task descriptions
- Delete tasks
- Mark tasks as complete or pending
- Command-line interface with both interactive and command modes
- Colorful and formatted terminal output using the rich library

## Requirements

- Python 3.13 or higher
- uv package manager (for dependency management)
- rich library (for colorful terminal output)

## Installation

1. Clone or download the repository
2. Navigate to the project directory
3. Ensure you have Python 3.13+ and uv installed
4. Install dependencies using uv:

```bash
uv sync
```

## Usage

### Interactive Mode

Run the application without any arguments to enter interactive mode:

```bash
uv run python src/cli/main.py
```

In interactive mode, you can use the following commands:
- `add` - Add a new task
- `view` - View all tasks
- `update` - Update a task's description
- `delete` - Delete a task
- `complete` - Mark a task as complete
- `pending` - Mark a task as pending
- `help` - Show help information
- `exit` or `quit` - Exit the application

### Command Mode

Run the application with specific commands:

```bash
# Add a task
uv run python src/cli/main.py add "My new task"

# View all tasks
uv run python src/cli/main.py view

# Update a task (ID 1) with a new description
uv run python src/cli/main.py update 1 "Updated task description"

# Delete a task (ID 1)
uv run python src/cli/main.py delete 1

# Mark a task as complete (ID 1)
uv run python src/cli/main.py complete 1

# Mark a task as pending (ID 1)
uv run python src/cli/main.py pending 1
```

## Project Structure

```
src/
├── models/
│   └── task.py          # Task data model
├── services/
│   └── task_manager.py  # Business logic for task operations
├── cli/
│   └── main.py          # Command-line interface
└── lib/
    └── utils.py         # Utility functions
tests/
├── unit/
│   ├── test_task.py          # Unit tests for Task model
│   └── test_task_manager.py  # Unit tests for TaskManager
└── integration/
    └── test_cli.py      # Integration tests for CLI
```

## Testing

To run the tests, use pytest with uv:

```bash
# Run all tests
uv run python -m pytest

# Run unit tests only
uv run python -m pytest tests/unit/

# Run integration tests only
uv run python -m pytest tests/integration/
```

## Dependency Management

This project uses uv for dependency management:

- `uv sync` - Install dependencies from pyproject.toml
- `uv run` - Run commands in the project environment
- Dependencies are defined in `pyproject.toml`

## Architecture

The application follows a clean architecture pattern:

- **Models**: Define the data structures (Task model)
- **Services**: Contain the business logic (TaskManager)
- **CLI**: Handles user interface and command parsing
- **Lib**: Contains utility functions

## In-Memory Storage

All tasks are stored in memory during application execution. When the application exits, all tasks are lost. This design keeps the application simple and lightweight.

## Installation

1. Clone or download the repository
2. Navigate to the project directory
3. Ensure you have Python 3.13+ and uv installed
4. Install dependencies using uv:

```bash
uv sync
```

## Usage

### Interactive Mode

Run the application without any arguments to enter interactive mode:

```bash
uv run python src/cli/main.py
```

In interactive mode, you can use the following commands:
- `add` - Add a new task
- `view` - View all tasks
- `update` - Update a task's description
- `delete` - Delete a task
- `complete` - Mark a task as complete
- `pending` - Mark a task as pending
- `help` - Show help information
- `exit` or `quit` - Exit the application

### Command Mode

Run the application with specific commands:

```bash
# Add a task
uv run python src/cli/main.py add "My new task"

# View all tasks
uv run python src/cli/main.py view

# Update a task (ID 1) with a new description
uv run python src/cli/main.py update 1 "Updated task description"

# Delete a task (ID 1)
uv run python src/cli/main.py delete 1

# Mark a task as complete (ID 1)
uv run python src/cli/main.py complete 1

# Mark a task as pending (ID 1)
uv run python src/cli/main.py pending 1
```

## Project Structure

```
src/
├── models/
│   └── task.py          # Task data model
├── services/
│   └── task_manager.py  # Business logic for task operations
├── cli/
│   └── main.py          # Command-line interface
└── lib/
    └── utils.py         # Utility functions
tests/
├── unit/
│   ├── test_task.py          # Unit tests for Task model
│   └── test_task_manager.py  # Unit tests for TaskManager
└── integration/
    └── test_cli.py      # Integration tests for CLI
```

## Testing

To run the tests, use pytest with uv:

```bash
# Run all tests
uv run python -m pytest

# Run unit tests only
uv run python -m pytest tests/unit/

# Run integration tests only
uv run python -m pytest tests/integration/
```

## Dependency Management

This project uses uv for dependency management:

- `uv sync` - Install dependencies from pyproject.toml
- `uv run` - Run commands in the project environment
- Dependencies are defined in `pyproject.toml`

## Architecture

The application follows a clean architecture pattern:

- **Models**: Define the data structures (Task model)
- **Services**: Contain the business logic (TaskManager)
- **CLI**: Handles user interface and command parsing
- **Lib**: Contains utility functions

## In-Memory Storage

All tasks are stored in memory during application execution. When the application exits, all tasks are lost. This design keeps the application simple and lightweight.

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for more details on how to get started.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Python 3.13+
- Dependency management with uv
- Terminal formatting with rich
- Testing with pytest