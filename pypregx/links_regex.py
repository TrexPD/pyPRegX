from re import findall, DOTALL


def search_for_links_in_HTML(content_html: str) -> list | None:
    """
    Extracting all the URLs found within a page's <a> tags.
    """
    pattern: str = r'<a\s+href=[\'"](.*?)[\'"].*?>'
    return findall(pattern, content_html, flags=DOTALL)