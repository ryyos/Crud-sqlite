
from src.repository.repository import Repository
from typing import List, Dict

class Service(Repository):
    def __init__(self) -> None:
        super().__init__()

    def create(self, name: str, username: str, ages: int) -> List[Dict[str, any]]:
        if self.search_by_username(username):
            return 'USERNAME ALREADY EXISTS'
        else:
            self.add_data(name, username, ages)
            return 'DATA ADDED SUCCESSFULLY'
        ...

    def read(self, username: str) -> Dict[str, any] | str:
        if not self.search_by_username(username):
            return 'USERNAME NOT FOUND'
        else:
            return self.search_by_username(username)
        ...

    def update(self, name: str, username: str, ages: int) -> str:
        if not self.search_by_username(username):
            return 'USERNAME NOT FOUND'
        else:
            self.update_data(name, username, ages)
            return 'DATA UPDATE SUCCESSFULLY'
        ...

    def delete(self, username: str) -> str:
        if not self.search_by_username(username):
            return 'USERNAME NOT FOUND'
        else:
            self.delete_data(username)
            return 'DATA DELETE SUCCESSFULLY'
    