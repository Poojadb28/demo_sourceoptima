pipeline {
    agent any

    environment {
        PYTHON = "python"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git url: 'YOUR_GITHUB_REPO_URL', branch: 'main'
            }
        }

        stage('Setup Python') {
            steps {
                bat "${PYTHON} --version"
                bat "pip install --upgrade pip"
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "pip install -r requirements.txt"
            }
        }

        stage('Run Smoke Tests') {
            steps {
                bat "pytest -m smoke -n auto --html=reports/smoke_report.html"
            }
        }

        stage('Run Regression Tests') {
            steps {
                bat "pytest -m regression -n auto --html=reports/regression_report.html"
            }
        }
    }

    post {

        always {
            archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
            archiveArtifacts artifacts: 'screenshots/*.png', allowEmptyArchive: true
            archiveArtifacts artifacts: 'downloads/*', allowEmptyArchive: true
        }

        success {
            echo "Build Passed - All tests successful"
        }

        failure {
            echo "Build Failed - Check reports"
        }
    }
}