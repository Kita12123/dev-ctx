---
name: command
tags:
  - skill
  - reference
---
# Command

# Definition
Do not use `ICommand`, `ICommandHandler` from `Mediator.SourceGenerator`.
Always use the application-specific `IAppCommand`, `IAppCommandHandler` instead.

## IAppCommand
Base interface for Command in CQRS pattern is defined `IAppCommand<TResponse>` as follows:
```csharp
using Mediator;

/// <summary>
/// Base interface for Command in CQRS pattern.
/// </summary>
public interface IAppCommand<TResponse> : ICommand<TResponse>
{
}
```

## Command Handler
Abstract base class for Command Handler in CQRS pattern is defined `AppCommandHandlerBase<TCommand, TResponse>` as follows:
```csharp
using System.ComponentModel.DataAnnotations;
using Mediator;

/// <summary>
/// Base abstract class for Command Handler in CQRS pattern.
/// </summary>
/// <param name="cmdContext">The command handler context.</param>
public abstract class AppCommandHandlerBase<TCommand, TResponse>(ICommandHandlerContext cmdContext)
    : ICommandHandler<TCommand, TResponse>
    where TCommand : IAppCommand<TResponse>
{
    private readonly ICommandHandlerContext _cmdContext = cmdContext ?? throw new ArgumentNullException(nameof(cmdContext));

    /// <inheritdoc/>
    public async ValueTask<TResponse> Handle(TCommand command, CancellationToken cancellationToken)
    {
        Validator.ValidateObject(command, new(command), true); // Validate command with DataAnnotation attributes
        var response = await this.RunAsync(this._cmdContext, command, cancellationToken);
        return response;
    }

    /// <summary>
    /// Runs the command handler logic.
    /// <br/>[Contract] This method's logic is allowed to be written in derived classes, but the method signature must not be changed.
    /// </summary>
    /// <param name="cmdContext">The command handler context.</param>
    /// <param name="command">The command to handle.</param>
    /// <param name="cancellationToken">The cancellation token.</param>
    /// <returns>The result of the command.</returns>
    protected abstract ValueTask<TResponse> RunAsync(ICommandHandlerContext cmdContext, TCommand command, CancellationToken cancellationToken);
}
```

## Context
The `ICommandHandlerContext` provides the context for the command handler as follows:
```csharp

```
- `RunCommandAsync`: A async method to run another command within the command handler.
- `AddRange`: A method to add multiple entities to database context.
- `DeleteRange`: A method to delete multiple entities from database context.