# Make hidden apps grayed-out
defaults write com.apple.Dock showhidden -boolean yes
killall Dock

# Speed up animation on auto-hide dock
defaults write com.apple.Dock autohide-delay -int 0
killall Dock
defaults write com.apple.Dock autohide-time-modifier -float 0.9
killall Dock
