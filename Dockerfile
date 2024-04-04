FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt requirements.txt
COPY data/ .
COPY *.py . 
RUN python3 -m pip install -r requirements.txt
CMD ["app.handler"]
