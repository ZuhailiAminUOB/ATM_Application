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
        powershell 'echo \'Running calculator script...\''
        bat '\'python -m unittest discover\''
      }
    }

  }
}