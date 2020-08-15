---
author: ''
category: Powershell
date: '2019-11-04'
summary: ''
title: Powershell Basics
---
## Help

    Get-Help

Get help with examples:

    get-help Connect-VIServer -examples


### Finding Commands

    Get-Command 

    Get-Command -Module "VMware.vimAutomation.Storage"
    
Just show the name for each command:

    Get-Command -Module "VMware.vimAutomation.Storage" | ForEach-Object { $_.name }

Find commands that move clusters:

    Get-Command -Verb move -Noun cluster

    Get-Command -Module VMWare.vimAutomation.Cloud -Verb get

### ISE

Only works with powershell

### VS Code

Install the Vscode extension

### Modules

PSM - Powershell module shell

## VMWare

Connect to VCenter

    connect-viserver –server vcenter-appliance-test.example.co.za -Force 

Get VM's:

    Get-VM

Format table (can format to table):

    Get-VM | ft


## Find Module

    Find-Module VMware* 

Install powershell module:

    Find-Module VMware.PowerCLI | Install-Module

Update all module:

    Get-Module -ListAvailable| Update-Module

## Profiles

Profile file is found by going:

    $profile

    $Varname = @{
        abc = "123"
        def = "456"
    }

Can import module in this profile:

    import-module /my/path/to/psd1

> `psd1` is the manifest for the functions

## Credential

Using credentials

    $credential = Get-Credential

### History

    Get-History

