from re import findall


def search_for_title_in_HTML(content_html: str) -> list | None:
    """
    returns the text inside the <title> tag.
    """
    pattern: str = r'<title>(.*?)</title>'
    return findall(pattern, content_html)[0]