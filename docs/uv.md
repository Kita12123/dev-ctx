---
name: uv
description: what is uv and how to use it.
tags:
  - knowledge
thumb: https://cdn2.thecatapi.com/images/74i.jpg
---
# uv

## When to use
- To manage Python environments.
- To manage Python packages.

## What is "uv"?
"uv" is a Python environment and package manager. It is a tool to manage Python environments and packages effectively.
It is most fast and easy to use compared to other Python environment and package managers such as pip, pipenv, poetry, and conda.
I suggest using "uv" for AI agents to manage their Python environments and packages.

## Getting Started
If your machine is windows, you can install uv with the following command in PowerShell:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

*reference: https://docs.astral.sh/uv/getting-started/installation/

## Trubleshooting
- The command "uv" is not found after installing uv.
  - Restart your terminal. If you use terminal in VS Code, please restart all VS Code windows.