
-- Generally sensible vim settings
vim.opt.shiftwidth = 2
vim.opt.tabstop = 8
vim.opt.expandtab = true
vim.opt.number = true
vim.opt.relativenumber = true

-- Install Lazy plugin manager
local lazypath = vim.fn.stdpath('data') .. '/lazy/lazy.nvim'
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    'git',
    'clone',
    '--filter=blob:none',
    'https://github.com/folke/lazy.nvim.git',
    '--branch=stable', -- latest stable release
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

-- Setup Lazy plugins
require('lazy').setup({
  'folke/which-key.nvim',
  'neovim/nvim-lspconfig',
  {
    'hrsh7th/nvim-cmp', -- Autocompletion plugin
    dependencies = {
      'hrsh7th/cmp-nvim-lsp', -- LSP support for autocompletion
      'L3MON4D3/LuaSnip',
      'saadparwaiz1/cmp_luasnip',
    },
  },
  {
    'nvim-telescope/telescope.nvim',
    dependencies = { 'nvim-lua/plenary.nvim' }
  },
  { 'rose-pine/neovim', name = 'rose-pine' },
  "rgroli/other.nvim", -- Cycle between related files (like a.vim or Alternate)
  {
    'numToStr/Comment.nvim',
    lazy = false,
  },
  {
    "nvim-lualine/lualine.nvim", -- Pretty cool status line
    dependencies = { 'nvim-tree/nvim-web-devicons' }
  },
  {
    "NeogitOrg/neogit",
    dependencies = {
      "nvim-lua/plenary.nvim",         -- required
      "sindrets/diffview.nvim",        -- optional - Diff integration
      "nvim-telescope/telescope.nvim", -- optional
    },
    config = true
  },
  {
    "ojroques/nvim-bufdel", -- Better buffer deletion
    opts = {
      next = 'cycle',       -- Cycle through buffers according to their index
      quit = false,         -- Quit when last buffer is closed
    }
  },
})

-- Setup colorscheme
vim.cmd.colorscheme('murphy')

-- Setup status line
require('lualine').setup()

-- Setup plugin to open related file
require("other-nvim").setup({
  rememberBuffers = false,
  mappings = {
    {
      pattern = "(.*).h$",
      target = {
    {
      target = "%1.C",
      context = "default"
    },
    {
      target = "%1.tpp",
      context = "template"
    },
      }
    },
    {
      pattern = "(.*).C$",
      target = {
    {
      target = "%1.h",
      context = "default"
    },
    {
      target = "%1.tpp",
      context = "template"
    },
      }
    },
    {
      pattern = "(.*).tpp$",
      target = {
    {
      target = "%1.h",
      context = "default"
    },
    {
      target = "%1.C",
      context = "template"
    },
      }
    },
    {
      pattern = "(.*)_ent.vhd",
      target = "%1_rtl.chd",
    },
    {
      pattern = "(.*)_rtl.vhd",
      target = "%1_ent.chd",
    }
  }
})

local cmp = require('cmp')
cmp.setup({
  sources = cmp.config.sources({
    { name = 'nvim-lsp' }
  }, {
    { name = 'buffer' }
  }),
  snippet = {
    expand = function(args)
      require('luasnip').lsp_expand(args.body)
    end
  }
})


local cmp_capabilities = require('cmp_nvim_lsp').default_capabilities()

local lspconfig = require('lspconfig')
local clangd_command = 'clangd'
lspconfig.clangd.setup({
  cmd = {
    'clangd',
    '--clang-tidy',
    '--header-insertion=never',
    '--pch-storage=memory', -- Change to =disk if it used too much memory
  },
  filetypes = { 'cpp', 'c' },
  capabilities = cmp_capabilities
})
lspconfig.pyright.setup({})

local telescope_builtin = require('telescope.builtin')

local find_all_files = function()
  telescope_builtin.find_files({no_ignore=true, hidden=true})
end

-- Set indent width for Python
vim.api.nvim_create_autocmd("FileType", {
  pattern = "python",
  callback = function()
    vim.opt_local.shiftwidth = 2
  end
})

-- Configure custom keybindings
vim.g.mapleader = ' '
vim.keymap.set('n', '<Leader>dn', vim.diagnostic.goto_next, {})
vim.keymap.set('n', '<Leader>dp', vim.diagnostic.goto_prev, {})
vim.keymap.set('n', '<Leader>de', vim.diagnostic.open_float, {})

vim.keymap.set('n', '<Leader>ff', telescope_builtin.find_files, {})
vim.keymap.set('n', '<Leader>af', find_all_files, {})

vim.keymap.set('n', '<Leader>lrf', vim.lsp.buf.format, {})

-- Vim behaviour of yank of a line
vim.keymap.set('n', 'Y', "yy")

vim.keymap.set('n', '<F1>', ":bp<CR>", {})
vim.keymap.set('n', '<F2>', ":bn<CR>", {})
vim.keymap.set('n', '<F3>', ":b#<CR>", {})

vim.keymap.set('n', '<F4>', ":cd dirname %<CR>")

vim.keymap.set('c', "bd<CR>", "BufDel<CR>")

-- Comment.nvim keybindings
local comment_api = require('Comment.api')
vim.keymap.set('n', '<Leader>/', comment_api.toggle.linewise.current)
vim.keymap.set('x', '<Leader>/', '<Plug>(comment_toggle_linewise_visual)')
