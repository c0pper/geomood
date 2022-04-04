# start by pulling the python image
FROM python:3.8-slim-buster
RUN apt-get update -y && apt-get install -y gcc

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

CMD ["flask", "run", "--host", "0.0.0.0"]