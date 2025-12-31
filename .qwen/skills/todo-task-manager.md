---
name: todo-task-manager
description: Manage CRUD operations for an in-memory CLI todo application
category: task-management
---

# Todo Task Manager Skill

This skill handles all CRUD operations for an in-memory todo list system, including creating, reading, updating, and deleting tasks while maintaining data integrity.

## Capabilities
- Create new tasks with titles, descriptions, due dates, and priority levels
- Read and display tasks in various formats (all tasks, completed tasks, pending tasks, by priority, by due date)
- Update existing tasks including status, priority, due dates, and descriptions
- Delete tasks based on ID or other criteria
- Mark tasks as complete/incomplete
- Filter and sort tasks based on various criteria
- Provide clear, concise feedback on all operations

## Task Structure
- ID (auto-generated)
- Title
- Description
- Status (pending/completed)
- Priority (low/medium/high)
- Creation Date
- Due Date (optional)
- Completion Date (when applicable)

## Usage Guidelines
1. Validate user input before performing operations
2. Provide clear confirmation messages after each operation
3. Handle errors gracefully and provide helpful error messages
4. Maintain an in-memory data store for tasks (no persistence between sessions)
5. Use consistent, readable format when displaying tasks
6. Implement partial updates (only specified fields need to be changed)
7. Implement search functionality to find tasks by title or description
8. Allow bulk operations where appropriate (e.g., mark multiple tasks as complete)

## Output Format
- Include task ID, title, status, priority, and due date in listings
- Provide success/error messages that are informative and actionable
- Use numbered format for easy reference when listing tasks
- Use YYYY-MM-DD consistently for date formats