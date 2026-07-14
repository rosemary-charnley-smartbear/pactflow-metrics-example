FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

COPY app.py .
COPY templates/ templates/

ENV DATA_DIR=/data

EXPOSE 5000

CMD ["python", "app.py"]
