pipeline {
    agent any

    tools {
        ansible 'ansible'   // configure this in Jenkins global tools
    }

    stages {

        stage('Clone Code') {
            steps {
                git url: 'https://github.com/vishwash-debug/jenkins-project.git', branch: 'main'
            }
        }

        stage('Deploy using Ansible Plugin') {
            steps {
                ansiblePlaybook(
                    playbook: 'ansidocker/deploy.yml',
                    inventory: 'ansidocker/hosts.ini',
                    credentialsId: 'ssh-key-id',
                    disableHostKeyChecking: true
                )
            }
        }
    }
}
