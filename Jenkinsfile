pipeline {

  agent any 

  stages {

    stage('Initial branch check and adhoc config'){
    
     when {
       branch 'mains'

     }
     steps {
             sh 'echo $BUILD_NUMBER'
             sh 'touch /var/tmp/$BUILD_NUMBER' 
           }

    post {
      failure {
         sh 'echo DONE-WRONG'

       }
      success {
         sh 'echo DONE-WRONG'

       }


    }
    }
  } 
 

}
