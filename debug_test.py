from src.models.task import Task, TaskStatus
from src.services.task_manager import TaskManager

tm = TaskManager()
task = tm.add_task('Test task')
print(f'Initial task status: {task.status}')
completed_task = tm.mark_complete(1)
print(f'After marking complete: {completed_task.status if completed_task else None}')
print(f'Expected: {TaskStatus.COMPLETED}')
print(f'Are they equal? {completed_task.status == TaskStatus.COMPLETED if completed_task else False}')