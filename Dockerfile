FROM python:3.12-slim

WORKDIR /app

# Instalar dependências do sistema necessárias para o MySQL
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Manter o container aberto para execução interativa
CMD ["bash"]
