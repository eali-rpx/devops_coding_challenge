FROM public.ecr.aws/lambda/python:3.11

WORKDIR /app

COPY requirements.txt requirements.txt
COPY *.py .
RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install --platform manylinux2014_x86_64 --target . --python-version 3.12 --only-binary=:all: numpy


COPY . .

CMD ["lambda_function.handler_function"]
