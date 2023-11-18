FROM python:3.7.8

# Copy the dependencies file to the working directory
COPY ./requirements.txt .

RUN pip install --upgrade pip

# Install any dependencies
RUN pipdddd install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# By default, container listen on port 8081
EXPOSE 8090

# Specify the command to run on container start
CMD [ "uvicorn", "app:app", "--port", "8090", "--host", "0.0.0.0" ]
