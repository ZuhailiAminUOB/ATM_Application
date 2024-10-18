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
        bat 'python3 -m unittest discover'
      }
    }

  }
}