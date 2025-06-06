"""Unit tests for hello module."""
from hello import add

def test_add():
    """Test something in hello."""
    assert add(2, 3) == 5
    assert add(5, 5) == 10
    print("All test cases passed")
