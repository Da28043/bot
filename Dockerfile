# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install the required dependencies directly
RUN pip install --no-cache-dir pyrogram==2.0.106 tgcrypto

# Copy the bot's source code into the container
COPY . /app

# Expose port (if necessary for external access)
# EXPOSE 8080

# Define the command to run the bot
CMD ["python", "bot.py"]
