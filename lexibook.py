import streamlit as st
from pdf_to_questions import pdf_to_questions
from summery_evaluator import evaluate
from utils import get_pdf_for_selected_chapter, get_vector_store_name_for_selected_chapter

import json

import asyncio

st.title("Lexi book MCQ wizard")

def build_question(count, json_question):

    if json_question.get(f"question") is not None:
        st.write("Question: ", json_question.get(f"question", ""))
        choices = ['A', 'B', 'C', 'D']
        selected_answer = st.selectbox(f"Select the correct response:", choices, key=f"select_{count}")
        for choice in choices:
            choice_str = json_question.get(f"{choice}", "None")
            st.write(f"{choice} {choice_str}")
                    
        color = ""
        if st.button("Submit", key=f"button_{count}"):
            rep = json_question.get(f"reponse")
            if selected_answer == rep:
                color = ":green"
                st.write(f":green[Correct response: {rep}]")
                
            else:
                color = ":red"
                st.write(f":red[Wrong answer. The correct answer is {rep}].")                

        st.write(f"{color}[Your response: {selected_answer}]")

        count += 1

    return count

txt = ""
choices_of_chapter = ['1', '2', '3', '4', '5', '6', '7']
selected_answer = st.selectbox(f"Select the chapter: Grade 10 Entrepreneurship Studies", choices_of_chapter, key=f"chapter_{7}")
txtSummery = st.text_area('Write a summry about selected section')

selected_file = get_pdf_for_selected_chapter(selected_answer)
selected_vector_store = get_vector_store_name_for_selected_chapter(selected_answer)

vector_store_path = "data/dbs/"+selected_vector_store
        
textEvaluate = st.button("Evaluate summery", key=f"button_summery")
if textEvaluate:
    summery_score = asyncio.run(evaluate(txtSummery, path=vector_store_path))
    if summery_score > 0.68:
        color = ":green"
        st.write(f":green[].")   
    else:
        color = ":red"
        st.write(f":red[].")  


if st.button("Generate Quiz", key=f"button_generator"):
   # if txt is not None:
    with st.spinner("Generating MCQs..."):
        st.session_state['questions'] = asyncio.run(pdf_to_questions(f"data/{selected_file}"))
        st.write("MCQ generation is successfull!")

if ('questions' in st.session_state):
    # Display question
    count = 0
    for json_question in st.session_state['questions']:

        count = build_question(count, json_question)
    