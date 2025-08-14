local M = {}

local vars = require("avviki.vars")

M.setup = function(opts)
  -- Quit if Avviki is already loaded
  --
  if vim.g.avviki_loaded then
    return
  else
    vim.g.avviki_loaded = 1
  end

  -- Begin setup
  --
  opts = opts or {}

  if opts.avviki_sources then
    vim.g.avviki_sources = opts.avviki_sources
  end
end


return M
