
# ./Data/question_data.py
import pandas as pd
from Data.queries import get_question_query, get_tagging_query
from Data.collections import jee_collection, neet_collection
from Processing.process_user_inputs import clean_ids_input
from config import MAX_QUESTION_IDS

def get_question_data(exam_id, question_ids):

    question_ids = clean_ids_input(question_ids)
    question_ids = question_ids[:MAX_QUESTION_IDS]
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

def get_tagging_data(exam_id, question_ids):

    question_ids = clean_ids_input(question_ids)

    if exam_id == '1':
        collection = jee_collection
    elif exam_id == '2':
        collection = neet_collection
    else:
        return None
    
    tagging_query = get_tagging_query(question_ids)
    tagging_data_cursor = collection.aggregate(tagging_query)
    tagging_data_list = list(tagging_data_cursor)
    tagging_data = pd.DataFrame(tagging_data_list)
    return tagging_data