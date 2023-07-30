def format(input_list):
    new_list = []
    for item in input_list:
        for key in item:
            if 'question1' in key or 'question2' in key or 'question3' in key:
                question_dict = {}
                question_num = key[-1]                
                question_dict[f'question'] = item[key]
                question_dict[f'A'] = item[f'A_{question_num}']
                question_dict[f'B'] = item[f'B_{question_num}']
                question_dict[f'C'] = item[f'C_{question_num}']
                question_dict[f'D'] = item[f'D_{question_num}']
                question_dict[f'reponse'] = item[f'reponse{question_num}']
                new_list.append(question_dict)

    return new_list    

def get_pdf_for_selected_chapter(selected_answer):

    selected_file = "Chapter_1.pdf"

    match selected_answer:
           case "1":
              selected_file = "Chapter_1.pdf"
           case "2":
                 selected_file = "Chapter_2.pdf"
           case "3":
                 selected_file = "Chapter_3.pdf"
           case "4":
                 selected_file = "Chapter_4.pdf"
           case "5":
                 selected_file = "Chapter_5.pdf"
           case "6":
                 selected_file = "Chapter_6.pdf"
           case "7":
                selected_file = "Chapter_7.pdf"
           case _:
                selected_file = "Chapter_1.pdf"
        
    return selected_file

def get_vector_store_name_for_selected_chapter(selected_answer):
    
    selected_vector_store = "Chapter_1.pdffaiss"

    match selected_answer:
           case "1":
              selected_vector_store = "Chapter_1.pdffaiss"
           case "2":
                 selected_vector_store = "Chapter_2.pdffaiss"
           case "3":
                 selected_vector_store = "Chapter_3.pdffaiss"
           case "4":
                 selected_vector_store = "Chapter_4.pdffaiss"
           case "5":
                 selected_vector_store = "Chapter_5.pdffaiss"
           case "6":
                 selected_vector_store = "Chapter_6.pdffaiss"
           case "7":
                selected_vector_store = "Chapter_7.pdffaiss"
           case _:
                selected_vector_store = "Chapter_1.pdffaiss"
        
    return selected_vector_store
        