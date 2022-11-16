FROM python:3.8.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt && pip cache purge  

CMD python run.py
