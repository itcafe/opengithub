#%% 文字列からjson文字列を抽出
from json import JSONDecoder
def findall_jsonstring(text, decoder=JSONDecoder()):
    """Find JSON objects in text, and yield the decoded JSON data

    Does not attempt to look for JSON arrays, text, or other JSON types outside
    of a parent JSON object.

    """
    pos = 0
    while True:
        match = text.find('{', pos)
        if match == -1:
            break
        try:
            result, index = decoder.raw_decode(text[match:])
            yield {"result": result, "start": match, "strcount": index}
            pos = match + index
        except ValueError:
            pos = match + 1


def findfirst_jsonstring(text, decoder=JSONDecoder()):
    """Find JSON objects in text, and yield the decoded JSON data

    Does not attempt to look for JSON arrays, text, or other JSON types outside
    of a parent JSON object.

    """
    pos = 0
    match = text.find('{', pos)
    if match == -1:
        return {}
    try:
        # jsonペアができている結果とその文字数を返却
        result, index = decoder.raw_decode(text[match:])
        return {"result": result, "start": match, "strcount": index}
    except ValueError:
        print(ValueError)
        return {}
