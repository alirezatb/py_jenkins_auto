pipeline {
    agent any
    stage('Checkout') { // Checkout (git clone ...) the projects repository
      steps {
        checkout scm
      }

    stage('Installing packages') {
            steps {
                script {
                    sh 'pip -r requirements.txt'
                }
            }
        }

    stage('Linting') { // Run pylint against your code
      steps {
        script {
          sh """
          pylint **/*.py
          """
        }
      }
    }
    stage('Running Unit tests') {
            steps {
                script {
                    sh 'python3.7 manage.py test --keepdb --with-xunit --xunit-file=pyunit.xml --cover-xml --cover-xml-file=cov.xml tests/*.py || true'
                    step([$class: 'CoberturaPublisher',
                        coberturaReportFile: "cov.xml",
                    ])
                    junit "pyunit.xml"
                }
            }

}