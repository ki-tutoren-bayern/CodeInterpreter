FROM python:3.11

WORKDIR /usr/src/app

copy . . 
RUN pip install --no-cache-dir -r requirements.txt
env OPENAI_API_KEY=
EXPOSE 5000
CMD ["python3", "app.py"]