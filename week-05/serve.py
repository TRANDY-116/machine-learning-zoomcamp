#!/usr/bin/env python
from waitress import serve
from predict import app

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=9696)