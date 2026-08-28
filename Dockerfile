FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

COPY main.py train_model.py /code/
RUN python train_model.py

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
