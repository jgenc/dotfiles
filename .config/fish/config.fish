if status is-interactive
    # Commands to run in interactive sessions can go here
end

# Environment vars
set -gx EDITOR /usr/bin/vim
set -gx FLYCTL_INSTALL "/home/jorgen/.fly" 

# ==================================
#           Aliases
# ==================================

#alias v="nvim"
#alias sv="sudo nvim"
alias r="ranger"

alias ru="ranger ~/Workspace/university/"

# This is used to spawn a thin wrapper for SSH, as it barely works on its own 
alias s="kitty +kitten ssh"

# Git
alias gst="git status"
alias gp="git push"
alias ga="git add"
