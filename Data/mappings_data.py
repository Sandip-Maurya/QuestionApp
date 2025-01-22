import pandas as pd
from Data.queries import get_chapter_query, get_topic_query
from Data.collections import chapter_collection, topic_collection

EXAM_MAP = {
    "1": 'JEE Main',
    "2": 'NEET'
}

SUBJECT_MAP = {
    "1": "Mathematics",
    "2": "Physics",
    "3": "Chemistry",
    "4": "Botany",
    "5": "Biology",
    "146": "Zoology",
}
TEMPLATE_MAP = {
    1: "Multi Choice Question",
    2: "Single Choice Question",
    11: "Numerical Question",
    13: "Intger Question",
}

CATEGORY_MAP = {
    1: "Practice Question",
    2: "Previous Year Question",
}

chapter_query = get_chapter_query()
chapter_df = pd.DataFrame(list(chapter_collection.aggregate(chapter_query)))
CHAPTER_MAP = chapter_df.set_index('_id')['chapterName'].to_dict()

topic_query = get_topic_query()
topic_df = pd.DataFrame(list(topic_collection.aggregate(topic_query)))
TOPIC_MAP = topic_df.set_index('_id')['topicName'].to_dict()