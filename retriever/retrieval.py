from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models.openai import ChatOpenAI
from langchain.schema import StrOutputParser
from langchain.vectorstores import Chroma

import config as cfg

class Retriever:
    def __init__(self):
        embeddings = OpenAIEmbeddings(
            openai_api_key=cfg.OPENAI_API_KEY,
            chunk_size=cfg.OPENAI_EMBEDDINGS_CHUNK_SIZE,
        )
      
        prompt_template = """You are an intelligent AI about sport news which analyses information from known knowledge and 
        answers the user's questions. You answer all questions by Vietnamese. 
        If you don't know the result, please say that you don't know, avoid making things up.
        Question: {question} 
        Answer:
        """

        prompt = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
        )
        
        self.k = 5
        
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=cfg.CHARACTER_SPLITTER_CHUNK_SIZE,
            chunk_overlap=0,
        )
        
        self.db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
        
        self.runnable = prompt | ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=cfg.OPENAI_API_KEY) | StrOutputParser()
        
        self.vector_store_retriever = self.db.as_retriever(search_type="similarity_score_threshold", search_kwargs={"k": self.k, "distance_metric": "cos", "score_threshold": .8})

    def add_new_documents(self, texts, metadatas):
        docs = self.text_splitter.create_documents(texts, metadatas=metadatas)
        self.db.add_documents(docs)

    def retrieve_text(self, query):
      try:
        response = self.vector_store_retriever.get_relevant_documents(query)
        retriever_flag = True
        if len(list(response)) == 0:
          retriever_flag = False
        
        if retriever_flag:
          result = []
          for document in list(response):
            slug = document.metadata['slug']
            title = document.metadata['title']
            result.append(f'Bài báo liên quan với tiêu đề "{title}": {cfg.WEB_BASE_URL}/posts/{slug}')
        else:
          response = self.runnable.invoke({'question': query})
          result = response

        return {'result': result}
      except Exception as e:
        print(e)
        return {'result': 'Không tìm thấy dữ liệu về thông tin này'}
