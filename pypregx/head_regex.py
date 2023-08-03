from re import findall, DOTALL


def extract_the_head_from_HTML(content_html: str) -> list | None:
    """
    Returns all the content that is inside the <head> tag of the HTML.
    """
    pattern: str = r'(<head\b[^>]*>.*?</head>)'
    return findall(pattern, content_html, flags=DOTALL)[0]