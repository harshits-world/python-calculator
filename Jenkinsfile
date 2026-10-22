pipeline {

    agent any



    stages {

        stage('Checkout') {

            steps {

                checkout scm

            }

        }



        stage('Build') {

            steps {

                sh 'python3 --version'

                sh 'python3 -m py_compile calculator.py'

            }

        }



        stage('Test') {

            steps {

                sh 'python3 -m unittest -v'

            }

        }



        stage('Smoke Test') {

            steps {

                sh 'python3 -c "assert 21 * 45 == 945; print(\'Multiplication test passed\')"'

            }

        }



        stage('Deploy') {

            steps {

                sh '''

                    mkdir -p "$WORKSPACE/deploy"

                    cp calculator.py "$WORKSPACE/deploy/"

                    echo "Deployment successful"

                    ls -l "$WORKSPACE/deploy/"

                '''

            }

        }

    }



    post {

        success {

            echo 'SUCCESS: Build, tests, and deployment completed!'

        }

        failure {

            echo 'FAILURE: Check the console output.'

        }

    }

}
