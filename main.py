"""
Ponto de entrada da aplicação

Este arquivo serve como ponto de entrada principal para executar a aplicação fastapi.
Ele importa a instância do aplicativo fastapi e inicia o servidor uvicorn para executar a aplicação.
"""

import uvicorn
from app.config import get_settings

if __name__ == "__main__":
    # Obter configurações
    config = get_settings()

    # Executar servidor usando configurações
    uvicorn.run(
        "app.application.main:app",
        host=config.api.host,
        port=config.api.port,
        reload=config.api.reload,
        log_level=config.logging.level.lower(),
    )

