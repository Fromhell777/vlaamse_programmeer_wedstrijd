
-- Configure custom keybindings
vim.keymap.set('n', '<Leader>dn', vim.diagnostic.goto_next, {})
vim.keymap.set('n', '<Leader>dp', vim.diagnostic.goto_prev, {})
vim.keymap.set('n', '<Leader>de', vim.diagnostic.open_float, {})

-- Configure Telescop to either search only git files or search all the files
local telescope_builtin = require('telescope.builtin')
local find_all_files = function()
  telescope_builtin.find_files({no_ignore=true, hidden=true})
end


vim.keymap.set('n', '<Leader>ff', telescope_builtin.find_files, {})
vim.keymap.set('n', '<Leader>af', find_all_files, {})

vim.keymap.set('n', '<Leader>lrf', vim.lsp.buf.format, {})

-- Vim behaviour of yank of a line
vim.keymap.set('n', 'Y', "yy")

vim.keymap.set('n', '<F1>', ":bp<CR>", {})
vim.keymap.set('n', '<F2>', ":bn<CR>", {})
vim.keymap.set('n', '<F3>', ":b#<CR>", {})

vim.keymap.set('n', '<F4>', ":lcd `dirname %`<CR>")

vim.keymap.set('c', "bd<CR>", "BufDel<CR>")

-- Comment.nvim keybindings
local comment_api = require('Comment.api')
vim.keymap.set('n', '<Leader>/', comment_api.toggle.linewise.current)
vim.keymap.set('x', '<Leader>/', '<Plug>(comment_toggle_linewise_visual)')
