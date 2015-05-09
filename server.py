# -*- coding: utf-8 -*-
from bottle import route, run, static_file, template

@route('/')
def server_static():
    return template('./html/main_page.html')

@route('/leaflet_control/')
def server_static():
    return template('./html/leaflet_control.html')


@route('/slider/')
def server_static():
    return template('./html/slider.html')

@route('/leaflet/js')
def leaflet_js():
    return static_file('leaflet.js', root = './html/')

@route('/leaflet/css')
def leaflet_css():
    return static_file('leaflet.css', root = './html/')

@route('/json')
def json():
    return static_file('data.json', root = './')



run(host='localhost', port=8811, debug=True)