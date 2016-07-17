import unicodedata

def readlines(filename):
    f = open(filename)
    lines = list(filter(None, f.read().split("\n")))
    f.close()
    return lines


def stripaccents(text):
    text = text.lower().replace("ñ", "ny")
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)
