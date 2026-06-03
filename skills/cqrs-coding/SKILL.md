---
name: cqrs-coding
tags:
  - skill
---
# CQRS Coding

## When to use
- To implement the Command Query Responsibility Segregation (CQRS) pattern in backend projects.

## What is CQRS?
CQRS is a design pattern that separates the read and write operations of a system into two distinct models: Command and Query.

## Getting Started
1. Install Nuget package [`Mediator.SourceGenerator` and `Mediator.Abstractions`](https://github.com/martinothamar/Mediator) to the project of application layer.

## Core Principles

### Command
When implementing the Command part of CQRS, you can follow these principles: [Command](references/command.md).

### Query
When implementing the Query part of CQRS, you can follow these principles: [Query](references/query.md).