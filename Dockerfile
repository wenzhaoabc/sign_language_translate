FROM python:3.10
COPY . /workspace

WORKDIR /workspace

EXPOSE 5000

RUN pip install -r requirements.txt && python ./api/routes.py



