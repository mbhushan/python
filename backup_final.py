import os
import time

src_dir = ['/home/mani/py']

dst_dir = '/home/mani/pybkup'

if not os.path.exists(dst_dir):
    os.mkdir(dst_dir)

today = dst_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = raw_input('Enter a comment ---->')

if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ','_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory: ', today

zip_cmd = "zip -r {0} {1}".format(target, ' '.join(src_dir))

print 'zip cmd is: ', zip_cmd
print 'running ...'
if os.system(zip_cmd) == 0:
    print 'successful backup to: ', target
else:
    print 'BACKUP FAILURE!'

