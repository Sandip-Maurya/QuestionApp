# main.py
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from Data.question_data import get_question_data
from Processing.process_question_data import process_question_data
from config import IDS_INPUT_MESSAGE, TAGGING_COLUMNS, CONTENT_COLUMNS
import logging

logging.basicConfig(level=logging.INFO)
logging.logger = logging.getLogger(__name__)
logging.log(logging.INFO, "Application started")


app = FastAPI()

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Render the input form template
    return templates.TemplateResponse("index.html", {"request": request, 'placeholder_message': IDS_INPUT_MESSAGE})


@app.post("/")
async def handle_form(
    request: Request,
    action: str = Form(...),
    exam_id: str = Form(...),
    ids_input: str = Form(...),
):
    try:        
        # Get question data
        question_data = get_question_data(exam_id, ids_input)
        if question_data is None or question_data.empty:
            return templates.TemplateResponse("index.html", {"request": request, "error": "No data found."})

        # Handle different actions
        if action == "view_content":
            # Process question content
            processed_data = process_question_data(question_data)
            content_data = processed_data.loc[:, CONTENT_COLUMNS].to_dict(orient="index")
            return templates.TemplateResponse("question_display.html", {"request": request, "content_data": content_data})

        elif action == "view_tagging":
            # Process tagging data
            processed_data = process_question_data(question_data)
            tagging_data = processed_data[TAGGING_COLUMNS].to_dict(orient="records")
            return templates.TemplateResponse("tagging_display.html", {"request": request, 'tagging_columns': TAGGING_COLUMNS ,"tagging_data": tagging_data})

        else:
            return templates.TemplateResponse("index.html", {"request": request, "error": "Invalid action."})
        
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "error": str(e)})
