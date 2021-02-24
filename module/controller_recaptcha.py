# coding=UTF-8
import requests
import json
import time
import logging 
import threading
from datetime import datetime
from flask import Flask, Response, render_template, request, redirect, jsonify, send_from_directory, url_for, make_response
from threading import Timer,Thread,Event
import const
from flask_restful import Resource
import log as logpy
from urllib.parse import urlencode
from urllib.request import urlopen

log = logpy.logging.getLogger(__name__)

# https://stackoverflow.com/questions/46393162/how-to-validate-a-recaptcha-response-server-side-with-python
# https://codesandbox.io/s/n3p4y?file=/src/App.vue

def setup_route(api):
    api.add_resource(Recaptcha, '/recaptcha')

class Recaptcha(Resource):
    def post(self):
        log.info(request.data)
        URIReCaptcha = 'https://www.google.com/recaptcha/api/siteverify'
        recaptchaResponse = json.loads(request.data).get('g-recaptcha-response', None)
        private_recaptcha = '6LellmQaAAAAAL705D1E8DkgNDHId8P0PFydI-Or'
        remote_ip = request.remote_addr
        params = urlencode({
            'secret': private_recaptcha,
            'response': recaptchaResponse,
            'remote_ip': remote_ip,
        })
        log.info(params)
        data = urlopen(URIReCaptcha, params.encode('utf-8')).read()
        result = json.loads(data)
        log.info(result)
        success = result.get('success', None)

        if success == True:
            log.info('reCaptcha passed')
        else:
            log.info('recaptcha failed')
