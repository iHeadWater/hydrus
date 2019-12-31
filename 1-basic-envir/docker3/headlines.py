# headlines.py

import parse
from reader import feed

tutorial = feed.get_article(0)
headlines = [
    r.named["header"]
    for r in parse.findall("\n## {header}\n", tutorial)
]
print("\n".join(headlines))