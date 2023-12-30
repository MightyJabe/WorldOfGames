# Use an appropriate base image with Linux support
FROM ubuntu:latest

# Set the working directory
WORKDIR /usr/local/WorldOfGames

# Update package list and install Python, pip, wget, gnupg2, and unzip
# Install Chrome and ChromeDriver
RUN apt-get update && \
    apt-get install -y python3 python3-pip wget gnupg2 unzip && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | tee -a /etc/apt/sources.list.d/google.list && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    BROWSER_MAJOR=$(google-chrome --version | sed 's/Google Chrome \([0-9]*\).*/\1/g') && \
    wget https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${BROWSER_MAJOR} -O chromedriver_version && \
    wget https://chromedriver.storage.googleapis.com/`cat chromedriver_version`/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/ && \
    DRIVER_MAJOR=$(chromedriver --version | sed 's/ChromeDriver \([0-9]*\).*/\1/g') && \
    if [ $BROWSER_MAJOR != $DRIVER_MAJOR ]; then echo "VERSION MISMATCH"; exit 1; fi && \
    rm -rf /var/lib/apt/lists/*


# Copy the program folders into the container
COPY . /usr/local/WorldOfGames

# Grant execution permissions to the entrypoint script
RUN chmod +x /usr/local/WorldOfGames/entrypoint.sh

# Install project dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Set the default command to run the entrypoint script
CMD ["sh", "-c", "./entrypoint.sh"]
