+++
title = "Intro to nvim-platformio.lua"
date = 2024-08-04

[taxonomies]
tags = ["nvim", "platformio"]
+++

If you work with microcontrollers you must have heard of `PlatformIO`. It is a tool which we can use to program and debug multiple families of microcontrollers in various frameworks with little to no manual setup work. PlatformIO takes care of installing the tool, setting up the project, build, upload and debug. PlatformIO comes with an extension for VS Code which wraps the underlaying `PlatformIO cli` tool and exposes a very nice interface to setup project and use other tools. But if you are a n/vim user like me, you only have the cli. I was fine with cli but I wanted that ease of use like VS Code extension so I made this neovim plugin called [nvim-platformio.lua](https://github.com/anurag3301/nvim-platformio.lua)

# Installation process

1. Install the PlatformIO core
```sh
curl -fsSL -o get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

2. Now check if you have PlatformIO cli ready to use
```sh
pio --version
```

3. Added [`anurag3301/nvim-platformio.lua`](https://github.com/anurag3301/nvim-platformio.lua) plugin and its dependencies for installation in your neovim package manager, here I have given example for `lazy.nvim`
```lua
return {
    "anurag3301/nvim-platformio.lua",
    dependencies = {
        { "akinsho/nvim-toggleterm.lua" },
        { "nvim-telescope/telescope.nvim" },
        { "nvim-lua/plenary.nvim" },
    },
}
```

And that's you have `nvim-platformio.lua` and `PlatformIO` ready to be used 🥳.

