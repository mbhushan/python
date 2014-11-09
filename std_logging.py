import os, platform, logging
#import platform
#import logging

if platform.platform().startswith("Windows"):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'py/python/test.log')

print 'logging to: ', logging_file

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug("start of the manibhushan program")
logging.info("Doing python programming - ie something useful")
logging.warning("program is going to DIE")
