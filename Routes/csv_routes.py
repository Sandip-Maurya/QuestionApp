from fastapi import APIRouter, Request
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/download_csv")
async def download_csv(request: Request):
    """
    Serve the CSV file for download.
    """
    file_path = request.session.get("csv_file_path")
    if not file_path or not os.path.exists(file_path):
        return {"error": "File not generated. Please try again or contact Sandip."}

    return FileResponse(file_path, media_type="text/csv", filename="tagging_data.csv")
