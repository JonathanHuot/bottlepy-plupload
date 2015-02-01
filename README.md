bottlepy-plupload
=================

Uploading multiples files using plupload js library and bottlepy as never been easier.


Setup virtualenv
=================
```
virtualenv dev
. dev/bin/activate
pip install bottle
```

Run multiple upload with plupload and bottle
=================
```
. dev/bin/activate
python bottle-example.py
```

Save uploaded files in your Python code
=================
```
from bottle import request, post
from plupload import plupload

@post('/upload')
def index():
    return plupload.save(request.forms, request.files, "/destination/folder")
```
