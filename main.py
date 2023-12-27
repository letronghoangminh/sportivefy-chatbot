from controller import Controller
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.models import Document
from typing import Optional

controller = Controller()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

    controller.embed_document([document.title + ' ' + document.body], metadatas=[{'author': document.author, 'title': document.title, 'slug': document.post_id, 'sport_type': document.sport_type}])
    return {"message": "Document created"}
