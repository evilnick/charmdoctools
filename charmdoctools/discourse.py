""" Functions to deal with markdown in discourse wiki posts"""

import requests
import click

def get_raw_url(url):
    r = url.split('/')
    r = r[0]+'//'+r[2]+'/raw/'+r[-1]
    return(r)  

def get_md(url):
    u = get_raw_url(url)
    print('fetching \u001b[36m{} \u001b[0m'.format(url))
    try:
        content = requests.get(url)
    except:
        print("Error fetching url:",url)
        exit(1)
    if (content.status_code != 200):
        print("Error fetching url:",url)
        exit(1)
    return(content.content)