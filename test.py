import nltk
import sys,re
import nltk
from collections import defaultdict
import cfg_fix
from cfg_fix import parse_grammar, CFG
from pprint import pprint
# The printing and tracing functionality is in a separate file in order
#  to make this file easier to read
from cky_print import CKY_pprint, CKY_log, Cell__str__, Cell_str, Cell_log


mylist = {"123","432","235","sdf"}
mylist.pop()
mylist.pop()
print mylist