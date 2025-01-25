import pandas as pd
import tempfile
import uuid
import os

# Temporary directory to store CSVs
temp_dir = tempfile.TemporaryDirectory()

def generate_csv(processed_data: pd.DataFrame) -> str:
    """
    Generate a CSV file and store it in a temporary directory.
    Returns the file path.
    """
    file_id = str(uuid.uuid4())
    file_path = os.path.join(temp_dir.name, f"{file_id}.csv")

    # Save processed data as a CSV
    processed_data.to_csv(file_path, index=False)
    return file_path
