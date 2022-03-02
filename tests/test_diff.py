import pytest

from charmdoctools.diff import diff_docs,source_to_text


def test_diff_files():
    result =  list(diff_docs("test_file_1.txt","test_file_2.txt"))
    
    assert result == [
        '--- test_file_1.txt\n',
        '+++ test_file_2.txt\n',
        '@@ -8,7 +8,7 @@\n',
        ' l',
        ' e',
        ' _',
        '-1',
        '+2',
        ' .',
        ' t',
        ' x',
    ]
    assert len(result) == 11


