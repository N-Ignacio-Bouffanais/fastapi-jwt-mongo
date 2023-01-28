def TaskEntity(task) -> dict:
    return {
        "id": str(task["id"]),
        "title": str(task["title"]),
        "description": str(task["description"]),
    }