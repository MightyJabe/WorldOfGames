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
                    docker.image("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}").withRun { c ->
                        // Run additional commands if needed before tests
                        sh 'sleep 1'  // Example: Wait for the application to start

                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}").inside('-p 8777:8777') {
                        // Run your Selenium tests
                        sh 'sleep 15'  // Example: Wait for the application to start
                        sh 'python3 e2e.py'
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    // Stop and remove the running container
                    docker.image("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}").inside {
                        sh 'pkill -f "python3 /usr/local/WorldOfGames/flask_app.py"'
                    }

                    // Push the Docker image to DockerHub
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials-id') {
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
