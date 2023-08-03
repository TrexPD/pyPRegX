from re import findall, DOTALL


def search_for_body_in_HTML(content_html: str) -> list | None:
    """
    Returns document body.
    """
    pattern: str = r'(<body\b[^>]*>.*?</body>)'
    return findall(pattern, content_html, flags=DOTALL)[0]