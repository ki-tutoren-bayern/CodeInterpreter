FROM python:3.11.7-bookworm

WORKDIR /usr/src/app

copy . . 
RUN pip install --no-cache-dir -r requirements.txt
env OPENAI_API_KEY=
EXPOSE 5000
CMD ["python", "app.py"]