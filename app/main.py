from fastapi import FastAPI
from app.core.scheduler import iniciar_scheduler
from app.database import Base, engine

# IMPORTAR TODOS OS MODELS (IMPORTANTE)
from app.models import empresa, user, cliente, plano, assinatura
from app.routes import assinaturas, auth, clientes, planos, teste
app = FastAPI(title="SaaS API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API SaaS rodando 🚀"}

app.include_router(auth.router)
app.include_router(clientes.router)
app.include_router(planos.router)
app.include_router(assinaturas.router)
iniciar_scheduler()

app.include_router(teste.router)