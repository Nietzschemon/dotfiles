local options = {
  ensure_installed = { "lua", "typescript", "sql", "json", "yaml", "html", "css", "javascript", "tsx", "bash", "vim", "dockerfile", "scss", "vue", "python", "react" },

  highlight = {
    enable = true,
    use_languagetree = true,
  },

  indent = { enable = true },
  textobjects = {
    enable = true,
    select = {
      enable = true,
      lookahead = true,
      keymaps = {
          ['aa'] = '@parameter.outer',
          ['ia'] = '@parameter.inner',
          ['af'] = '@function.outer',
          ['if'] = '@function.inner',
          ['ac'] = '@class.outer',
          ['ic'] = '@class.inner',
          ['ii'] = '@conditional.inner',
          ['ai'] = '@conditional.outer',
          ['il'] = '@loop.inner',
          ['al'] = '@loop.outer',
          ['at'] = '@comment.outer',
      },
    },
  },
}

return options
