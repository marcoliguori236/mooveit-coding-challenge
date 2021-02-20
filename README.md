# mooveit-coding-challenge
 Coding challenge from Moove It for technical interview
 
## Introduction

This project represents a conceptual implementation of the Memcached system, it is not intended for practical use, although it tries to hover over several programming concepts in order to demonstrate technical capabilities within software development.

The project was developed in Python 3.9.1.

## Supported commands

Commands supported from the real Memcached system are:
* get
* set 
* add
* replace
* append
* prepend
* replace

'cas' and 'gets' were not supported for practical context reasons.

Lastly, it is important to note that instead of accepting <command name> <key> <flags> <exptime> <bytes> [noreply]\r\n
cas <key> <flags> <exptime> <bytes> <cas unique> [noreply]\r\n like the real Memcached system, this implementation uses the following protocol:
 <command name> <key> <value> <bytes>.

## Reproductibility

In order to reproduce the project, one must have Python and a Python interpreter installed on his/her computer. As an interpreter i used Visual Studio Code, which the environments files were uploaded under 'project_env' for reproductibility reasons.

### How to reproduce the project

The most basic way of setting up the project is to:
- Download Python from https://www.python.org/downloads/ and install it
- Download .zip files from GitHub repository
- Extract them into your Desktop
- Run server.py choosing Python as interpreter
- Run client.py choosing Python as interpreter
- From client window, enter supported commands

To run tests:
- Run memcached_tests.py choosing Python as interpreter
The output should be:



