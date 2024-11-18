       pipeline {
           agent any
           environment {
               DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
           }
           stages {
               stage('Clone Repository') {
                   steps {
                       git 'https://github.com/sarabarona/Integraci-n-continua-Socket.git'
                   }
               }
               stage('Build Docker Image') {
                   steps {
                       script {
                           dockerImage = docker.build("usuario/app:${env.BUILD_ID}")
                       }
                   }
               }
               stage('Push Docker Image') {
                   steps {
                       script {
                           docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                               dockerImage.push()
                           }
                       }
                   }
               }
               stage('Deploy') {
                   steps {
                       sh 'docker-compose up -d'
                   }
               }
           }
           post {
               always {
                   cleanWs()
               }
           }
       }
