import re
#from decimal import Decimal
filename = 'setup.rpt'
Endpoint = input('Please enter a Endpoint:\n')
with open(filename) as file:
    r = file.read()
    regex = re.compile(r' +(Startpoint:\s+(\S+)+?[\s\S]+?Endpoint:\s+(\S+)[\s\S]+?Type:\s+(\S+)[\s\S]+?'
    r'delay\s\S+.+?(\S+)[\s\S]+?delay\s\S+.+?(\S+)[\s\S]+?reconvergence pessimism.+?(\S+)[\s\S]+?slack\s+\(.*?\)\s+(\S+))')
    names = regex.findall(r)

    for name in names:
        if Endpoint == name[2]:
            #print('name: '+name[0])
            print('startpoint: '+name[1])
            print('endpoint: '+name[2])
            #print('max/min: '+name[3])

            #print('delay1: '+name[4])
            a = float(name[4])
            #print('delay2: '+name[5])
            b = float(name[5])
            #print('reconvergence pessimism: '+name[6])
            c = float(name[6])
            if 'max' == name[3]:
                #res = Decimal(name[6]) + Decimal(name[5]) - Decimal(name[4])
                d =  b + c - a   #delay2 + reconvergence pessimism - delay1
                #print('max: '+name[3])
                print('max_skew:'+str(d))
            if 'min' == name[3]:
                #res = Decimal(name[4]) - Decimal(name[5]) - Decimal(name[6])
                d =  a - b - c    #delay1 - delay2 - reconvergence pessimism
                #print('min: ' + name[3])
                print('max_skew:' +str(d))
            print('violation: ' + name[7])

