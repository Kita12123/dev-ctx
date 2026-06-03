---
name: command
tags:
  - skill
  - reference
---
# Command

# Definition

## Interface
Base interface for Command in CQRS pattern is defined `IAppCommand<TResponse>` as follows:
```csharp
using Mediator;

public interface IAppCommand<TResponse> : ICommand<TResponse>
{
}
```