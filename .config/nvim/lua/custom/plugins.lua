local overrides = require ("custom.configs.overrides")
local plugins = {
  {
    dependencies = {
      "MunifTanjim/nui.nvim",
      "nvim-lua/plenary.nvim",
      "folke/trouble.nvim",
      "nvim-telescope/telescope.nvim"
    },
    "jackMort/ChatGPT.nvim",
      event = "VeryLazy",
      config = function()
        require("chatgpt").setup({
        api_key_cmd = "rbw get gpt-api-key",
        openai_params = {
          model = "gpt-4-turbo-preview"
        }
      })
      end,
  },
  {
    "github/copilot.vim",
    lazy = false,
    event = "InsertEnter",
    opts = overrides.copilot,
    config = function()
      -- Mapping tab is already used by NvChad
      vim.g.copilot_no_tab_map = true;
      vim.g.copilot_assume_mapped = true;
      vim.g.copilot_tab_fallback = "";
      -- The mapping is set to other key, see custom/lua/mappings
      -- or run <leader>ch to see copilot mapping section
    end
  },
  {
    "williamboman/mason.nvim",
    cmd = { "Mason", "MasonInstall", "MasonInstallAll", "MasonUpdate" },
    opts = {
      ensure_installed = {
        "mypy",
        "ruff",
        "pyright",
      }
    },
  },
  {
    "neovim/nvim-lspconfig",
    config = function()
      require "plugins.configs.lspconfig"
      require "custom.configs.lspconfig"
    end,
  },
}
return plugins
