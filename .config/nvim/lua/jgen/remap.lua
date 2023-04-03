-- TODO: Find a better combinantion to summon netrw
-- Space-e: 
-- Open netrw
vim.keymap.set("n", "<leader>e", vim.cmd.Ex)

-- These two keybinds move whatever is highlighted with the cursor, truly
-- useful
vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv")
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv")

-- J appends line under cursor to current line but moves cursor at the end of 
-- the current line. This keybind will keep the cursor where it was
vim.keymap.set("n", "J", "mzJ`z")

-- When searching the cursor will remain in the middle 
vim.keymap.set("n", "n", "nzzzv")
vim.keymap.set("n", "N", "Nzzzv")

-- Space-p:
-- Pasting over something will not overwrite the clipboard register
-- Paste over highlighted content with Space-p and the clipboard will not be
-- overwritten
vim.keymap.set("x", "<leader>p", "\"_dP")

-- Copy to system clipboard
vim.keymap.set({"n", "v"}, "<leader>y", "\"+y")

-- Space-s: Replace word on cursor
vim.keymap.set("n", "<leader>s", ":%s/\\<<C-r><C-w>\\>/<C-r><C-w>/gI<Left><Left><Left>")

-- Change theme
vim.keymap.set("n", "<leader>qq", function() vim.cmd "colorscheme moonfl" end)
vim.keymap.set("n", "<leader>qw", function()
    vim.cmd "colorscheme onelight"
end)

-- Swap tabs
vim.keymap.set("n", "<leader>]", ":tabnext<CR>")
vim.keymap.set("n", "<leader>[", ":tabprevious<CR>")
