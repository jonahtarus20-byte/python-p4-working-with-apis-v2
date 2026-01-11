
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from open_library_api import Search
import json

def test_get_search_results():
    """Test that get_search_results returns bytes"""
    search = Search()
    result = search.get_search_results()
    assert isinstance(result, bytes)
    assert b'title":"The Lord of the Rings"' in result
    assert b'author_name":["J.R.R. Tolkien"]' in result

def test_get_search_results_json():
    """Test that get_search_results_json returns a dict"""
    search = Search()
    result = search.get_search_results_json()
    assert isinstance(result, dict)
    assert 'docs' in result
    assert len(result['docs']) == 1
    assert result['docs'][0]['title'] == "The Lord of the Rings"
    assert result['docs'][0]['author_name'] == ["J.R.R. Tolkien"]

def test_get_user_search_results():
    """Test that get_user_search_results returns formatted string"""
    search = Search()
    result = search.get_user_search_results("the lord of the rings")
    assert isinstance(result, str)
    assert "Title: The Lord of the Rings" in result
    assert "Author: J.R.R. Tolkien" in result
