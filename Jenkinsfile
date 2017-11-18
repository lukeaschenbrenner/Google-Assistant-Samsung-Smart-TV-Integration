node {
	def docker
	def service = "samsung-smart-tv-remote"
	
	stage('Preparation') {
		checkout scm
		
		def dockerHome = tool 'Docker'
		docker = "${dockerHome}/bin/docker"
	}
	
	stage('Docker Image Build') {
		sh "${docker} build -t ${service}:latest ."
	}
	
	stage('Docker Deploy') {
		sh "${docker} stop ${service} || true"
		sh "${docker} rm ${service} || true"
		sh "${docker} run --name ${service} ${service}"
	}
	
}