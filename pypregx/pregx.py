from pypregx.title_regex import search_for_title_in_HTML


class ParserRegex():
    def __init__(self, file_path: str):
        with open(file_path, "rt", encoding="utf-8") as file:
            self.content = file.read()

    def title(self):
        return search_for_title_in_HTML(self.content)
    



if __name__ in "__main__":
    parser = ParserRegex(r"C:\Users\leyna\Desktop\meupdf.html")
    print(parser.title())