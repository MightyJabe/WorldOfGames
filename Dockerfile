# Use an appropriate base image with Linux support
FROM ubuntu:latest

# Set the working directory
WORKDIR /usr/local/WorldOfGames

# Install Python, pip, wget, xvfb, and unzip (needed for Chrome and ChromeDriver setup)
RUN apt-get update && \
    apt-get install -y python3 python3-pip wget xvfb unzip

# Set up the Chrome PPA
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

# Update the package list and install chrome
RUN apt-get update -y && \
    apt-get install -y google-chrome-stable

# Set up Chromedriver Environment variables
ENV CHROMEDRIVER_VERSION 2.19
ENV CHROMEDRIVER_DIR /chromedriver
RUN mkdir $CHROMEDRIVER_DIR

# Download and install Chromedriver
RUN wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip" && \
    unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR

# Put Chromedriver into the PATH
ENV PATH $CHROMEDRIVER_DIR:$PATH

# Copy the program folders into the container
COPY . /usr/local/WorldOfGames

# Grant execution permissions to the entrypoint script
RUN chmod +x /usr/local/WorldOfGames/entrypoint.sh

# Install project dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Set the default command to run the entrypoint script
CMD ["sh", "-c", "./entrypoint.sh"]
