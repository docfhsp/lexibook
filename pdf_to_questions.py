import asyncio
from langchain.document_loaders import PyPDFLoader
from question_generator import generate_questions
from utils import format

async def pdf_to_questions(pdf_file_name):


    pdf_file_loader = PyPDFLoader(pdf_file_name)
    
    pages = pdf_file_loader.load_and_split()

    sem = asyncio.Semaphore(10)  # Set the maximum number of parallel tasks

    async def process_page(page):
        async with sem:
            return await generate_questions(page.page_content)

    tasks = []
    for page in pages:
        task = process_page(page)
        tasks.append(task)

    formatted_questions = []

    questions = await asyncio.gather(*tasks)    
    
    for question in questions:
        formatted_questions.extend(format(question[0]))

    return formatted_questions
  
