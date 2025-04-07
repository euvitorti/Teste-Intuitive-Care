from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.src.rotas.operadora_controller import router as operadoras_router

app = FastAPI()

# Configuração do CORS
origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rotas
app.include_router(operadoras_router)
