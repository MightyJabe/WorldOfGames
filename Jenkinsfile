pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'thicksy/worldofgames'
        DOCKER_IMAGE_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}", '.')
                }
            }
        }

        stage('Run & Test') {
            steps {
                script {
                    // Run the Docker container in detached mode and capture the container ID
                    CONTAINER_ID = sh(script: "docker run -d -p 8777:8777 ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}", returnStdout: true).trim()
                    sh 'sleep 15'  // Example: Wait for the application to start

                    // Run your Selenium tests
                    try {
                        sh 'python3 e2e.py'
                    } finally {
                        // Stop and remove the Docker container
                        sh "docker stop ${CONTAINER_ID}"
                        sh "docker rm ${CONTAINER_ID}"
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    // Push the Docker image to DockerHub
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}").push()
                    }
                }
            }
        }
    }

    post {
        failure {
            echo 'One or more stages failed. Clean up and notify.'
            // Add any additional steps or notifications on failure
        }
    }
}
