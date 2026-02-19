pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/nehakambble3027/jenkins-ci-cd-project.git',
                    credentialsId: 'github-token'
            }
        }

        stage('Build') {
            steps {
                echo 'Build stage'
            }
        }

        stage('Push to GitHub') {
            steps {
                echo 'Pushing to GitHub for deployment...'
                bat '''
                    git config user.email "nehakambble3027@gmail.com"
                    git config user.name "nehakambble3027"
                    git add .
                    git commit -m "Auto deploy from Jenkins"
                    git push origin main
                '''
            }
        }
    }
}
