# pylint: disable-all
import pytest
import webbrowser

chrome_path = "/usr/bin/google-chrome %s"
browser = None


@pytest.fixture(scope="module")
def setup():
    print("starting browser...")
    global browser
    browser = webbrowser.get(chrome_path)
    yield browser
    print("closing browser...")


def test_web1(setup):
    browser.open("https://www.google.com")
    print("Test 1 executed successfully...")


def test_web2(setup):
    browser.open("https://www.geeksforgeeks.com")
    print("Test 2 executed successfully...")
