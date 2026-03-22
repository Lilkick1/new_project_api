import logging
from typing import Any, List
import pytest
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_user_response import CreateUserResponse


@pytest.fixture
def created_obj():
    object: List[Any] = []
    yield object
    clean_user(object)

def clean_user(object: List[Any]):
    api_manager = ApiManager(object)
    for u in object:
        if isinstance(u, CreateUserResponse):
            api_manager.admin_steps.delete_user(u.id)
        else:
            logging.warning(f"Error in delete user_id: {u.id}")
