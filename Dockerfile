# Use an appropriate base image with Linux support
FROM ubuntu:latest

# Set the working directory
WORKDIR /usr/local/WorldOfGames

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Copy the program folders into the container
COPY . /usr/local/WorldOfGames


#Install Docker inside the container
RUN curl -fsSL https://get.docker.com | sh


# Grant execution permissions to the entrypoint script
RUN chmod +x /usr/local/WorldOfGames/entrypoint.sh
# Install project dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Set the default command to run the entrypoint script
CMD ["sh", "-c", "./entrypoint.sh"]
