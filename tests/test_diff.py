import pytest

from charmdoctools.diff import diff_docs,source_to_text


def test_diff_files():
    assert diff_docs("test_file_1.txt","test_file_2.txt") == {
        "charm_name": "etcd",
        "charm_source": "https://github.com/charmed-kubernetes/layer-etcd",
        "docs": "https://discourse.charmhub.io/t/charm-etcd-docs-index/5592",
    }
    assert get("Text with\nno metadata") == None


