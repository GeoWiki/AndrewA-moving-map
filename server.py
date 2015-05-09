#!/usr/bin/python3
# -*- coding: utf-8 -*-
from bottle import route, run, static_file, template

@route('/')
def server_static():
    return template('./html/main_page.html')

@route('/leaflet_control/')
def server_static():
    return template('./html/leaflet_control.html')

@route('/ne/')
def server_static():
    return template('./html/ne_index.html')

@route('/slider/')
def server_static():
    return template('./html/slider.html')

@route('/slider2/')
def server_static():
    return template('./html/slider2.html')

@route('/json/test2')
def server_static():
    return static_file('data2.json', root = './')

@route('/leaflet/js')
def leaflet_js():
    return static_file('leaflet.js', root = './html/')

@route('/leaflet/css')
def leaflet_css():
    return static_file('leaflet.css', root = './html/')

@route('/test2/')
def static():
    return static_file('data.json', root = './')

@route('/json')
def json():
    return static_file('data.json', root = './')

@route('/json/ne/<file:path>')
def return_json(file):
    return static_file(file, root = './ready_json/NE/')

run(host='localhost', port=8811, debug=True)