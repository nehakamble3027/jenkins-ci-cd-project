pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/nehakamble3027/jenkins-ci-cd-project.git',
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
                sh '''
                    git config user.email "nehakambble3027@gmail.com"
                    git config user.name "nehakambble3027"
                    git add .
                    git commit -m "Auto deploy from Jenkins" || true
                    git push origin main
                '''
            }
        }
    }
}
