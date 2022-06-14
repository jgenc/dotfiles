" Vim Plug
	call plug#begin()
	" Icons // Req: A patched font
	Plug 'kyazdani42/nvim-web-devicons'
		
	" Telescope : Fuzzy finder
	" Req:	plenary
	"		nvim-treesitter
	Plug 'nvim-lua/plenary.nvim'
	Plug 'nvim-telescope/telescope.nvim'
	" Installed libstdc++-devel on Fedora
	Plug 'nvim-treesitter/nvim-treesitter'
	
	" Tabline plugin
	Plug 'romgrk/barbar.nvim'


	" Hex Color highlighter 
	Plug 'norcalli/nvim-colorizer.lua'

	" Neon Colort heme
	Plug 'rafamadriz/neon'

	" Lualine
	Plug 'nvim-lualine/lualine.nvim'

	set encoding=UTF-8
call plug#end()

lua require'colorizer'.setup()

lua << END
require('lualine').setup()
END
