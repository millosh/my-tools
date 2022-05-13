"""
Skeleton for my new programs, <2022-05-13 Fri 13:53>
"""

import re, time, pickle, sys, os
from subprocess import getoutput as go
from os.path import *

def exec_cmd(cmd,torun,toprint,togo):
    ret = False
    if toprint:
        print(cmd)
    if torun:
        if togo:
            ret = go(cmd)
        else:
            ret = os.system(cmd)
    return ret

def get_arg(arg,args):
    value = False
    if arg in sys.argv:
        index = sys.argv.index(arg)
        if len(sys.argv) > index+1:
            value = sys.argv[index+1]
            arg = re.sub("^\-+","",arg)
        else:
            sys.exit("No value for argument '" + arg + "', no fun!")
    args[arg] = value
    return args

def get_args():
    # args and data
    args = {}
    data = {}

    # timestamps
    args['gmtime'] = time.gmtime()
    args['timestamp'] = time.mktime(time.gmtime())
    args['date'] = time.strftime("%Y-%m-%d",args['gmtime'])
    args['start time'] = time.strftime("%Y-%m-%d %H:%M:%S",args['gmtime'])
    
    # directories and logs
    args = get_arg('--root-dir')
    if not args['root-dir']:
        args['root-dir'] = "."
    if not exists(args['root-dir']):
        os.mkdir(args['root-dir'])
    args = get_arg('--logs-dir',args)
    if not args['logs-dir']:
        args['logs-dir'] = args['root-dir'] + "/logs"
    if not exists(args['logs-dir']):
        os.mkdir(args['logs-dir'])
    args = get_arg('--log-file',args)
    if not args['log-file']:
        args['log-file'] = args['logs-dir'] + '/basic.log'
    args = get_arg('--error-file',args)
    if not args['error-file']:
        args['error-file'] = args['logs-dir'] + '/errors.log'
    args = get_arg('--data-dir',args)
    if not args['data-dir']:
        args['data-dir'] = args['root-dir'] + "/data"
    if not exists(args['data-dir']):
        os.mkdir(args['data-dir'])
    
    # general
    args = get_arg('--command',args)
    if not args['command']:
        sys.exit("No command, no fun!")

    return args, data

def main():
    args, data = get_args()
    if args['command'] == 'our-command':
        # python basic.py --command our-command
        # call subroutines here
        pass
    elif args['command'] == 'another-command':
        # python basic.py --command another-command
        # call subroutines here
        pass
    else:
        sys.exit("No valid command, no fun!")

if __name__ == "__main__":
    main()
