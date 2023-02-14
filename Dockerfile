FROM registry.access.redhat.com/ubi9/python-39:latest

# By default, container listen on port 8081
EXPOSE 8081
# Copy the dependencies file to the working directory
COPY ./requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD [ "uvicorn", "app:app", "--port", "8081", "--host", "0.0.0.0" ]