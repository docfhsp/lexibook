import asyncio
from langchain.document_loaders import PyPDFLoader

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader

async def evaluate(text,path):
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local(path, embeddings)
    docs = db.similarity_search_with_score(text,distance_metric='cos',k=20)

    print("the similarity score =",docs[0][1])
    
    return docs[0][1]
    
  
