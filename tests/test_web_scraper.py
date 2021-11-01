from web_scraper import __version__

from web_scraper.scraper import get_citations_needed_count,get_citations_needed_report
def test_version():
    assert __version__ == '0.1.0'

def test_get_citations_needed_count():
    url = "https://en.wikipedia.org/wiki/History_of_India"
    expected=5
    actual = get_citations_needed_count(url)
    assert  actual == expected
    
    
def test_get_citations_needed_report():
    url = "https://en.wikipedia.org/wiki/History_of_India"
    expected="the sentence is too long and contain a lot of spaces"
    actual=get_citations_needed_report(url)
    assert actual == expected
        
       