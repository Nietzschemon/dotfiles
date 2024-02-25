local M = {}

M.copilot = {
  i = {
    ["<C-j>"] = {
      function()
        vim.fn.feedkeys(vim.fn['copilot#Accept']("\\<CR>"), '')
      end,
      "Copilot Accept",
      {replace_keycodes = true, nowait=true, silent=true, expr=true, noremap=true}
    }
  }
}

return M
