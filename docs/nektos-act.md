---
name: nektos/act
description: what is github nektos/act and how to use it.
tags:
  - knowledge
  - framework
thumb: https://cdn2.thecatapi.com/images/8kk.jpg
---
# Nektos/Act
[Nektos/Act](https://github.com/nektos/act) is a framework for running [GitHub Action](github-action.md) locally.

## When to use
- To run GitHub Actioin locally.
- To evaluate GitHub Action.

## Getting Started
**reference**: https://nektosact.com/installation/index.html
If your want to run with windows, you can install act with run `winget install nektos.act` in the terminal.
You can implement action with just running `act` in the project root directory.

## Getting Started : Linux
Please install and login docker and check [act release version](https://github.com/nektos/act/releases/latest)
```
# Install act
curl -OL https://github.com/nektos/act/releases/download/{VERSION}/act_Linux_x86_64.tar.gz
tar -zxvf act_Linux_x86_64.tar.gz
# Confirm
./act --version
# Run
sudo ./act -W ./.github/workflows/<FileName>.yml
```

## Usage
If you use `ubuntu-latest` as machine and define action file name  as "dotnet.yml", you can implement with following:
```
act -P ubuntu-latest=-self-hosted -W .github/workflows/dotnet.yml
```

If you use command `actions/upload-artifact`, use `--artifact-server-path` parameter. Example:
```
act --artifact-server-path ./artifacts
```

If you defined secret variable on GitHub Secret Service, use `-s` parameter. Example:
```
act -s NUGET_PASSWORD=password
```

>[!NOTE]
>You don't have to set parameter if you create setting file `.actrc` on the project root directory as following:
>```
>-P ubuntu-latest=catthehacker/ubuntu:act-latest
>--artifact-server-path ./artifacts
>```