
pipeline {
    agent any

    environment {
        DOCKER_IMAGE       = 'ajaydhadi95/voting-app'
        DOCKER_CREDENTIALS = 'dockerhub-credentials'

        GITOPS_URL         = 'https://github.com/ajaydhadi95-gif/voting-app-gitops.git'
        GITOPS_BRANCH      = 'main'
        GITOPS_CREDENTIALS = 'github-gitops-credentials'

        GITOPS_DIR         = 'gitops'
    }

    options {
        timestamps()
        disableConcurrentBuilds()
        timeout(time: 30, unit: 'MINUTES')
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
                    pip install --upgrade pip
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
                dir("${GITOPS_DIR}") {
                    deleteDir()

                    withCredentials([
                        usernamePassword(
                            credentialsId: GITOPS_CREDENTIALS,
                            usernameVariable: 'GIT_USER',
                            passwordVariable: 'GIT_TOKEN'
                        )
                    ]) {
                        sh '''
                            set -eu

                            git clone \
                              --branch "$GITOPS_BRANCH" \
                              "https://$GIT_USER:$GIT_TOKEN@github.com/ajaydhadi95-gif/voting-app-gitops.git" \
                              .

                            test -f voting-app-gitops/kubernetes/deployment.yaml

                            python3 - <<'PY'
                            import os
                            import re
                            from pathlib import Path

                            path = Path("voting-app-gitops/kubernetes/deployment.yaml")
                            content = path.read_text()

                            image = os.environ["DOCKER_IMAGE"]
                            tag = os.environ["BUILD_NUMBER"]

                            pattern = r'(?m)^(\\s*image:\\s*)' + re.escape(image) + r'(?::[^\\s]+)?\\s*$'

                            updated, count = re.subn(
                                pattern,
                                lambda match: match.group(1) + image + ":" + tag,
                                content
                            )

                            if count != 1:
                                raise SystemExit(
                                    f"Expected exactly one voting-app image entry, found {count}"
                                )

                            path.write_text(updated)
                            PY

                            git config user.name "Jenkins"
                            git config user.email "jenkins@example.com"

                            git add voting-app-gitops/kubernetes/deployment.yaml

                            if git diff --cached --quiet; then
                                echo "No GitOps changes to commit."
                            else
                                git commit -m "Deploy voting-app build $BUILD_NUMBER"
                                git push origin "$GITOPS_BRANCH"
                            fi
                        '''
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Docker image pushed and GitOps repository updated.'
            echo 'Argo CD can now sync the Kubernetes deployment.'
        }

        failure {
            echo 'FAILED: Check Jenkins console output for the failed stage.'
        }

        always {
            echo 'Voting App CI/CD pipeline finished.'
        }
    }
}
