#!/bin/python

import sys


time = raw_input().strip()
sections = time.split(':')
if sections[0] == '12' and sections[2][-2:] == 'AM':
    print '00'+ ':' + sections[1] + ':' + sections[2][:2]
elif sections[0] == '12' and sections[2][-2:] == 'PM':
    print '12'+ ':' + sections[1] + ':' + sections[2][:2]
elif (sections[2][-2:] == 'PM'):
    print str(int(sections[0]) + 12).zfill(2) + ':' + sections[1] + ':' + sections[2][:2]
else:
    print time[:-2]
