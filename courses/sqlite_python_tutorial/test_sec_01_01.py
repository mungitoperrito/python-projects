import section_01_01 as test_target

def test_imports():
    assert hasattr(test_target, 'sqlite3')

