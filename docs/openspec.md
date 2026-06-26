---
name: OpenSpec
description: what is OpenSpec and how to use it.
tags:
  - framework
  - knowledge
thumb: https://cdn2.thecatapi.com/images/dgl.jpg
---
# OpenSpec

## When to use
- To implement with SDD.
- To manage Specifications.

## Getting Started : Linux
1. Install Node
```bash
sudo apt update
sudo apt install -y nodejs npm
```
2. Install OpenSpec
```bash
sudo npm install -g @fission-ai/openspec@latest
cd <your_project>
openspec init
```

## How to use
1. Switch to `/openspec-explore` agent and task with AI agent about specifications.
2. Switch to `/openspec-propose` agent to automatically create documents (e.g. proposal.md, spec.md design.md, tasks.md).
3. Switch to `/openspec-apply-change` agent to implement from documents.
4. You fix code.
5. Switch to `/openspec-sync-specs` agent to fix documents on code base.
6. You mearge code to main branch.
7. Switch to `/openspec-archive-change` agent to confirm.