" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  "autocmd VimEnter * PlugInstall
  "autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin('~/.config/nvim/autoload/plugged')
    " Better Syntax Support
    Plug 'sheerun/vim-polyglot'

    "Auto pairs for '(' '[' '{'
    Plug 'jiangmiao/auto-pairs'

    "Themes
    Plug 'morhetz/gruvbox'
    Plug 'arzg/vim-colors-xcode'
    Plug 'patstockwell/vim-monokai-tasty'

    " Stable version of coc
    Plug 'neoclide/coc.nvim'
    
    "Airline (bottom bar)
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'

    "Ranger Plugin
    "Plug 'kevinhwang91/rnvimr', {'do': 'make sync'}
    
    "Nerdtree
    Plug 'preservim/nerdtree'

    "Commentary -- Plugin to comment out lines
    "To comment out something: <Spc>-/
    Plug 'tpope/vim-commentary'

    "CSS color
    Plug 'ap/vim-css-color'

    "Vim-which-key, similar to emacs
    Plug 'liuchengxu/vim-which-key'

    "Plugin for the startpage
    Plug 'mhinz/vim-startify'

call plug#end()
