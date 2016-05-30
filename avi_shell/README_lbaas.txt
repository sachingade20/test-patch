AVI CLI Shell Client

## Usage

    usage: avi_lbaas [-h] [--batch-mode] [--min-output] [--local] [--debug]
                 [--file FILE] [--json] [--log LOG]
                 [--os-username <auth-user-name>]
                 [--os-password <auth-password>]
                 [--os-tenant-name <auth-tenant-name>]
                 [--os-tenant-id <tenant-id>] [--os-auth-url <auth-url>]
                 [--os-region-name <region-name>]

    optional arguments:
        -h, --help            show this help message and exit
        --batch-mode
        --min-output
        --local               local shell login procedure
        --debug
        --file FILE           Execute the CLI commands from this file
        --json
        --log LOG             Log file name
        --os-username <auth-user-name>
                        Name used for authentication with the OpenStack
                        Identity service. Defaults to env[OS_USERNAME].
        --os-password <auth-password>
                        Password used for authentication with the OpenStack
                        Identity service. Defaults to env[OS_PASSWORD].
        --os-tenant-name <auth-tenant-name>
                        Tenant to request authorization on. Defaults to
                        env[OS_TENANT_NAME].
        --os-tenant-id <tenant-id>
                        Tenant to request authorization on. Defaults to
                        env[OS_TENANT_ID].
        --os-auth-url <auth-url>
                        Specify the Identity endpoint to use for
                        authentication. Defaults to env[OS_AUTH_URL].
        --os-region-name <region-name>
                        Specify the region to use. Defaults to
                        env[OS_REGION_NAME].


## Examples

CLI Client for AVI ADC:

    $ source openstack_credentials.txt
    $ avi_lbaas


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

