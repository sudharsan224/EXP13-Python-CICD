pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking Source Code'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('app') {
                    sh '''
                        python3 -m venv venv
                        venv/bin/pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Python Tests') {
            steps {
                dir('app') {
                    sh '''
                        venv/bin/python -m pytest -v
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t exp13-python:latest .'
            }
        }

        stage('Deploy Locally') {
            steps {
                sh '''
                    docker rm -f exp13-container || true

                    docker run -d \
                    --name exp13-container \
                    -p 5000:5000 \
                    exp13-python:latest
                '''
            }
        }

        stage('Verify Deployment') {
    steps {
        sh '''
            sleep 5
            curl --fail http://host.docker.internal:5000/health
        '''
    }
}

    post {
        success {
            echo 'CI/CD Pipeline Completed Successfully!'
        }

        failure {
            echo 'CI/CD Pipeline Failed!'
        }
    }
}