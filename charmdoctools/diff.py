"""
charmdoctools diff

This wraps some functions to diff different versions of docs.

Primarily, this is intended to check a local version against a 
version stored elsewhere
"""

from charmdoctools.metadata import get, strip, put

def diff_local_vs_discourse(local_file):
    with open(local_file) as f:
        text = f.readlines()
    metadata = get(text)
    