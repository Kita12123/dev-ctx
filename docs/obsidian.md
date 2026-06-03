---
name: obsidian
description: what is obsidian and how to use it
tags:
  - knowledge
cover: https://cdn2.thecatapi.com/images/6j7.jpg
---
# Obsidian

## When to use
- To easily manage your knowledge.
- To use markdown files.

## What is "Obsidian"?
Obsidian is a powerful knowledge management tool that edits markdown files.
Also supports plugins that can sync with github, customize styles, and more. 
I suggest using Obsidian for AI agents to manage thier knowledge base.
Because of markdown support and github sync, it is a great tool for this purpose.

## Getting Started
1. Install Obsidian from [here](https://obsidian.md/).
2. Create a new `vault`.
3. Start creating a new `note`.
4. You can customize your vault with plugins and settings to enhance your experience.

## Usage
Obsidian has many features that can help you manage your knowledge effectively.
Here are some suggestions for using Obsidian.

### 1. With AI Agents
Install [Obsidian Skills](https://github.com/kepano/obsidian-skills) from terminal. Example command:
```shell
npx skills add https://github.com/kepano/obsidian-skills --agent github-copilot --all
```

### 2. Deploy on GitHub Pages
[Quartz](https://quartz.jzhao.xyz/) is a tool to deploy your Obsidian vault on GitHub Pages.
Show [here](quartz.md) for detailed instructions.

## Customization
Obsidian is highly customizable, and you can tailor it to your needs.
Here are some suggestions for plugins and settings to enhance your experience with Obsidian.

### 1. Plugins
I suggest using the following plugins:
- Obsidian Git, GitHub: Sync your vault with a GitHub repository for version control and backup
- Pretty Properties: Display note properties in a visually appealing way

### 2. Settings
I suggest using the following settings:
- Snippet folder: `./.obsidian/snippets` (for custom CSS)
- Wikilink style off: Use markdown links instead of wikilinks for showing links in GitHub and other markdown viewers.

## Glossary
| Term | Description |
| --- | --- |
| `vault` | A folder of markdown files that Obsidian manages. |
| `note` | A markdown file that Obsidian manages. |