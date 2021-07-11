"""Needed for adding src directory in python path."""
import os.path as op
import sys
ROOTDIR = op.dirname(op.abspath(__file__))
try:
    sys.path.remove(ROOTDIR)
except ValueError:
    pass
sys.path.insert(0, op.join(ROOTDIR, 'src'))
