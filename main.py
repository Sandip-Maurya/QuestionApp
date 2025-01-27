# main.py
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.middleware.sessions import SessionMiddleware
from Routes.csv_routes import router as csv_router
from utils.csv_utils import generate_csv

from Data.question_data import get_question_data, get_tagging_data
from Processing.process_question_data import process_question_data, process_tagging
from config import IDS_INPUT_MESSAGE, TAGGING_COLUMNS, CONTENT_COLUMNS
import logging

logging.basicConfig(level=logging.INFO)
logging.logger = logging.getLogger(__name__)
logging.log(logging.INFO, "Application started")


app = FastAPI()
app.add_middleware(
    SessionMiddleware,
    secret_key="your-secret-key-hfj5",  # Replace this with a secure random key
    session_cookie="fastapi_session",  # Optional: Customize the session cookie name
    max_age=3600,  # Optional: Session expiration time in seconds (e.g., 1 hour)
)

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(csv_router)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Render the input form template
    return templates.TemplateResponse("index.html", {"request": request, 'placeholder_message': IDS_INPUT_MESSAGE})


@app.post("/view")
async def handle_form(
    request: Request,
    action: str = Form(...),
    exam_id: str = Form(...),
    ids_input: str = Form(...),
):
    try:                

        # Handle different actions
        if action == "view_content":
            # Get question data
            question_data = get_question_data(exam_id, ids_input)
            if question_data is None or question_data.empty:
                return templates.TemplateResponse("index.html", {"request": request, "error": "No data found. Please select correct exam or change IDs."})

            # Process question content
            processed_data = process_question_data(question_data)
            content_data = processed_data.loc[:, CONTENT_COLUMNS].to_dict(orient="index")
            return templates.TemplateResponse("question_display.html", {"request": request, "content_data": content_data})

        elif action == "view_tagging":
            # Get tagging data
            tagging_data = get_tagging_data(exam_id, ids_input)
            if tagging_data is None or tagging_data.empty:
                return templates.TemplateResponse("index.html", {"request": request, "error": "No data found. Please select correct exam or change IDs."})


            # Process tagging data
            processed_data = process_tagging(tagging_data)
            # Call the /generate_csv route to store the CSV temporarily
            request.session["csv_file_path"] = generate_csv( processed_data.loc[:, TAGGING_COLUMNS] )
            tagging_data = processed_data.to_dict(orient="records")
            return templates.TemplateResponse("tagging_display.html", {"request": request, 'tagging_columns': TAGGING_COLUMNS ,"tagging_data": tagging_data})

        else:
            return templates.TemplateResponse("index.html", {"request": request, "error": "Invalid action."})
        
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "error": str(e)})
