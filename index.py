import pytest
import sys

if __name__ == '__main__':
    # Run pytest on 'Test.py' with verbose output
    # sys.exit ensures the script returns a proper error code to the OS if tests fail
    sys.exit(pytest.main(["-v", "tests.py"]))