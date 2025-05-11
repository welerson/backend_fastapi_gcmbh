
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import io
from utils import gerar_relatorio_html

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_planilha(file: UploadFile = File(...)):
    conteudo = await file.read()
    df = pd.read_excel(io.BytesIO(conteudo))
    html = gerar_relatorio_html(df)
    return HTMLResponse(content=html)

@app.get("/")
def home():
    return {"mensagem": "API GCMBH ativa"}
