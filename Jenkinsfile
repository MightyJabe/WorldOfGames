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
                    // Start the container in detached mode
                    def app = docker.image("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}").run("-d -p 8777:8777")

                    // Wait for the application to start
                    sh 'sleep 15'

                    // Run tests within the container
                    sh "docker exec ${app.id} python3 /usr/local/WorldOfGames/e2e.py"

                    // Stop and remove the container
                    sh "docker stop ${app.id}"
                    sh "docker rm ${app.id}"
                }
            }
        }
        stage('Finalize') {
            steps {
                script {
                    // Using credentials binding
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_HUB_USER', passwordVariable: 'DOCKER_HUB_PASS')]) {
                        // Write the Docker password to a temporary file and use it to login
                        sh """
                            echo $DOCKER_HUB_PASS > docker_password.txt
                            cat docker_password.txt | docker login -u $DOCKER_HUB_USER --password-stdin
                            rm docker_password.txt
                        """
                        // Push the Docker image to DockerHub
                        docker.withRegistry('https://registry.hub.docker.com', '') {
                            docker.image("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}").push()
                        }
                    }
                }
            }
        }
    }
    post {
        failure {
            // Notify about the failure
            echo 'One or more stages failed. Clean up and notify.'
        }
    }
}
