# Basics
FROM python:3.10
WORKDIR /app

# Create user and update
RUN adduser --disabled-password --no-create-home user
RUN apt-get update;
# RUN apt-get upgrade -y;

# Install the libs
COPY --chown=user requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the files
COPY --chown=user ./src /app/src

# Run the program
USER user
CMD python3 -u src/index.py