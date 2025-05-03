from pydantic import BaseModel


class DatabaseCreatePost(BaseModel):
    title: str
    content: str


class ReadPost(DatabaseCreatePost):
    id: int


class UpdatePost(DatabaseCreatePost):
    pass