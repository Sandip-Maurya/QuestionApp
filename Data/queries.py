# ./Data/queries.py


def get_question_query(question_ids):
    question_query = [
        {
            "$match": {
                "_id": {
                    "$in": question_ids
                }
            }
        },
        {
            "$addFields": {
                "sortOrder": {
                    "$indexOfArray": [question_ids, "$_id"]
                }
            }
        },
        {
            "$sort": {
                "sortOrder": 1
            }
        },
        {
            "$project": {
                "_id": 1,
                "classId": 1,
                "subjectId": 1,
                "unitId": 1,
                "chapterId": 1,
                "topicId": 1,
                "majorConceptId": 1,
                "templateType": 1,
                "Q_DIFFICULTY": {"$toString": "$difficultyLevel"},
                "question": 1,
                "questionOptions": 1,
                "answers": 1,
                "explanation": 1,
                "quesStatus": 1,
                "questionCategory": 1,
                "inSyllabus": 1,
            }
        },
    ]
    return question_query

def get_tagging_query(question_ids):
    tagging_query = [
        {
            "$match": {
                "_id": {
                    "$in": question_ids
                }
            }
        },
        {
            "$addFields": {
                "sortOrder": {
                    "$indexOfArray": [question_ids, "$_id"]
                }
            }
        },
        {
            "$sort": {
                "sortOrder": 1
            }
        },
        {
            "$project": {
                "_id": 1,
                "classId": 1,
                "subjectId": 1,
                "unitId": 1,
                "chapterId": 1,
                "topicId": 1,
                "majorConceptId": 1,
                "templateType": 1,
                "Q_DIFFICULTY": {"$toString": "$difficultyLevel"},
                "quesStatus": 1,
                "questionCategory": 1,
                "inSyllabus": 1,
            }
        },
    ]
    return tagging_query

def get_chapter_query():
    chapter_query = [
        {"$match": {"classExamId": {"$in": ["1", "2"]}, "status": "1"}},
        {"$project": {"chapterName": 1}},
    ]
    return chapter_query


def get_topic_query():
    topic_query = [
        {"$match": {"classId": {"$in": ["1", "2"]}, "status": "1"}},
        {"$project": {"topicName": 1}},
    ]
    return topic_query
