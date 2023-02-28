function kitty-theme --description 'Change kitty theme to light theme'
    if test -z $argv
        echo "No argument provided. Possible argumenets are 'd' for dark and 'l' for light." 
        return
    end
    if test $argv = "l"
        kitty +kitten themes PaperColor\ Light
        echo y | fish_config theme save Mono\ Lace 
    else if test $argv = "d"
        kitty +kitten themes Moonfly
        echo y | fish_config theme save Just\ a\ Touch
    else
        echo "Incorrect Arguement"
    end
end
