pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Execute Python Script') {
            steps {
                script {
                    // Definir a variável para o caminho do script Python
                    def pythonScriptPath = ". app.py"

                    // Executar o script Python usando o interpretador Python
                    sh "python3 ${pythonScriptPath}"
                }
            }
        }
    }
}
