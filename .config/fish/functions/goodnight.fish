function goodnight --description 'Upgrade system and shut down. Usaully used before going to sleep'
	set -l fdate (date '+%Y%m%d-%T')
	sudo dnf upgrade --refresh | tee ~/Documents/.goodnight-logs/$fdate.log 
	shutdown | tee ~/Documents/.goodnight-logs/$fdate.log 

end
