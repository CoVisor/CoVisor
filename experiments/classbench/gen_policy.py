#!/usr/bin/python
import sys
import subprocess
import time
import random


def generatePolicy(paraFile, ruleCount):
    cmd = './db_generator -bc %s %d 2 -0.5 0.1 tttemp >/dev/null 2>&1' % (paraFile,
        ruleCount + 20)
    subprocess.call(cmd, shell=True)

    outFile = '%s_%d' % (paraFile.split('/')[1].split('_')[0], ruleCount)
    cmd = 'head -n -20 tttemp > %s' % outFile
    subprocess.call(cmd, shell=True)

    subprocess.call('rm tttemp', shell=True)

def generateSubnets(policyFile):
    subnets = set()
    fin = open(policyFile, 'r')
    oneline = fin.readline()
    while oneline != "":
        temp = oneline.strip().split()
        subnets.add(temp[0][1:])
        subnets.add(temp[1])
        oneline = fin.readline()
    fin.close()
    if '0.0.0.0/0' in subnets:
        subnets.remove('0.0.0.0/0')
    print len(subnets)
    #subnets = list(subnets)

    fout = open(policyFile.split('_')[0] + '_prefix', 'w')
    for subnet in subnets:
        fout.write(subnet + '\n')
    fout.close()

def generateAll():
    paraFile = 'parameter_files/acl1_seed'
    for i in [100, 200, 300, 400, 500]:
        generatePolicy(paraFile, i)
        #generateSubnets('%s_%d' % (paraFile.split('/')[1].split('_')[0], i))
    # prefix
    generatePolicy(paraFile, 2000)
    generateSubnets('%s_%d' % (paraFile.split('/')[1].split('_')[0], 2000))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print '\tgen_policy.py policy paraFile ruleCount'
        print '\tgen_policy.py prefix policyFile'
        sys.exit()

    if sys.argv[1] == 'all':
        generateAll()
    elif sys.argv[1] == 'policy':
        generatePolicy(sys.argv[2], int(sys.argv[3]))
    else:
        generateSubnets(sys.argv[2])

