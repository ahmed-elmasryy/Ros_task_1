import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ahmed-elmasry/ws1/src/pkg_1/install/pkg_1'
