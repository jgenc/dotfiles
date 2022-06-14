" Settings
set number
set autoindent
set tabstop=4
set shiftwidth=4
set smarttab
set softtabstop=4
set mouse=a
set termguicolors
set cc=80
set clipboard=unnamedplus
set ttyfast

source $HOME/.config/nvim/keys.vim
source $HOME/.config/nvim/plug.vim
source $HOME/.config/nvim/lua/treesitter.lua

" Colorscheme settings
"	Note: For neon
"		There are various options, to see them run `:help neon.txt`
let g:neon_style = "dark"
let g:neon_italic_keyword = v:true
let g:neon_italic_boolean = v:true
let g:neon_italic_function = v:true
let g:neon_bold = v:true

colorscheme neon
