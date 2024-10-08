from typing import Annotated
from fastapi import FastAPI, File, UploadFile, Form
import uvicorn
from PyPDF2 import PdfReader
import io
from PDF_Text import get_text_from_pdf 
from Response import get_response

app = FastAPI()


@app.post("/upload-pdf/")
async def read_pdf( file: UploadFile = File(...)):
    try:
        # Read the PDF file content as bytes
        contents = await file.read()
        pdf_file = io.BytesIO(contents)

        clean_text = get_text_from_pdf(pdf_file)

        System = "You are the expert system of the world. You know everything."
        start = "Generate the MCQ for the given Text below\n"

        prompted = start + clean_text

        answer = get_response(System , prompted)
        required_text = answer.replace('*', '')

        print(required_text)
        return {"MCQs": required_text}

    except Exception as e:
        return {"Error Internet Connection": e}

if __name__ == '__main__':

    uvicorn.run(app, host = 'localhost', port = 8000)





