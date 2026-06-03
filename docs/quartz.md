---
name: quartz
description: what is quartz and how to use it
tags:
  - knowledge
cover: https://cdn2.thecatapi.com/images/6j7.jpg
---
# Quartz

## When to use
- To easily share your Obsidian vault.

## What is "Quartz"?
[Quartz](https://quartz.jzhao.xyz/) is a tool to convert your Obsidian vault into a static website.

## Usage

### 1. Deploy on GitHub Pages
Show [here](https://quartz.jzhao.xyz/getting-started/installation) for detailed instructions.
1. Clone the Quartz repository on different location from your vault.
2. Move the `quartz` folder and run `npm i` in the terminal.
3. Setup quartz with run `npx quartz create` and follow parameters. ("obsidian", "EmptyFolder", "dev-ctx")
4. Setup remote with run `git remote rm origin` and `git remote add origin <your repository url>` in the terminal on quartz repository.
5. Deploy on GitHub Pages with `npx quartz sync` in the terminal.

But.. I don't recommend using Quartz. Because GitHub can render markdown files and you can see your vault without deploying it on GitHub Pages.
