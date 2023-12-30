pipeline {
    agent any

    environment {
        // Define environment variables
        DOCKER_IMAGE_NAME = 'thicksy/worldofgames'
        DOCKER_IMAGE_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                // Check out the source code from the SCM (Source Code Management)
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    docker.build("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}", '.')
                }
            }
        }

        stage('Run & Test') {
            steps {
                script {
                    // Start the Docker container in detached mode and run tests
                    def app = docker.image("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}").run("-d -p 8777:8777")
                    sh 'sleep 15' // Wait for the application to start
                    sh "docker exec ${app.id} python3 /usr/local/WorldOfGames/e2e.py" // Execute tests

                    // Stop and remove the Docker container
                    sh "docker stop ${app.id}"
                    sh "docker rm ${app.id}"
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    // Use credentials binding for Docker Hub login
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_HUB_USER', passwordVariable: 'DOCKER_HUB_PASS')]) {
                        // Login to Docker Hub
                        sh 'echo "$DOCKER_HUB_PASS" | docker login -u "$DOCKER_HUB_USER" --password-stdin'

                        // Tag and push the Docker image to Docker Hub
                        sh 'docker tag ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}'
                        sh 'docker push ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}'
                    }
                }
            }
        }
    }

    post {
        failure {
            // Notify or perform actions in case of failure
            echo 'One or more stages failed. Clean up and notify.'
        }
    }
}
