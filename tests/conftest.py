import pytest
from bson import ObjectId


# Mock do banco de dados
class MockCollection:

    def __init__(self):
        self.todos = [
            {
                "_id": ObjectId("60af884a6d1b2c6b55b0d36c"),
                "name": "First Todo",
                "description": "This is the first todo",
                "completed": True
            },
            {
                "_id": ObjectId("60af884a6d1b2c6b55b0d36d"),
                "name": "Second Todo",
                "description": "This is the second todo",
                "completed": True
            }
        ]

    def find(self):
        return self.todos

    def find_one(self, query):
        return next((todo for todo in self.todos if todo["_id"] == query["_id"]), None)

    def insert_one(self, todo):
        self.todos.append(todo)
        return None

    def find_one_and_update(self, query, update):
        todo = self.find_one(query)
        if todo:
            todo.update(update["$set"])
            return todo
        return None

    def delete_one(self, query):
        todo = self.find_one(query)
        if todo:
            self.todos.remove(todo)
            return todo
        return None


@pytest.fixture
def mock_db():
    return MockCollection()
