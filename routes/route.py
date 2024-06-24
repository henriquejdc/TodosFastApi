from fastapi import APIRouter, HTTPException, status

from bson import ObjectId
from config.database import collection_name
from models.todos import Todo
from schema.schemas import individual_serializer, list_serializer

router = APIRouter()


def raise_not_found_exception(detail: str = "Todo not found"):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


@router.get(
    "/todo",
    response_model=list[Todo],
    response_description="Get all todos",
    status_code=status.HTTP_200_OK
)
async def get_todos():
    return list_serializer(collection_name.find())


@router.get(
    "/todo/{todo_id}",
    response_model=Todo,
    response_description="Get a todo by id",
    status_code=status.HTTP_200_OK
)
async def get_todo(todo_id: str):
    result = collection_name.find_one({"_id": ObjectId(todo_id)})

    if not result:
        raise_not_found_exception()

    return individual_serializer(result)


@router.post(
    "/todo",
    response_model=Todo,
    response_description="Create a new todo",
    status_code=status.HTTP_201_CREATED
)
async def create_todo(todo: Todo):
    collection_name.insert_one(todo.model_dump())
    return todo


@router.put(
    "/todo/{todo_id}",
    response_description="Update a todo by id",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_todo(todo_id: str, updated_todo: Todo):
    result = collection_name.find_one_and_update({"_id": ObjectId(todo_id)}, {"$set": updated_todo.model_dump()})

    if not result:
        raise_not_found_exception()


@router.delete(
    "/todo/{todo_id}",
    response_description="Update a todo by id",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_todo(todo_id: str):
    result = collection_name.find_one({"_id": ObjectId(todo_id)})

    if not result:
        raise_not_found_exception()

    collection_name.delete_one({"_id": ObjectId(todo_id)})
