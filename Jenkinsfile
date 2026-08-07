pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                bat '''
                C:\\Python313\\python.exe --version
                C:\\Python313\\python.exe -m pytest --version
                C:\\Python313\\python.exe -m pytest -v
                '''
            }
        }
    }

    post {
        success {
            echo '테스트 완료: 모든 테스트를 통과했습니다.'
        }

        failure {
            echo '테스트 실패'
        }
    }
}