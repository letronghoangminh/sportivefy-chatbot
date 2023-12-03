from pydantic import BaseModel

class Document(BaseModel):
    author: str = None
    content: str = None
    title: str = None
    post_id: int = None
    sport_type: str = None
