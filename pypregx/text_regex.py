from re import compile, DOTALL, sub
from html import unescape


def extract_only_the_HTML_text(content_html: str, file_name: str = "text_extract.txt", save_file: bool = False) -> str | None:
    """
    Removes all html tags and preserves only the text.
    """
    content_html = sub(r"<script\b[^>]*>(.*?)</script>", "", content_html, flags=DOTALL)
    
    content_html = sub(r"<style\b[^>]*>(.*?)</style>", "", content_html, flags=DOTALL)

    content_html = unescape(content_html)
    
    string = compile(r"<[^<>]*>").sub(" ", content_html)
    string = " ".join(string.split())
    if save_file:
        with open(f'{file_name}.txt', 'wt', encoding='utf-8') as file:
            file.write(string)
    return string