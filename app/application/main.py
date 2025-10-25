"""
Aplicação FastAPI principal

Configura e inicializa a aplicação FastAPI com todos os
middlewares, routers e configurações necessárias.
"""

from fastapi import FastAPI

from app.config import get_settings

# Obter configurações
settings = get_settings()

# Criar instância do FastAPI
app = FastAPI(
    title="Beoone Agent API",
    description="API para o sistema Beoone Agent",
    version="1.0.0",
)


@app.get("/")
async def root():
    """Endpoint de health check"""
    return {"message": "Beoone Agent API está funcionando!", "status": "ok"}


@app.get("/health")
async def health_check():
    """Endpoint de verificação de saúde da aplicação"""
    return {"status": "healthy", "service": "beoone-agent", "version": "1.0.0"}
