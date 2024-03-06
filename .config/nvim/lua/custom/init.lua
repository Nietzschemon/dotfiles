vim.api.nvim_create_autocmd("BufWritePre", {
  pattern = "*",
  callback = function(args)
    require("conform").format({ bufnr = args.buf })
  end,
})
-- Set up an autocommand for Python files
--[[
vim.api.nvim_create_augroup("PythonFolding", { clear = true })
vim.api.nvim_create_autocmd("FileType", {
  pattern = "python",
  group = "PythonFolding",
  callback = function()
    -- Set fold method to expression for Python files
    vim.wo.foldmethod = "expr"
    -- Set the fold expression to use a custom Lua function
    vim.wo.foldexpr = "v:lua.python_foldexpr(v:lnum)"
  end,
})

-- Define the Lua function for determining fold levels
function _G.python_foldexpr(lnum)
  local line = vim.fn.getline(lnum)
  -- Check if the line is a comment
  if line:match("^%s*\"\"\"") then
    return ">1"
  else
    return "="
  end
end
]]--
vim.wo.relativenumber = true
vim.opt.clipboard = "unnamedplus"
