FROM python:3

# Install required packages
RUN pip install requests

# Copy the action script
COPY get_joke.py /get_joke.py

# Set the entrypoint
ENTRYPOINT ["python", "/get_joke.py"]
