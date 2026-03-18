from fastapi import FastAPI
from app.database import Base, engine

# IMPORTAR TODOS OS MODELS (IMPORTANTE)
from app.models import empresa, user, cliente, plano, assinatura

app = FastAPI(title="SaaS API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API SaaS rodando 🚀"}