-- [[ Configure and install plugins using Lazy ]]
require('lazy').setup({
  require 'plugins/whichkey',

  require 'plugins/cmp',

  require 'plugins/indent_line',

  require 'plugins/lspconfig',

  require 'plugins/conform',

  require 'plugins/telescope',

  require 'plugins/treesitter',

  { 'rose-pine/neovim', name = 'rose-pine' },
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
