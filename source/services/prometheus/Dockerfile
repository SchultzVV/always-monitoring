FROM python:3.10-slim

WORKDIR /app

COPY . .

ARG REQUIREMENTS=requirements-dev.txt

RUN pip install --no-cache-dir -r $REQUIREMENTS

EXPOSE 5000

CMD ["python", "main.py"]
