#use the official python image as the base image
FROM python:3.9-slim-buster

#set the working directory in the container
WORKDIR /app

#install the necessary packages for psutil
RUN apt-get update && \
    apt-get install -y gcc python3-dev

#upgrade pip
RUN python -m pip install --upgrade pip

#copy the requirements file to the working directory
COPY requirements.txt .

#install the required python packages
RUN pip install --no-cache-dir -r requirements.txt

#copy the application code to the working directory
COPY . .

#set the environment variables for the flask app
ENV FLASK_RUN_HOST=0.0.0.0

#expose the port on which the flask app will run
EXPOSE 5000

#start the flask app when the container is run
CMD ["flask", "run"]
