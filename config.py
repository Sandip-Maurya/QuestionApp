# ./config.py
import os
import dotenv

dotenv.load_dotenv()

MONGODB_CONNECTION_URL = os.getenv('MONGODB_CONNECTION_URL')
JEE_DB_Name = 'qandi_question_bank_jee'
NEET_DB_Name = 'qandi_question_bank_neet'
ADMIN_DB_Name = 'qandi_admin'
QUESTIONS_COLLECTION_NAME = 'questionBank'
CHAPTER_COLLECTION_NAME = 'examSubjectChapters'
TOPIC_COLLECTION_NAME = 'topics'
MAX_QUESTION_IDS = 200

EXAM_NAME_TO_ID = {
    'JEE Main':"1",
    'NEET': "2"
}
EXAMS = list(EXAM_NAME_TO_ID.keys())

IDS_INPUT_MESSAGE = '''Example: 3085, 20678, 2055 or 
225453
188994
184873
'''

TAGGING_COLUMNS = [
    'S_No',
    'Q_ID',
    'EXAM',
    'SUBJECT',
    'CHAPTER',
    'TOPIC',
    'Q_DIFFICULTY',
    'Q_CATEGORY',
    'Q_TEMPLATE',
    'Q_STATUS',
]

CONTENT_COLUMNS = [
    'Q_ID',
    'EXAM',
    'SUBJECT',
    'CHAPTER',
    'Q_TEMPLATE',
    'question',
    'Option-1',
    'Option-2',
    'Option-3',
    'Option-4',
    'Correct_Option',
    'Answer',
    'explanation'
]
