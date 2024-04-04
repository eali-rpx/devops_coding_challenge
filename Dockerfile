FROM public.ecr.aws/docker/library/python:3.12-slim

WORKDIR /app
COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt
COPY *.py ./
CMD ["app.handler"]