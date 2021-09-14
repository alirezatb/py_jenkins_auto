pipeline {
    agent docker
    options {
        ansiColor('xterm')
        skipDefaultCheckout()
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }
    environment {
        PRODUCT = 'py_jenkins_auto'
        GIT_HOST = 'github.com'
        GIT_REPO = 'repo'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    BRANCH_NAME = env.CHANGE_BRANCH ? env.CHANGE_BRANCH : env.BRANCH_NAME
                    deleteDir()
                    git url: "git@<host>:<org>/${env.PRODUCT}.git", branch: BRANCH_NAME
                }
            }
        }
//         stage('Installing packages') {
//             steps {
//                 script {
//                     sh 'pip install -r requirements.txt'
//                 }
//             }
//         }
//     stage('Running Unit tests') {
//             steps {
//                 sh 'python tests/*.py'
//                 }
//             post {
//                 always {
//                     junit 'test-reports/*.xml'
//                 }
//             }
//         }
//     stage ('Merge PR'){
//         when {
//             branch 'PR-*'
//         }
//         steps {
//             sh 'git remote set-url origin git@github.com:alirezatb/py_jenkins_auto.git'
//             sh 'git remote set-branches --add origin ${CHANGE_TARGET}'
//             sh 'git fetch origin'
//             sh 'git checkout ${CHANGE_TARGET}'
//             sh 'git merge --no-ff ${GIT_COMMIT}'
//             sh 'git push origin ${CHANGE_TARGET}'
//         }
//       }
    }
}