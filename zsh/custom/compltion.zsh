# Fish-like Pager (Tab Menu) Configuration

# Enable interactive selection highlighting
zstyle ':completion:*' menu select

# 1. Colors Setup
# 'ma' = Selection Highlight.
# 48;5;236 is the ANSI background for #333 (Dark Grey)
# 38;5;255 is the ANSI foreground for White
# 'no' = Standard text color.
# 38;5;250 is the ANSI foreground for #BBB (Light Grey)
zstyle ':completion:*' list-colors "ma=48;5;236;38;5;255:no=38;5;250"

# 2. Description Styling (fish_pager_color_description 666)
# %F{242} is the ANSI code for #666 (Grey)
zstyle ':completion:*:*:*:*:descriptions' format '%F{242}-- %d --%f'

# 3. Group Titles (like "Aliases", "Commands") -> Teal (#00AAAA)
zstyle ':completion:*:*:*:*:messages' format '%F{37}%d%f'
zstyle ':completion:*:*:*:*:warnings' format '%F{red}No matches found%f'
