FROM python:3

WORKDIR /app
ADD app.py requirements.txt /app/
RUN pip install -r requirements.txt
EXPOSE 9090

CMD ["python", "app.py"]
