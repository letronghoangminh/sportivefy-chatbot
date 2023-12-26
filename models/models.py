from pydantic import BaseModel

class Document(BaseModel):
    author: str = None
    body: str = None
    title: str = None
    slug: str = None
    sport_type: str = None
