#!/usr/bin/python


import argparse
import os
import subprocess
import sys




class bcolors:
    INFO      = '\033[1;34m'  # blue
    OK        = '\033[32m'  # green
    WARNING   = '\033[31m'  # red
    ENDC      = '\033[0m'

env = dict(os.environ)   # Make a copy of the current environment


parser = argparse.ArgumentParser(description='Set environment variables for make.')
parser.add_argument('--env', default='devel', help="Sets server execution environment", action="store", choices=['devel', 'deploy-qa', 'qa', 'prod'])
parser.add_argument('--hostname', help="Sets the remote host, for automated tests using the network", action="store")
parser.add_argument('--port', type=int, help="Sets the port for the server API", action="store")
parser.add_argument('--mongo-path', help="Sets the mongo database, for automated tests", action="store")
parser.add_argument('--skip-login', help="Allows access to services without logging in", action="store_true")
parser.add_argument('--debug', help="Runs mocha for the target in debug mode", action="store_true")
parser.add_argument('--debug-port', type=int, help="Sets the port for node-inspector", action="store")
parser.add_argument('--local-only', help="Runs the server in local-only mode, for automated tests without the network", action="store_true")
parser.add_argument('make_args', help="the args to pass to make", nargs=argparse.REMAINDER)
args = parser.parse_args()

if (args.env):
    env['SERVER_ENV'] = args.env
else:
    env['SERVER_ENV'] = 'devel'
color = bcolors.OK if (env['SERVER_ENV'] == 'prod') else bcolors.INFO
print('Setting server environment to ' + color + env['SERVER_ENV'] + bcolors.ENDC)

if (args.hostname):
    env['HOSTNAME'] = str(args.hostname)
    print('Setting hostname to ' + bcolors.OK + env['HOSTNAME'] + bcolors.ENDC)

if (args.port):
    env['PORT'] = str(args.port)
    if (env['SERVER_ENV'] == 'prod'):
        color = bcolors.OK if (env['PORT'] == '80') else bcolors.WARNING
        print('Resetting server port to default for production: ' + color + str(env['PORT']) + bcolors.ENDC)
    else:
        print('Setting port to ' + bcolors.OK + env['PORT'] + bcolors.ENDC)


if (args.skip_login):
    env['SKIP_LOGIN'] = 'true'
    print(bcolors.WARNING + 'Allowing access to services without login' + bcolors.ENDC)
else:
    print(bcolors.OK + 'Requiring login to access services' + bcolors.ENDC)

if (args.debug or args.debug_port):
    env['NODE_ARGS']  = '--debug-brk'
    env['MOCHA_ARGS'] = '--debug-brk --timeout 1000000'
    if (args.debug_port):
        env['NODE_ARGS']  += ' --debug=' + str(args.debug_port)
        print(bcolors.WARNING + 'Will run in node-inspector at port ' + str(args.debug_port) + bcolors.ENDC)
    else:
        print(bcolors.WARNING + 'Will run in node-inspector' + bcolors.ENDC)
else:
    env['NODE_ARGS']  = ''
    env['MOCHA_ARGS'] = ''

if (args.local_only):
    env['LOCAL_ONLY'] = 'true'
    print(bcolors.WARNING + 'Will run in local-only mode (without the network)' + bcolors.ENDC)



cmd = ['make', '--file', 'Makefile.app'] + args.make_args
print('cmd=' + str(cmd))
p = subprocess.Popen(cmd, env=env)
p.wait();

sys.exit(0)
