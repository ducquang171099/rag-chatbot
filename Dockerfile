FROM python:3.12.9-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y build-essential curl \
    && pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your code from src/ into the container
COPY src/ ./src/

WORKDIR /app/src

EXPOSE 8501

CMD bash -c "streamlit run app.py"
