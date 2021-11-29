FROM python:3.9

COPY . ./code

WORKDIR /code

RUN pip install --no-cache-dir --upgrade -r /code/docker_requirements.txt

CMD ["pytest"]
