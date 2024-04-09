from models.user_model import User
from models.task_model import Task
from typing import List
from schemas.task_schema import TaskCreate, TaskUpdate
from uuid import UUID

class TaskService:
    @staticmethod
    async def list_tasks(user: User) -> List[Task]:
        tasks = await Task.find(Task.owner.id == user.id).to_list()
        return tasks
    
    @staticmethod
    async def create_task(user: User, data: TaskCreate) -> Task:
        task = Task(**data.dict(), owner=user)
        return await task.insert()
    
    @staticmethod
    async def detail(user: User, task_id: UUID):
        task = await Task.find_one(Task.task_id == task_id, Task.owner.id == user.id)
        return task
    
    @staticmethod
    async def update_task(user: User, task_id: UUID, data: TaskUpdate):
        task = await TaskService.detail(user, task_id)
        await task.update({
            '$set': data.dict(
                exclude_unset=True
            )
        })
        await task.save()
        return task
    
    @staticmethod
    async def delete_task(user: User, task_id: UUID) -> None:
        task = await TaskService.detail(user, task_id)
        if task:
            await task.delete()
        return None