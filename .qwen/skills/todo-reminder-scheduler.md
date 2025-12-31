---
name: todo-reminder-scheduler
description: Schedule and manage in-memory reminders for tasks and trigger notifications at the correct time
category: scheduling
---

# Todo Reminder Scheduler Skill

This skill enables scheduling and management of in-memory reminders for tasks, ensuring timely notifications are sent when due.

## Capabilities
- Create new reminders with specific due times
- Update existing reminders when requested
- Delete reminders when they're completed or cancelled
- Monitor all scheduled reminders and trigger notifications when they're due
- Maintain an in-memory database of all active reminders
- Provide status information about scheduled reminders

## Usage Guidelines
1. Parse incoming requests to understand the reminder details (task description, due time, notification method)
2. Calculate the appropriate trigger time based on the provided schedule
3. Store the reminder in the in-memory database with a unique identifier
4. Continuously monitor for due reminders and trigger notifications
5. Handle updates, deletions, and status queries for existing reminders
6. Ensure that all notifications are sent promptly when due

## Time Format Support
- Relative times like "in 5 minutes"
- Absolute times like "at 3:00 PM"
- Various time formats with timezone support when specified