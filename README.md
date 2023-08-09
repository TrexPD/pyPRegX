# PyPregX [ALPHA]

#### A parser made entirely with regex to extract elements from HTML!

### Libraries used:

```re```
```html```

### Use in practice:

```
parser = ParserRegex(r"The path of your file here!")
print(parser.title())
```
##### Ouput:
```
It's FOSS
```

#### Methods:
- **.body()**  = Returns document body.
- **.head()**  = Returns all the content that is inside the ```<head>``` tag of the HTML.
- **.links()** = Extracting all the URLs found within a page's ```<a>``` tags.
- **.text()**  = Removes all html tags and preserves only the text.
- **.title()** = returns the text inside the ```</title>``` tag.

### License:

PyPregX is open-source under the [MIT License](./LICENSE).

<h2 align="center">
    <strong>🌟
        Favourite this repository!
    </strong>🌟
</h2>

<p align="center">
    Created with ❤️ and python by
    <a href="https://github.com/TrexPD"> Paulo Daniel (TrexPD)! </a>
</p> 