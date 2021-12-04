pipeline {
    agent any
    stages {
        stage ('Checkout Project') {
            steps {
                git credentialsId: '3312bfb1-5093-40f4-b850-555df00dfcba', url: 'https://github.com/RitikSVala/QA-Practical-Project.git', branch: 'main'
            }
        }
        
        stage ('Prepare docker images') {
            steps {
                dir('QA-Practical-Project') {
                    withCredentials([usernamePassword(credentialsId: '910f0823-51a3-4658-8d06-f486ba1273c9', passwordVariable: 'pass', usernameVariable: 'user')]) {
                      sh "docker-compose build --parallel"
                      sh "docker login -u ${user} -p ${pass}"
                      sh "docker-compose push"
                    }
                }
            }
        }
        
        stage ('Deploy applications') {
            steps {
                sh "ls -l"
                sh "ansible-playbook configurations/playbook.yml"
            }
        }
    }
}