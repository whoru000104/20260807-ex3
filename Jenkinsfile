pipeline {
    agent any

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
                        sh 'pip3 install --quiet pytest'
                    } else {
                        bat 'pip install --quiet pytest'
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
                        bat 'python -m pytest -v'
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
