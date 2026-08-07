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

        stage('Install') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'pip3 install pytest'
                    } else {
                        bat '''
                        C:\\Python313\\python.exe --version
                        C:\\Python313\\python.exe -m pip --version
                        C:\\Python313\\python.exe -m pip install pytest
                        '''
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 -m pytest -v'
                    } else {
                        bat '''
                        C:\\Python313\\python.exe -m pytest -v
                        '''
                    }
                }
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