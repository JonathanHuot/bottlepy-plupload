import os


def _jsonrpc(value="error", *a, **ka):
    base = {"jsonrpc": "2.0", value: None, "id": "id"}
    if a or ka:
        base[value] = {}.update(*a, **ka)
    return base


def save(forms, files, dest):
    if "name" in forms:
        filename = forms["name"]
    elif len(files) > 0:
        filename = files.file.filename
    else:
        return _jsonrpc("error", code=102, message="Filename must be present")

    if "chunk" in forms and "chunks" in forms:
        chunk = int(forms["chunk"])
        total = int(forms["chunks"])
    else:
        chunk = 0
        total = 1

    first = chunk == 0
    last = chunk == total - 1

    try:
        destfile = os.path.join(dest, filename)
        if os.access(destfile, os.F_OK):
            return _jsonrpc("error", code=102, message="File already uploaded")

        tmpfile = os.path.join(dest, "{0}.part".format(filename))
        with open(tmpfile, "w+b" if first else "ab") as fd:
            files.file.save(fd)

        if last:
            os.rename(tmpfile, destfile)
    except:
        return _jsonrpc("error", code=101, message="Failed to write file.")
    return _jsonrpc("result")
