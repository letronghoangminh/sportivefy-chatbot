from retriever.retrieval import Retriever


class Controller:
    def __init__(self):
        self.retriever = Retriever()
        self.query = ""

    def embed_document(self, documents, metadatas):
        if documents is not None:
            self.retriever.add_new_documents(documents, metadatas)
        
    def retrieve(self, query):
        result = self.retriever.retrieve_text(query)
        return result
