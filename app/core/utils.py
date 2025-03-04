import os
from fastapi import UploadFile

async def save_uploaded_image(file: UploadFile):
    static_dir = "app/static"
    os.makedirs(static_dir, exist_ok=True)
    file_path = os.path.join(static_dir, file.filename)
    
    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    
    return f"/static/{file.filename}"