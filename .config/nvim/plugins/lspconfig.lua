return {
  {
    "neovim/nvim-lspconfig",
    opts = {
      inlay_hints = {
        enable = true,
      },
      tools = {
        runnables = {
          use_telescope = true,
        },
        inlay_hints = {
          auto = true,
          show_parameter_hints = false,
          parameter_hints_prefix = "",
          other_hints_prefix = "",
        },
      },
      servers = {
        lua_ls = {
          workspace = { checkThirdParty = false },
          telemetry = { enable = false },
            hint = { enable = true },
        },
        rust_analyzer = {
          hint = { enable = true },
          mason = false,
          cmd = { "rust-analyzer" },
          settings = {
            ["rust-analyzer"] = {
              checkOnSave = {
                command = "clippy",
              },
              imports = {
                granularity = {
                  group = "module",
                },
                prefix = "self",
              },
              cargo = {
                allFeatures = true,
                buildScripts = {
                  enable = true,
                },
              },
              procMacro = {
                enable = true,
              },
            },
          },
        },
      },
    },
  },
}
