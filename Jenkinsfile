pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git url: 'https://github.com/vishwash-debug/jenkins-project.git', branch: 'main'
            }
        }

        stage('Deploy using Ansible') {
            steps {
                sh '''
                /usr/bin/ansible-playbook -i ansidocker/hosts.ini ansidocker/deploy.yml
                '''
            }
        }
    }
}
