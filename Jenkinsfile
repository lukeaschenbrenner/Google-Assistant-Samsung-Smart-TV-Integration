node {
	def docker
	def service = "samsung-smart-tv-remote"
	
	stage('Preparation') {
		checkout scm
		
		def dockerHome = tool 'Docker'
		docker = "${dockerHome}/bin/docker"
	}

    stage('Docker Image Build') {
        sh "mv config/artik_cloud.ini.example config/artik_cloud.ini"
        sh "sed -i -- 's/add_your_device_id/$artik_cloud_device_id/g' config/artik_cloud.ini"
        sh "sed -i -- 's/add_your_device_token/$artik_cloud_device_token/g' config/artik_cloud.ini"

        sh "mv config/samsung_smart_tv_remote.ini.example config/samsung_smart_tv_remote.ini"
        sh "sed -i -- 's/add_your_tv_ip/$samsung_smart_tv_ip/g' config/samsung_smart_tv_remote.ini"
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