pipeline {
    agent { label "${AGENT_LABEL}"}

    environment {
        IMAGE_NAME = "netapp1"
        IMAGE_TAG  = "${BUILD_NUMBER}"
        DOCKER_IMAGE = "${IMAGE_NAME}:${IMAGE_TAG}"
    }

    stages {

        stage('CODE') {
            steps {
                git url:https://github.com/vishwash-debug/jenkins-project.git, branch:"main"
            }
        }

        stage('Build') {
            steps {
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }

        stage('Deploy') {
            steps {
                    sh """
                      docker stop net1 || true
                      docker rm net1 || true
                      docker run -d --name net1 -p 80:80 --restart always ${DOCKER_IMAGE}
                    """
                }
        }
    }
