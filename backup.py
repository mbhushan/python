import os
import time

src = ['/home/mani/py']

dst = '/home/mani/bkup'

target = dst + os.sep + time.strftime('%Y%m%H%M%S') + '.zip'

if not os.path.exists(target):
    os.mkdir(dst)

zip_cmd = "zip -r {0} {1}".format(target, ' '.join(src))

print 'Zip Cmd is: '
print zip_cmd
print 'running ...'

if os.system(zip_cmd) == 0:
    print 'zip successful:', target
else:
    print 'Backup FAILED!'
