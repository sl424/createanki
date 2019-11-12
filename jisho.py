from urllib.parse import quote
import json
import os
import requests

# TODO: make this configurable I guess
cachedir = os.path.expanduser("~/.cache/jisho/")
if not os.path.exists(cachedir):
    os.makedirs(cachedir)

def jisho_get(kanji, tags=[]):
    tags = " ".join(tags)
    cache = os.path.join(cachedir, f"{kanji} {tags}.json")
    if os.path.exists(cache):
        with open(cache) as f:
            return json.load(f)
    r = requests.get("https://jisho.org/api/v1/search/words" +
        f"?keyword={kanji} {quote(tags)}")
    if r.status_code != 200:
        raise Exception("jisho returned " + r.text)
    with open(cache, "w") as f:
        f.write(r.text)
    return r.json()
