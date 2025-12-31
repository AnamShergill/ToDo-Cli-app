# Quickstart Guide: CLI Todo Core Functionality

**Feature**: CLI Todo Core Functionality
**Date**: 2025-01-01
**Version**: 1.0

## Overview
Quickstart guide to get the command-line todo application up and running.

## Prerequisites
- Python 3.13 or higher
- pip (Python package installer)

## Setup Instructions

### 1. Clone or Create the Project Structure
```bash
mkdir todo-cli
cd todo-cli
```

### 2. Create the Directory Structure
```bash
mkdir -p src/models src/services src/cli src/lib tests/unit tests/integration
```

### 3. Verify Python Version
```bash
python --version
# Should show Python 3.13.x
```

## Running the Application

### 1. Navigate to the Project Directory
```bash
cd src/cli
```

### 2. Run the Application
```bash
python main.py
```

## Basic Usage

### Adding a Task
```bash
python main.py add "Buy groceries"
```

### Viewing All Tasks
```bash
python main.py view
```

### Marking a Task as Complete
```bash
python main.py complete 1
```

### Updating a Task
```bash
python main.py update 1 "Buy groceries and cook dinner"
```

### Deleting a Task
```bash
python main.py delete 1
```

## Interactive Mode
Run without arguments to enter interactive mode:
```bash
python main.py
# Then follow the prompts to select operations
```

## Running Tests
```bash
# From the project root
python -m pytest tests/
```

## Troubleshooting

### Python Version Issues
If you get a Python version error:
- Ensure Python 3.13+ is installed
- Use `python3` instead of `python` on some systems

### Module Import Issues
If you get import errors:
- Ensure you're running from the correct directory
- Check that all files are in the correct locations