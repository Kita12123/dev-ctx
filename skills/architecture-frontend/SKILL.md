---
name: architecture-frontend
---
# Architecture - Frontend

## When to use
- To design and maintain the architecture of a frontend application.
- To create or edit documentation related to frontend architecture.
- To implement architectural improvements or refactor existing frontend systems.
- To optimize performance or enhance security in a frontend architecture.
- To review architectural decisions or provide feedback on frontend design practices.

## Core Principles
- **Component-Based Architecture**: Structure the frontend application using reusable components, following best practices for separation of concerns and maintainability.
- **SourceCode-First Design**: Adopt a SourceCode-First approach to design the frontend architecture, ensuring that the codebase is the primary source of truth for the application's structure and behavior.

See the "References" section below for details.

## Getting Started: React project setup
1. If you haven't already, install Node.js and npm on your machine.
2. Run `npx shadcn@latest init --preset b1aKNEsHA --base base --template next --rtl --pointer --name frontend` to set up the project structure using Shadcn UI.
3. Run `npm i` to install all dependencies and ensure the project is ready for development.

## References

### Component-Based Architecture
- **Shadcn UI**: Use Shadcn UI as a component library to build the frontend application, following its design principles and best practices for component composition and styling. If you need to customize or extend the components, refer to the Shadcn UI documentation for guidance on how to create custom components or modify existing ones while maintaining consistency with the overall design system.

### SourceCode-First Design
- **Storybook**: Use Storybook to document and visualize the frontend components, ensuring that the codebase is the primary source of truth for the application's structure and behavior. This approach allows for better collaboration between developers and designers, as well as easier maintenance and scalability of the frontend architecture.
- **Chromatic**: Use Chromatic to manage and review changes to the frontend components, ensuring that any modifications are properly tested and reviewed before being merged into the main codebase. This helps maintain the integrity of the frontend architecture and ensures that all changes are aligned with the overall design principles and best practices.