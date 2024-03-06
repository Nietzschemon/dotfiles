local M = {}


-- Override the default configuration for the copilot plugin
M.copilot = {
  -- Possible configurable fields can be found on:
  -- https://github.com/zbirenbaum/copilot.lua#setup-and-configuration
  suggestion = {
    auto_trigger = true,
  },
  vim.keymap.set('i', '<c-w>', 'copilot#Accept("")', {
    expr = true,
    replace_keycodes = false
  }),

}

return M
