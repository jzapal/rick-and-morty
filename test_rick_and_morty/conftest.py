import pytest


@pytest.fixture(autouse=True)
def mock_page_size(monkeypatch):
    monkeypatch.setattr('settings.settings.PAGE_SIZE', 10)
