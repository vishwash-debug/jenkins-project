pipeline {
    agent { label 'master' }

    stages {

        stage('Clone Code') {
            steps {
                git url: 'https://github.com/vishwash-debug/jenkins-project.git', branch: 'main'
            }
        }

        stage('Deploy using Ansible') {
            steps {
                sh '''
                ansible-playbook -i ansidocker/hosts.ini ansidocker/deploy.yml
                '''
            }
        }
    }
}
