#!/usr/bin/env python

import onlyonce

with onlyonce.SingleProcessLock('stuff') as lock:
    print 'starting'
    lock.run(['sleep','100'])
print 'done.'
