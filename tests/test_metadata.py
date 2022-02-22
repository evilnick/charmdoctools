import pytest

from charmdoctools.metadata import get, strip, put

test_str= ("<!-- METADATA\n"
     "charm_name: etcd\n"
     "charm_source:  https://github.com/charmed-kubernetes/layer-etcd\n"
     "docs: https://discourse.charmhub.io/t/charm-etcd-docs-index/5592\n"
     "-->\n\n"
     "Etcd is a highly available distributed key value store that provides a reliable\n"
     "way to store data across a cluster of machines. Etcd gracefully handles master\n"
     "elections during network partitions and will tolerate machine failure,\n"
     "including the master.\n")
test_stripped = ("Etcd is a highly available distributed key value store that provides a reliable\n"
     "way to store data across a cluster of machines. Etcd gracefully handles master\n"
     "elections during network partitions and will tolerate machine failure,\n"
     "including the master.\n")
test_alt = ("<!-- METADATA\n"
     "charm_name: Etcd\n"
     "charm_source: example.com\n"    
     "-->\n\n"
     "Etcd is a highly available distributed key value store that provides a reliable\n"
     "way to store data across a cluster of machines. Etcd gracefully handles master\n"
     "elections during network partitions and will tolerate machine failure,\n"
     "including the master.\n")
test_alt_meta = {'charm_name': 'Etcd', 'charm_source': 'example.com'}

def test_metadata_get():
    assert get(test_str) == {'charm_name': 'etcd', 'charm_source': 'https://github.com/charmed-kubernetes/layer-etcd', 'docs': 'https://discourse.charmhub.io/t/charm-etcd-docs-index/5592'}
    assert get("Text with\nno metadata") == None

def test_metadata_put():
    assert put(test_str, test_alt_meta) == test_alt
    assert put(test_stripped, test_alt_meta) == test_alt

def test_metadata_strip():
    assert strip(test_str) == test_stripped
    assert strip("Text with\nno metadata") == "Text with\nno metadata"