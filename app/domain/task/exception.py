class TaskNotFoundError(Exception):

    message = "Task does not exist."

    def __str__(self) -> str:
        return TaskNotFoundError.message
