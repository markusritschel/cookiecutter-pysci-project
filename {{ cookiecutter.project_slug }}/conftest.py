import pytest


@pytest.fixture(autouse=True)
def add_pytest_to_doctest_namespace(doctest_namespace):
    """Inject pytest into the doctest namespace so `pytest.skip()`
    properly aborts illustrative docstring examples as skipped."""
    doctest_namespace["pytest"] = pytest
