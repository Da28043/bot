# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables to avoid pyc files and enable immediate log flushing
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Install the required dependencies directly
RUN pip install --no-cache-dir pyrogram==2.0.106 tgcrypto

# Verify pyrogram installation (optional, but helpful for debugging)
RUN pip show pyrogram

# Copy the bot's source code into the container
COPY . /app

# Define the command to run the bot (update this to match your file name, e.g., 'main.py' or 'bot.py')
CMD ["python", "bot.py"]