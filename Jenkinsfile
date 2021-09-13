pipeline {
    agent any
    stages {
    stage('Running Unit tests') {
            steps {
                sh 'python tests/*.py'
                }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
            }
        }
    stage ('Merge PR'){
        when {
            branch 'PR-*'
        }
        steps {
            sh 'git remote set-url origin git@github.com:alirezatb/py_jenkins_auto.git'
            sh 'git remote set-branches --add origin ${CHANGE_TARGET}'
            sh 'git fetch origin'
            sh 'git checkout ${CHANGE_TARGET}'
            sh 'git merge --no-ff ${GIT_COMMIT}'
            sh 'git push origin ${CHANGE_TARGET}'
        }
      }
    }
}