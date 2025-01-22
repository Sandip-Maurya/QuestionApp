import json

def process_option(option, option_no):
    if option:
        option = json.loads(option)
        return option[option_no]
    return None
def process_correct_option(correct_option):
    correct_option = json.loads(correct_option)
    if isinstance(correct_option, dict):
        return list(correct_option.keys())[0]
    return None

def process_answer(answer):
    answer = json.loads(answer)
    if isinstance(answer, dict):
        return list(answer.values())[0]
    return answer[0]