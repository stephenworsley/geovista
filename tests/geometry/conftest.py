"""pytest fixture infra-structure for :mod:`geovista.geometry` unit-tests."""

import pytest


@pytest.fixture(params=["110m", "50m", "10m"])
def resolution(request):
    """Fixture for testing each of the Natural Earth coastline resolutions."""
    return request.param