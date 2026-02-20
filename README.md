# Ansible Sign Demo Project

## Description
This project demonstrates the process of signing Ansible projects using GPG keys for security verification.

## Requirements
* GPG (GNU Privacy Guard)
* Ansible-sign utility
* RHEL 8 or higher environment

## Usage
To sign this project, ensure your GPG key is generated and use the following command:
`ansible-sign project gpg-sign .`

## Manifest Information
This project uses a MANIFEST.in file to:
* Exclude .git directories from the signature.
* Include this README.md file in the integrity check.
