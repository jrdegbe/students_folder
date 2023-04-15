# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make ports 8000 and 8501 available to the world outside this container
EXPOSE 8000
EXPOSE 8501

# Define environment variable
ENV NAME World

# Run app_fastapi.py and app_streamlit.py when the container launches
CMD ["sh", "-c", "uvicorn app_fastapi:app --host 0.0.0.0 --port 8000 & streamlit run app_streamlit.py"]

