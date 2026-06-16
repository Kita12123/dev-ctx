---
name: Oh My Zsh
description: what is Oh My Zsh and how to use it.
tags:
  - knowledge
  - framework
thumb: https://cdn2.thecatapi.com/images/aco.jpg
---
# Oh My Zsh
*repository*: https://github.com/ohmyzsh/ohmyzsh

## When to use
- To develop with the terminal in Linux.
- To develop effectivility in the terminal.

## Getting Started
*reference*: https://github.com/ohmyzsh/ohmyzsh#basic-installation
```
# Install
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)
```

## Customization
### Theme
*reference*: https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
You can change your terminal theme by modifying the `ZSH_THEME` variable in your `.zshrc` file.
I personally recommend the `fletcherm` theme; it displays the current directory, git branch, and execution time in a layout similar to PowerShell.

### Plugin
*reference*: https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins
You can enhance your development environment by modifying the 'plugins' variable in your .zshrc file. I personally recommend the following:
```zsh
plugins=(
  git-auto-fetch
  dotenv
  dotnet
  last-working-dir
)
GIT_AUTO_FETCH_INTERVAL=600 # 10 minutes
```