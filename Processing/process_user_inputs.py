# ./Processing/process.py
import re

def clean_ids_input(question_ids_input):
    question_ids_input = question_ids_input.replace(" ", "")
    question_ids = re.split(r"[,\t\n]+", question_ids_input)
    question_ids = [question_id.strip() for question_id in question_ids if question_id.strip()]
    return question_ids