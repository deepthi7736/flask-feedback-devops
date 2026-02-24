pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/deepthi7736/flask-feedback-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-feedback-devops .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop flask-feedback-devops || true
                docker rm flask-feedback-devops || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                docker run -d -p 5000:5000 --name flask-feedback-devops flask-feedback-devops
                '''
            }
        }
    }
}
