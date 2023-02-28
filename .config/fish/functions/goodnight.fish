function goodnight --description 'Upgrade system and shut down. Usaully used before going to sleep'
	set -l fdate (date '+%Y%m%d-%T')
	set -l dir ~/Documents/.goodnight-logs   
	# If directory does not exist, create it
	if ! test -d $dir 
		mkdir $dir
	end
	touch $dir/$fdate.log
	sudo dnf upgrade -y --refresh | tee $dir/$fdate.log 
	shutdown
    set -l myname (whoami)
    echo "goodnight $myname"
end
