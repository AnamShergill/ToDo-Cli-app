# Data Model: CLI Todo Core Functionality

**Feature**: CLI Todo Core Functionality
**Date**: 2025-01-01
**Model Version**: 1.0

## Overview
Data model for the command-line todo application with in-memory storage.

## Task Entity

### Attributes
- **id** (integer)
  - Unique identifier for each task
  - Auto-generated when task is created
  - Primary key for lookups

- **description** (string)
  - Text content describing the task
  - Required field
  - Maximum length: 1000 characters

- **status** (enum)
  - Current completion status of the task
  - Values: "PENDING", "COMPLETED"
  - Default: "PENDING"

### Example
```json
{
  "id": 1,
  "description": "Complete the project specification",
  "status": "PENDING"
}
```

## In-Memory Storage Structure

### Task Storage
- **Type**: Dictionary (hash map)
- **Key**: Task ID (integer)
- **Value**: Task object
- **Access Time**: O(1) for lookups by ID

### Example Structure
```python
tasks = {
    1: {"description": "Complete the project specification", "status": "PENDING"},
    2: {"description": "Implement the CLI interface", "status": "COMPLETED"},
    3: {"description": "Write unit tests", "status": "PENDING"}
}
```

## Task Status Lifecycle

### Possible Transitions
- PENDING → COMPLETED (when task is marked complete)
- COMPLETED → PENDING (when task is marked incomplete, if feature is implemented)

### Initial State
- All newly created tasks start with status "PENDING"

## Validation Rules

### Task Creation
- Description must not be empty or contain only whitespace
- ID must be unique within the storage
- Status must be one of the allowed values

### Task Updates
- Description can be modified but must not become empty
- Status can be changed between allowed values
- ID cannot be changed

## Relationships
- No relationships needed as this is a single-entity model