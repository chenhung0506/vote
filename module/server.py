# -*- coding: utf-8 -*-
from flask import Flask
# from flask_cors import CORS
import log as logpy
import re
import os
import const
import controller
import controller_sso
import controller_recaptcha
#import controller_ccui
import flask_restful
import utils
import json
import service
from flask_cors import CORS, cross_origin
from flask_restful import Api
from flask_restful import Resource
from datetime import datetime
from flask import Flask, request, render_template, send_from_directory
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

utils.setLogFileName()
log = logpy.logging.getLogger(__name__)
# setting for render_template
template_dir = os.path.abspath('./resource/customized/')
app = Flask(__name__, template_folder=template_dir)
api = Api(app)
controller.setup_route(api)
controller_sso.setup_route(api)
controller_recaptcha.setup_route(api)
# setting for send_from_directory
app.static_folder = os.path.abspath("resource/customized/")
app.static_url_path = os.path.abspath("resource/customized/")
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


# @app.route('/static/<path:filename>', methods=['GET'])
# @cross_origin()
# def serve_static(filename):
#     root_dir = os.path.dirname(os.getcwd())
#     return send_from_directory(os.path.join(root_dir, 'static', 'js'),   filename)       


if __name__=="__main__":
    # utils.setLogFileName()
    try:
        if not os.path.exists("./data_for_KG/"):
            os.makedirs("./data_for_KG/")
    except OSError as e:
        log.info(e)
    sched = BackgroundScheduler()
    sched.start()
    sched.add_job(utils.setLogFileName, CronTrigger.from_crontab('59 23 * * *'))
    # controller.transmitProcess(None)
    # sched.add_job(controller.transmitProcess, CronTrigger.from_crontab(const.TRANSMIT_CRON), [None])
    app.run(host="0.0.0.0", port=const.PORT, debug=True, use_reloader=False)