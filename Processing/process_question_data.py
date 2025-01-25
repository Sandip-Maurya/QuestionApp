# Processing/process_question_data.py
import pandas as pd
from Processing.process_option_and_ans import (
    process_option, 
    process_answer, 
    process_correct_option
)
from Data.mappings_data import (
    EXAM_MAP, 
    SUBJECT_MAP, 
    CHAPTER_MAP, 
    TOPIC_MAP,
    CATEGORY_MAP,
    TEMPLATE_MAP, 
)

def process_tagging(question_data):
    question_data['EXAM'] = question_data['classId'].map(EXAM_MAP)
    question_data['SUBJECT'] = question_data['subjectId'].map(SUBJECT_MAP)
    question_data['CHAPTER'] = question_data['chapterId'].map(CHAPTER_MAP)
    question_data['TOPIC'] = question_data['topicId'].map(TOPIC_MAP)
    question_data['Q_TEMPLATE'] = question_data['templateType'].map(TEMPLATE_MAP)
    question_data['Q_CATEGORY'] = question_data['questionCategory'].map(CATEGORY_MAP)
    question_data.index = pd.Index(range(1, len(question_data)+1 ), name='Q_NO')
    question_data['S_No'] = question_data.index
    question_data.rename(columns={'_id': 'Q_ID', 'quesStatus': 'Q_STATUS'}, inplace=True)
    return question_data

def process_content(question_data):

    question_data['Option-1'] = question_data['questionOptions'].apply( process_option, args=("1",) )
    question_data['Option-2'] = question_data['questionOptions'].apply( process_option, args=("2",) )
    question_data['Option-3'] = question_data['questionOptions'].apply( process_option, args=("3",) )
    question_data['Option-4'] = question_data['questionOptions'].apply( process_option, args=("4",) )   
    
    question_data['Answer'] = question_data['answers'].apply( process_answer )
    question_data['Correct_Option'] = question_data['answers'].apply( process_correct_option )

    return question_data

def process_question_data(question_data):
    question_data = process_tagging(question_data)
    question_data = process_content(question_data)
    return question_data

