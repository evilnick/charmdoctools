"""
charmdoctools metadata

tools for extracting and writing metadata from the top of docs
"""
import re
from ruamel.yaml import YAML
from io import StringIO
yaml = YAML(typ='safe')
yaml.default_flow_style = False
regex = r"<!-- METADATA\n(.*)\n-->\n*"

def get(text):
    'Extracts metadata yaml and returns a dict'
    matches = re.search(regex, text, re.DOTALL)
    if matches:
        metadata = yaml.load(matches.group(1))
    else:
        metadata = None
    return(metadata)

def put(text, data):
    'Adds dict of metadata as yaml embedded in comment at top of text'
    new_text = strip(text)
    stream = StringIO()
    yaml.dump(data, stream)
    metadata = '<!-- METADATA\n'+stream.getvalue()+'-->\n\n'
    stream.close()
    return(metadata+new_text)

def strip(text):
    'Returns text with metadata portion removed'
    new_text = re.sub(regex, '', text,1, re.DOTALL)
    return(new_text)