require'nvim-treesitter.configs'.setup {
  -- A list of parser names, or "all"
  ensure_installed = { "bash", 
		"cpp",
		"css",
		"dockerfile",
		"fish",
		"html",
		"http",
		"java",
		"javascript",
		"jsdoc",
		"json",
		"pug",
		"python",
		"vim"
	},

  -- Install parsers synchronously (only applied to `ensure_installed`)
  sync_install = false,

  highlight = {
    -- `false` will disable the whole extension
    enable = true,
  },
}
