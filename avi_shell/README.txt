AVI CLI Shell Client

## Usage

    usage: avi_shell [-h] [--address ADDRESS] [--batch-mode] [--min-output]
                       [--local] [--debug] [--file FILE] [--json]
                       [--password PASSWORD] [--token TOKEN] [--tenant TENANT]
                       [--user USER] [--log LOG] [--server] [--port PORT]

    optional arguments:
        -h, --help           show this help message and exit
        --address ADDRESS    Address of the REST API server
        --batch-mode
        --min-output
        --local              local shell login procedure
        --debug
        --file FILE          Execute the CLI commands from this file
        --json
        --password PASSWORD  Password for the REST API server
        --token TOKEN        Token for the REST API server
        --tenant TENANT
        --user USER          Username for the REST API server
        --log LOG            Log file name
        --server             Use a client server model for CLI
        --port PORT          Listening port for the CLI server


## Examples

CLI Client for AVI ADC:

    $avi_shell --address X.X.X.X --user admin --password admin

The `--address` option is necessary here because we are connecting shell client to any of our remote controllers.

New Version Commands

## License
The MIT License (MIT)

Avi Shell CLI Client -- a cli client for Avi CLI.
Copyright (C) 2015 anpartha@avinetworks.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE

