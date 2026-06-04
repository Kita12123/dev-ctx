---
name: lang-chain
description: what is Lang Chain and how to use it.
tags:
  - knowledge
thumb: https://cdn2.thecatapi.com/images/cjc.jpg
---
# Lang Chain

## When to use
- To manage workflow of AI agents.
- To visualize the workflow of AI agents.
- To customize the workflow of AI agents.
- To define development process of AI agents.

## What is "Lang Chain"?
[Lang Chain](https://www.langchain.com/langchain) is a Python framework to orchestrate AI agents.

## Memory of Setup
Setup for OpenAI Example:
1. If you don't have "uv" installed, please refer to the [uv](uv.md) documentation and install it.
2. Install Lang Chain with running following command in terminal.
```bash
uv init
uv add langchain deepagents langchain-openai
uv sync
```
3. Add `.env` file in the project root directory and set API keys for LLMs. Example: OPENAI_API_KEY="your personal acccess token"