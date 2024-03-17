---@type MappingsTable
local M = {}

M.general = {
  n = {
    [";"] = { ":", "enter command mode", opts = { nowait = true } },

    --  format with conform
    ["<leader>fm"] = {
      function()
        require("conform").format()
      end,
      "formatting",
    },
  },
  v = {
    [">"] = { ">gv", "indent" },
  },
}
vim.keymap.set("n", "<Tab>", ":bn!<CR>", {})
vim.keymap.set("n", "<S-Tab>", ":bn!<CR>", {})
-- map <TAB> :bn!<CR>
-- map <S-TAB> :bp!<CR>
-- more keybinds!

return M
