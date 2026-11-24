
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "ajaydhadi95/voting-app"
        DOCKER_CREDENTIALS = "dockerhub-credentials"
        GITOPS_URL = "https://github.com/ajaydhadi95-gif/voting-app-gitops.git"
        GITOPS_BRANCH = "main"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m py_compile app.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${BUILD_NUMBER}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry(
                        'https://index.docker.io/v1/',
                        DOCKER_CREDENTIALS
                    ) {
                        docker.image(
                            "${DOCKER_IMAGE}:${BUILD_NUMBER}"
                        ).push()
                    }
                }
            }
        }

        stage('Update GitOps Repository') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'github-gitops-credentials',
                        usernameVariable: 'GIT_USER',
                        passwordVariable: 'GIT_TOKEN'
                    )
                ]) {
                    sh '''
                        rm -rf gitops
                        git clone -b ${GITOPS_BRANCH} \
                        https://${GIT_USER}:${GIT_TOKEN}@github.com/ajaydhadi95-gif/voting-app-gitops.git gitops

                        cd gitops

                        sed -i "s|image: .*|image: ${DOCKER_IMAGE}:${BUILD_NUMBER}|" kubernetes/deployment.yaml

                        git config user.name "Jenkins"
                        git config user.email "jenkins@example.com"

                        git add kubernetes/deployment.yaml
                        git commit -m "Update voting-app image to ${BUILD_NUMBER}" || true
                        git push origin ${GITOPS_BRANCH}
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'CI successful. GitOps repository updated.'
        }

        failure {
            echo 'CI pipeline failed. Check Jenkins logs.'
        }
    }
}
