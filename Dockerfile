FROM python:3.13.4-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 3000
CMD [ "fastapi", "run", "./src/main.py", "--port", "3000" ]