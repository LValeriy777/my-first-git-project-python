import pytest
from src.utils import read_json_file
from typing import Any

def test_read_json_file_valid() -> None:
    data = read_json_file("valid.json")
    assert isinstance(data, list)
    assert len(data) > 0

def test_read_json_file_invalid() -> None:
    empty_data = read_json_file("empty.json")
    assert empty_data == []

def test_read_json_file_nonexistent() -> None:
    nonexistent_data = read_json_file("nonexistent.json")
    assert nonexistent_data == []
