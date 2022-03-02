"""
charmdoctools diff

This wraps some functions to diff different versions of docs.

Primarily, this is intended to check a local version against a 
version stored elsewhere
"""

import validators
import os
import difflib
from charmdoctools.metadata import get, strip, put


def source_to_text(src) -> list:
    """Checks supplied string to see if it is a url, local file etc, and return the appropriate text from that location"""
    text = list()
    if os.path.exists(src):
        """supplied arg is a filename"""
        with open(src) as f:
            text = f.readlines()
    elif validators.url(src):
        pass

    return text

def diff_docs(file1, file2):
    text1 = source_to_text(file1)
    text2 = source_to_text(file2)
    outlines = list(difflib.unified_diff(file1,file2,fromfile=file1,tofile=file2))
    return(outlines)

