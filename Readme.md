# Network Scanner Tool

## Introduction
This project is a simple wrapper of Nmap
It serves the simple purpose of sending automatically the result to your notification service (yes you can do the same with some smart piping in linux)

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Installation
To install the necessary dependencies for this tool, run the following command:
`pip install -r requirements.txt`

## Usage
To use this tool, run the following command from the terminal:
`python main.py --port [PORT_RANGE] --ip [TARGET_IP] --send [RESULT_URL]`
- `--port`: Port range to scan (default: 0-1000)
- `--ip`: Target IP address (default: 127.0.0.1)
- `--send`: URL where the result will be sent (required)

## Features
- Scans specified port ranges on a given IP address.
- Utilizes Nmap for detailed scanning, including service/version detection.
- Sends scanning results to a specified URL.

## Dependencies
- Nmap
- Click
- Requests

## Configuration
No additional configuration is required beyond the installation of dependencies and usage commands.

## Examples
Scan the first 1000 ports on the local host and send results:

## Troubleshooting
Ensure Nmap is properly installed and accessible from your command line environment. For issues related to HTTP requests, verify the result URL is correct and accepting POST requests.

## Contributors
Me

## License
This project is open-sourced under the MIT License.