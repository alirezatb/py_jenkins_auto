pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python -m py_compile main.py python_pass_check.py test_python_pass_check.py'
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
    }
}