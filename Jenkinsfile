pipeline {
  agent any
  stages {
    stage('checkout') {
      steps {
        deleteDir()
        git(url: 'https://github.com/amanda-chan/ATM_Application.git', branch: 'main')
      }
    }

    stage('test') {
      steps {
        bat 'echo \'Running unit tests...\''
        bat 'bat \'python -m unittest discover\''
      }
    }

  }
}