from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

from pathlib import Path
import shutil
import uuid


from services.document_processor import DocumentProcessor


router = APIRouter(
    tags=["TIA"]
)


UPLOAD_DIR = Path("uploaded_reports")

UPLOAD_DIR.mkdir(
    exist_ok=True
)


document_processor = DocumentProcessor()



@router.get("/")
def home():

    return {
        "message": "TIA Backend is running 🚀"
    }



@router.post("/analyze-report")
async def analyze_report(
        file: UploadFile = File(...)
):

    try:

        # ----------------------------
        # Validate extension
        # ----------------------------

        allowed_extensions = [
            ".pdf",
            ".png",
            ".jpg",
            ".jpeg"
        ]


        extension = Path(
            file.filename
        ).suffix.lower()


        if extension not in allowed_extensions:

            raise HTTPException(
                status_code=400,
                detail="Unsupported file format"
            )


        # ----------------------------
        # Save uploaded file
        # ----------------------------

        file_id = str(uuid.uuid4())


        saved_file = (
            UPLOAD_DIR /
            f"{file_id}{extension}"
        )


        with open(saved_file, "wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )


        print(
            f"Saved report: {saved_file}"
        )


        # ----------------------------
        # Process report
        # ----------------------------

        result = document_processor.process(
            str(saved_file)
        )


        # ----------------------------
        # Return response
        # ----------------------------

        return JSONResponse(
            content={
                "status": "success",
                "report": result
            }
        )


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )