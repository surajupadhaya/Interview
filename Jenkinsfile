pipeline {

  agent any 
  
  

  stages {
    stage('Approval gate'){
      steps {
        input( message: 'Build is approved ??' ,ok: 'YES',submitter: 'ops-team',parameters: [ string(name:'REASON',description:'REASON for DEPLOY')])
        }
    }
    stage('Stage 1') {
     steps { sh 'echo $BUILD_NUMBER'
             sh 'echo $BRANCH_NAME'}
    }
    stage('Initial branch check and adhoc config'){
    
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
    stage('Runing the basic script '){
      steps {
        retry(3){
          script { 
                 def returncode = sh( script: 'sh /var/tmp/basic.sh',returnStatus:true)
            
	      if ( returncode != 0){
			 error ( "Failure runing  script" )
		      }

                }
      }
      }
      post {
             failure {
                   echo "Script failed to ran"
                  emailext(
		      subject: "FAILED: ${JOB_NAME} #${BUILD_NUMBER}",
		      body: """
			Build failed.
			Job: ${JOB_NAME}
			Build: ${BUILD_NUMBER}
			Branch: ${GIT_BRANCH}
			URL: ${BUILD_URL}
		      """,
		      to: 'srupadhaya15@gmail.com',
		      attachLog: true
		    ) 
                   }
             success {
                   echo "Script ran"
                   }
         }

   }
  } 
 

}
