local builtin = require('telescope.builtin')
vim.keymap.set('n', '<leader>ff', builtin.find_files, {})
-- TODO: Maybe find a better key combination?
vim.keymap.set('n', '<leader>fg', builtin.git_files, {})
-- INFO: This searches for anything that matches the grep input in the project directory, I really like this.
-- TODO: Make this annonymous function take ESC as a special input and not as a search value, meaning if search is ESC return
vim.keymap.set('n', '<leader>fs', function() builtin.grep_string({ search = vim.fn.input("Grep > ") }) end)
