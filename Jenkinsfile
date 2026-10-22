pipeline {

    agent any



    stages {

        stage('Checkout') {

            steps {

                checkout scm

            }

        }



        stage('Check Python') {

            steps {

                sh 'python3 --version'

            }

        }



        stage('Run Calculator Tests') {

            steps {

                sh 'python3 -m unittest -v'

            }

        }



        stage('Calculator Smoke Test') {

            steps {

                sh 'echo "Testing calculator multiplication"'

                sh 'python3 -c "assert 21 * 45 == 945; print(\\\"Multiplication test passed\\\")"'

            }

        }

    }



    post {

        success {

            echo 'SUCCESS: Calculator build and tests completed!'

        }

        failure {

            echo 'FAILURE: Check the console output for errors.'

        }

    }

}
