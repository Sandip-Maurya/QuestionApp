
# ./Data/question_data.py
import pandas as pd
from Data.queries import get_question_query
from Data.collections import jee_collection, neet_collection
from Processing.process_user_inputs import clean_ids_input

def get_question_data(exam_id, question_ids):

    question_ids = clean_ids_input(question_ids)

    if exam_id == '1':
        collection = jee_collection
    elif exam_id == '2':
        collection = neet_collection
    else:
        return None
    
    question_query = get_question_query(question_ids)
    question_data_cursor = collection.aggregate(question_query)
    question_data_list = list(question_data_cursor)
    question_data = pd.DataFrame(question_data_list)
    return question_data
