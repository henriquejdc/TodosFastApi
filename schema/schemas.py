from models.todos import Todo


def individual_serializer(todo: Todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "completed": todo["completed"],
    }


def list_serializer(todos: list[Todo]) -> list[dict]:
    return [individual_serializer(todo) for todo in todos]
