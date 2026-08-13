from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI(title="CSV API Sender")


@app.get("/")
def home():
    return {"message": "API de upload de CSV funcionando"}


@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Envie um arquivo CSV válido.")

    try:
        contents = await file.read()
        df = pd.read_csv(pd.io.common.BytesIO(contents))
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Arquivo CSV inválido: {exc}") from exc

    if df.empty:
        raise HTTPException(status_code=400, detail="O arquivo CSV está vazio.")

    return {
        "filename": file.filename,
        "rows_count": int(len(df)),
        "columns": df.columns.tolist(),
        "preview": df.head(5).to_dict(orient="records"),
    }


@app.exception_handler(HTTPException)
async def http_exception_handler(_, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
