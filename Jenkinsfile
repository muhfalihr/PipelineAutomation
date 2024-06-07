pipeline {
    agent any
    stages {
        stage('Python Version') {
            steps {
                script {
                    sh "python3 --version"
                }
            }
        }
        stage('Start Program') {
            steps {
                script {
                    sh "python3 while.py"
                }
            }
        }
    }
}