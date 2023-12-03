from controller import Controller
from fastapi import FastAPI
from models.models import Document
from typing import Optional

controller = Controller()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "OK"}

@app.get("/query")
async def query(query: str):
    return controller.retrieve(query=query)

@app.post("/create_document")
async def create(document: Optional[Document]):
    if not isinstance(document, Document):
      raise ValueError('Invalid document')

    controller.embed_document([document.title + ' ' + document.content], metadatas=[{'author': document.author, 'title': document.title, 'post_id': document.post_id, 'sport_type': document.sport_type}])
    return {"message": "Document created"}
