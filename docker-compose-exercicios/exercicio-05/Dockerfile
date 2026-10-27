FROM python:3.12-slim

WORKDIR /app

# Instalar dependências
RUN pip install flask pymysql --no-cache-dir

# Copiar código
COPY app.py .
COPY requirements.txt .

# Criar diretório para dados
RUN mkdir -p /app/data

# Expor porta
EXPOSE 5000

# Comando padrão
CMD ["python", "app.py"]
