pipeline {
    agent {
        docker { image 'python:3' }
    }

    stages {

        stage('Checkout') {
          steps {
            echo "Checkout Git.."
            deleteDir()
            checkout scm
           }
        }

        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                python3 app.py
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}