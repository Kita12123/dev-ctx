---
name: github-models
tags:
  - knowledge
thumb: https://cdn2.thecatapi.com/images/a7m.jpg
---
# GitHub Models

## When to use
- To use LLMs (Large Language Models) such as GPT-4 and GPT-3.5.
- To manage LLMs effectively.

## What is "GitHub Models"?
[GitHub Models](https://docs.github.com/ja/github-models/about-github-models) is a tool to manage LLMs effectively.

## How to use
1. Select a model from the list of available models on [here](https://github.com/marketplace/models).
2. Click "Use this model" and follow the instructions of issue personal access token.
3. See [GitHub API documentation](https://docs.github.com/ja/rest/models) for get AI models you can use with GitHub API. Example:
```powershell
$token = "<your personal access token>"
$headers = @{
  "Authorization" = "Bearer $token"
  "Accept" =  "application/vnd.github+json"
  "X-GitHub-Api-Version" = "2026-03-10" # current apiVersion
}

Invoke-RestMethod `
  -Method Get `
  -Uri "https://models.github.ai/catalog/models" `
  -Headers $headers
```
4. Use the model you want with GitHub API. Example:
```powershell
$token = "<your personal access token>"
$headers = @{
  "Authorization" = "Bearer $token"
  "Accept" =  "application/vnd.github+json"
  "X-GitHub-Api-Version" = "2026-03-10" # current apiVersion
  "Content-Type" = "application/json"
}

$body = @{
  model = "gpt-5-mini" # Selected Model ID
  messages = @(
    @{ role = "user"; content = "hello" }
  )
} | ConvertTo-Json -Depth 5

Invoke-RestMethod `
  -Method Post `
  -Uri "https://models.github.ai/inference/chat/completions" `
  -Headers $headers `
  -Body $body
```