# Usar uma imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos da aplicação para o contêiner
COPY . /app

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta que a aplicação vai usar
EXPOSE 8080

# Comando para iniciar a aplicação
CMD ["python", "todo_project/run.py"]
