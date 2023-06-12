FROM python:3.9

# Set the working directory to /code
WORKDIR /code

# Copy the requirements.txt file to the /code directory
COPY ./requirements.txt /code/requirements.txt

# Install the Python packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Install the 'bark' library from the GitHub repository
RUN pip install git+https://github.com/suno-ai/bark.git

# Copy the contents of the 'app' directory to the /code/app directory
COPY ./app /code/app

# Set the command to run when the container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
