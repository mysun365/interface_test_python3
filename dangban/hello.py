#! encoding:utf8

def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/json')])
    return '{"code":"seccess"}'
