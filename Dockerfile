FROM public.ecr.aws/lambda/python:3.11

WORKDIR /app

COPY requirements.txt requirements.txt
COPY *.py .
RUN python3 -m pip install -r requirements.txt

COPY . .

CMD ["lambda_function.handler_function"]
