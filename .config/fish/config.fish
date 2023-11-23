if status is-interactive
    # Commands to run in interactive sessions can go here
end

# Environment vars
set -gx EDITOR /usr/bin/vim
set -gx FLYCTL_INSTALL "/home/jorgen/.fly" 
set -gx DENO_INSTALL "/home/jorgen/.deno"

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

# ls replacer
alias ls="exa --icons --header"

# Python
alias p="python"


# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
#eval /usr/bin/conda "shell.fish" "hook" $argv | source
# <<< conda initialize <<<

