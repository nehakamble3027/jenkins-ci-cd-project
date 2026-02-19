pipeline {
    agent any

    stages {

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
                    git config user.name "nehakamble3027"
                    git add .
                    git commit -m "Auto deploy from Jenkins" || exit 0
                    git push origin main
                '''
            }
        }
    }
}
