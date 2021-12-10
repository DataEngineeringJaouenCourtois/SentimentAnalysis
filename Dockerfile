FROM python:3.6

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

 
COPY ./docker_app /code/app

EXPOSE 8000

CMD ["uvicorn", "app.web_app.myapp:app", "--host=0.0.0.0", "--reload"]
