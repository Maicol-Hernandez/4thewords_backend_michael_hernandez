import os
import uuid
from fastapi import UploadFile, HTTPException

async def save_uploaded_image(file: UploadFile):
    # Generates a unique name for the file
    unique_filename = f"{uuid.uuid4()}{os.path.splitext(file.filename)[1]}"
    
    # Absolute path of the directory (better practice for production)
    static_dir = os.path.abspath("app/static")
    os.makedirs(static_dir, exist_ok=True)
    
    # Full path of the file
    file_path = os.path.join(static_dir, unique_filename)
    
    try:
        # Saves the file
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
            
        return f"/static/{unique_filename}"  # Example: "/static/550e8400-e29b-41d4-a716-446655440000.jpg"
    
    except Exception as e:
        # Error handling
        raise HTTPException(
            status_code=500, 
            detail=f"Error al guardar la imagen: {str(e)}"
        )