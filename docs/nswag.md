---
name: nswag
description: what is nswag and how to use it
cover: https://cdn2.thecatapi.com/images/MTc4NzYzMg.jpg
---
# NSwag

## When to use
- To automatically generate .NET, .NET ASP Core and TypeScript code from openapi/swagger file.
- To automatically generate openapi/swagger file from .NET, .NET ASP Core and TypeScript code.
- To easily synchronize openapi/swagger file and .NET, .NET ASP Core and TypeScript code.

## What is "NSwag"?
[NSwag](https://github.com/RicoSuter/NSwag) is a Swagger/OpenAPI toolchain for .NET, ASP.NET Core and TypeScript.

## Getting Started
1. Create `nswag.json` file with [NSwag Studio](https://github.com/RicoSuter/NSwag/wiki/NSwagStudio) or manually.
1. Put `nswag.json` file to the project root directory.
2. Run command: `npx nswag run "nswag.json"` in terminal to generate source code from openapi specification.

## Example: NSwag.json
I suggest using the following `nswag.json` file for generating .NET ASP Core controller code from `openapi.yml` file.
```json
{
  "runtime": "Net100",
  "defaultVariables": null,
  "documentGenerator": {
    "fromDocument": {
      "json": "",
      "url": "openapi.yml",
      "output": null
    }
  },
  "codeGenerators": {
    "openApiToCSharpController": {
      "controllerBaseClass": "Microsoft.AspNetCore.Mvc.ControllerBase",
      "controllerStyle": "abstract",
      "useCsprojMyNamespace": false,
      "aspNetNamespace": "Microsoft.AspNetCore.Mvc",
      "className": "{controller}",
      "namespace": "Server.Presentation.Controllers",
      "additionalNamespaceUsages": [],
      "additionalContractNamespaceUsages": [],
      "generateOptionalParameters": true,
      "generateJsonMethods": false,
      "enforceHttpResponseExceptionBehavior": false,
      "allowedResponseStatusCodeTypes": [
        "200",
        "201",
        "204"
      ],
      "jsonLibrary": "SystemTextJson",
      "useSystemTextJson": true,
      "output": "src/Server/Generated/GeneratedControllers.cs",
      "newLineBehavior": "Auto",
      "csharpGeneratorSettings": {
        "namespace": "Server.Application.Dtos",
        "requiredPropertiesMustBeDefined": true,
        "dateType": "System.DateTimeOffset",
        "dateTimeType": "System.DateTimeOffset",
        "timeType": "System.TimeSpan",
        "timeSpanType": "System.TimeSpan",
        "arrayType": "System.Collections.Generic.List",
        "arrayInstanceType": "System.Collections.Generic.List",
        "dictionaryType": "System.Collections.Generic.Dictionary",
        "dictionaryInstanceType": "System.Collections.Generic.Dictionary",
        "arrayBaseType": "System.Collections.Generic.List",
        "dictionaryBaseType": "System.Collections.Generic.Dictionary",
        "classStyle": "Poco",
        "generateDefaultValues": true,
        "generateDataAnnotations": true,
        "excludedTypeNames": [],
        "handleReferences": true,
        "generateImmutableArrayProperties": false,
        "generateImmutableDictionaryProperties": false,
        "jsonSerializerSettingsTransformationMethod": null,
        "inlineNamedArrays": false,
        "inlineNamedDictionaries": false,
        "inlineNamedTuples": false,
        "inlineNamedAny": false,
        "anyType": "object",
        "integerType": "int",
        "numberType": "decimal",
        "enumNameHistory": false
      }
    }
  }
}
```