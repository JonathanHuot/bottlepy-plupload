from bottle import run
from bottle import get, post, view


@get('/')
def home():
    from bottle import redirect
    redirect('/upload')


@get('/plupload/js/<filename:path>')
def send_plupload(filename):
    from bottle import static_file
    return static_file(filename, root='plupload/js')


@get('/upload')
@view('upload.tpl')
def index():
    return {}


@post('/upload')
def index():
    from bottle import request
    import os
    import plupload
    return plupload.save(request.forms, request.files, os.getcwd())


run(host='localhost', port=8080, debug=True)

