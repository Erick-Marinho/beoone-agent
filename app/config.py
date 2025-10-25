"""
Sistema de Configuração Centralizado para Beoone Agent

Este módulo implementa um sistema de configuração centralizado usando Pydantic Settings,
organizando configurações por domínio e fornecendo validação automática de tipos.
"""

import os
from abc import ABC
from typing import Literal

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings


class APISettings(BaseSettings):
    """Configurações da API"""
    host: str = Field(default="127.0.0.1", description="Host da API")
    port: int = Field(default=8000, description="Porta da API")
    reload: bool = Field(default=True, description="Auto-reload em desenvolvimento")
    
    class Config:
        env_prefix = "API_"


class LoggingSettings(BaseSettings):
    """Configurações de logging"""
    level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = Field(
        default="INFO", 
        description="Nível de log"
    )
    
    class Config:
        env_prefix = "LOG_"


class Settings(BaseSettings):
    """Configurações principais da aplicação"""
    api: APISettings = Field(default_factory=APISettings)
    logging: LoggingSettings = Field(default_factory=LoggingSettings)
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def get_settings() -> Settings:
    """Factory function para obter instância das configurações"""
    return Settings()


