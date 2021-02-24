# coding=UTF-8
import requests
import json
import time
import re
import ast
import logging
import os
import math
import time
import ctypes 
import threading
from datetime import datetime
from flask import Flask, Response, render_template, request, redirect, jsonify, send_from_directory, url_for, make_response
from threading import Timer,Thread,Event
import dao
import const
from flask_restful import Resource
import log as logpy
import pymysql
import service
import service_sso
import utils
from datetime import datetime

log = logpy.logging.getLogger(__name__)

def setup_route(api):
#    api.add_resource(Default, '/customized/')
    api.add_resource(Content_to_chat_call_records, '/customized/ChatCallRecords')
    api.add_resource(TestPageForChatCallRecords, '/customized/test')
    api.add_resource(Default, '/customized/chat/')
    api.add_resource(HealthCheck, '/healthCheck')
    api.add_resource(Transmit, '/transmit')
    api.add_resource(GetChatRecords, '/getChatRecords')
    api.add_resource(Chat, '/customized/chat')
    api.add_resource(Tag, '/customized/tag')
    api.add_resource(GetEnterCCbotUrl, '/customized/getEnterCCbotUrl')
    api.add_resource(StaticResource, '/customized/<path:filename>')
    api.add_resource(FTP_test, '/FTP_test')
    api.add_resource(GetOptions, '/vote/getOptions')
    api.add_resource(GetBallots, '/vote/getBallots')

class StaticResource(Resource):
    def get(self, filename):
        # root_dir = os.path.dirname(os.getcwd())
        # return send_from_directory( os.path.join(root_dir,'static'), filename)
        log.info(filename)
        return send_from_directory('./resource/customized',  filename )

class GetOptions(Resource):
    def post(self):
        data = dao.Database().queryOptions()
        log.info(data)
        return {"data":data, "status": 200, "message":"success"}, 200

class GetBallots(Resource):
    def post(self):
        data = dao.Database().queryBallots()
        log.info(data)
        return {"data":data, "status": 200, "message":"success"}, 200

class FTP_test(Resource):
    def get(self):
        records=["123","123","123"]
        csvfile=[records,records]
        filePath = const.SFTP_UPLO_PATH + "test.csv"
        utils.exportCsv(filePath, csvfile)
        total_file = [filePath]
        log.debug(str(const.IS_FTP_UPLOAD))
        if str(const.IS_FTP_UPLOAD)=='true':
            log.debug('use ftp upload')
            utils.ftpUpload(total_file)
        else:
            log.debug('use sftp upload')
            utils.sftpUpload(total_file)
        log.info('process complete')
        return 'process complete'

class Content_to_chat_call_records(Resource):
    log.debug('Content_to_chat_call_records')

    def post(self):
        session_id = request.form.get('session_id', None)

#        if session_id is None:
#            log.info('session_id is empty.')
#        else:
#            log.info(session_id)

        pid = request.form.get('pid', None)

        if pid is None:
            log.error('Content_to_chat_call_records(): pid is None.')
            resp = make_response('Content_to_chat_call_records(): pid is None.')
            resp.headers['Cache-Control'] = 'no-store'
            resp.headers['Expires'] = 'Fri, 12 Jan 2001 0:0:0 GMT'
            return resp

        account = const.LEAST_AUTH_USERNAME
        password = const.LEAST_AUTH_PASSWORD
        callApi_sso = service_sso.CallApi()
        token = callApi_sso.get_auth_token(account, password)

        if session_id is None or len(session_id) != 36:
            campa_id = request.form.get('campa_id', None)

            server = 'http://' + const.EXTERNAL_IP
#            server = 'http://127.0.0.1:8000'#

            callApi_sso = service_sso.CallApi()
            ts = datetime.strftime(datetime.utcnow(), "%s")
            enc = callApi_sso.encrypt_aes_ecb(pid, ts)

            if campa_id is None:
#                log.info('pid = ' + pid)#
                url = server + '/ccbot/#/call-in?tokenInfo=' + token + '&pid=' + enc + '&ts=' + ts
            else:
#                log.info('pid = ' + pid + ', campa_id = ' + campa_id)#
                url = server + '/ccbot/#/call-in?tokenInfo=' + token + '&pid=' + enc + '&campa_id=' + campa_id + '&ts=' + ts

#            html = '<html><head><meta http-equiv="Pragma" content="no-cache"/>' \
#                '<meta http-equiv="expires" content="Fri, 12 Jan 2001 0:0:0 GMT"/>' \
#                '<meta http-equiv="Refresh" content="0; URL=' + url + '"/></head></html>' \
#                '<head></head></html>'
            html = url

#            resp = make_response(redirect(url))
            resp = make_response(html)
            resp.headers['Cache-Control'] = 'no-store'
            resp.headers['Expires'] = 'Fri, 12 Jan 2001 0:0:0 GMT'
            return resp
        else:
            server = 'http://' + const.EXTERNAL_IP
#            server = 'http://127.0.0.1:8330'#
            url = server + '/customized/chat/#/?callID=' + session_id

#            html = '<html><head><meta http-equiv="Pragma" content="no-cache"/>' \
#                '<meta http-equiv="expires" content="Fri, 12 Jan 2001 0:0:0 GMT"/>' \
#                '<meta http-equiv="Refresh" content="0; URL=' + url + '"/></head>' \
#                '<body onload="javascript:window.location.href="' + url + '";">' \
#                '<script>window.onload = function(){window.location.href = "' + url + '";}</script></body></html>'
            html = url

#            resp = make_response(redirect(url))
            resp = make_response(html)
            resp.headers['Cache-Control'] = 'no-store'
            resp.headers['Expires'] = 'Fri, 12 Jan 2001 0:0:0 GMT'
            return resp

class TestPageForChatCallRecords(Resource):
    def get(self):
        resp = send_from_directory('./resource', 'test.html')
        resp.headers['Cache-Control'] = 'no-store'
        resp.headers['Expires'] = 'Fri, 12 Jan 2001 0:0:0 GMT'
        return resp

class Default(Resource):
    log.debug('check health')
    def get(self):
        return send_from_directory('./resource', 'index.html')

class HealthCheck(Resource):
    log.debug('check health')
    def get(self):
        return {"status": "200","message": "success"}, 200

class GetEnterCCbotUrl(Resource):
    log.debug('enter get ccbot url')
    def get(self):
        return {"status": "200","data": const.ENTER_CCBOT_URL}, 200
    def post(self):
        session_id = request.get_json('session_id')

        if not session_id is None:
            account = const.LEAST_AUTH_USERNAME
            password = const.LEAST_AUTH_PASSWORD
            callApi_sso = service_sso.CallApi()
            token = callApi_sso.get_auth_token(account, password)

            return {"status": "200","data": const.ENTER_CCBOT_URL+'?tokenInfo='+token+'&'}, 200
        else:
            return {"status": "200","data": const.ENTER_CCBOT_URL}, 200

class Chat(Resource):
    def get(self):
        callApi=service.CallApi()
        log.info('GetChatRecords api start')
        log.info(request.json.get('callID'))
        response = callApi.getChatRecords(request.json.get('callID'))
        # log.info(response)
        return {
            'data': response
        }, 200
    def post(self):
        callApi=service.CallApi()
        log.info('GetChatRecords api start')
        log.info(request.json.get('callID'))
        response = callApi.getChatRecords(request.json.get('callID'))
        # log.info(response)
        return {
            'data': response
        }, 200

class Tag(Resource):
    def get(self):
        callApi=service.CallApi()
        log.info('GetTagByCallId api start')
        log.info(request.json.get('callID'))
        response = callApi.getTagByCallId(request.json.get('callID'))
        log.info(response)
        return {
            'data': response
        }, 200
    def post(self):
        callApi=service.CallApi()
        log.info('GetTagByCallId api start')
        log.info(request.json.get('callID'))
        response = callApi.getTagByCallId(request.json.get('callID'))
        log.info(response)
        return {
            'data': response
        }, 200

class GetChatRecords(Resource):
    def get(self):
        callApi=service.CallApi()
        log.info('GetChatRecords api start')
        response = callApi.getChatRecords("1e8fc05f-6c04-4333-a5b9-436fd5663f7b")
        log.info(response)
        return {
            'message': str(response)
        }, 200
    def post(self):
        callApi=service.CallApi()
        log.info('GetChatRecords api start')
        response = callApi.getChatRecords("1e8fc05f-6c04-4333-a5b9-436fd5663f7b")
        log.info(response)
        return {
            'message': str(response)
        }, 200

class Transmit(Resource):
    def get(self):
        return {
            'status': 200,
            'message': transmitProcess(request)
        }, 200

def transmitProcess(request):
    try:
        utils.cleanFolder(const.SFTP_UPLO_PATH)
        callApi=service.CallApi()
        ccbotData = callApi.getTag(request)
        log.debug(json.dumps(ccbotData))
        log.info("ccbotData quantity:" + str(len(ccbotData)))
        if len(ccbotData) == 0:
            return 'no data need transmit'
        log.debug("ccbotData data:" + str(ccbotData))

        # =====================================
        # ccbotData = {}
        # ccbotData =  [{"session_id": "acde1df7-5cab-4f69-8fa6-12e8a2536dd0", "call_direction": "outbound", "caller": "07010092440", "callee": "0972146919", "status": 1, "calls_number": 1, "talk_start_time": "2020-10-20 16:37:51", "ring_duration": 12, "talk_duration": 68, "extend_data": {"scenario":"0001","*campaign":"00000001","*PID":"pid_data2","*確認本人": "yes"}}]
        # =====================================

        scenario_key = json.loads(const.SCENARIO_KEY)
        scen_val_len = json.loads(const.SCEN_VAL_LEN)

        for data in ccbotData:
            for extend in data.get("extend_data"):
                data[extend] = data["extend_data"][extend]
            del data["extend_data"]
            if data.get("information"):
                for information in data.get("information"):
                    data[information] = data["information"][information]
                del data["information"]

        log.debug(json.dumps(ccbotData))
        csv_data = {}
        for data in ccbotData:
            campaign=data.get("scenario")
            if not campaign or campaign not in scenario_key.keys():
                continue
            campaign_header = scenario_key[campaign]
            if csv_data.get(campaign) == None:
                csv_data[campaign]=[]
            csv_data[campaign].append(data)

        log.debug(json.dumps(csv_data))
        if csv_data == {} :
            log.info('no campaign id mapping, process complete')
            return 'no campaign id mapping'

        # csv_header =  [scenario_key 去除 * 號]
        csv_header={}
        for scenario in scenario_key:
            header_list=[]
            for key in scenario_key[scenario]:
                regex = re.search('^(\*{1}|^\d{1,3}\.{1}\*?)(.*)', key)
                if regex:
                    header_list.append(regex.group(2))
                else:
                    header_list.append(key)
            csv_header[scenario]=header_list

        log.debug(scenario_key)
        log.debug(csv_header)
            
        total_file = []
        total_file_for_csv = []
        # begTime = datetime.strptime(const.CSV_FILE_BEG_TIME, '%Y-%m-%d %H:%M:%S').strftime("%Y%m%d")
        endTime = datetime.strptime(const.CSV_FILE_END_TIME, '%Y-%m-%d %H:%M:%S').strftime("%Y%m%d")

        for campaign_data in csv_data:
            csvfile=[]
            csvfile.append(csv_header[campaign_data]) #塞header進csv
            for data in csv_data[campaign_data]:
                csv_record = []
                for key in scenario_key[campaign_data]:
                    # val_len = 16 #如json沒特別設定預設塞16個
                    # if scen_val_len.get(key) != None:
                    #     val_len = scen_val_len.get(key)
                    if data.get(key) == '-' or data.get(key) == None:
                        # csv_record.append(' ' * val_len)
                        csv_record.append('')
                    else:
                        # space_len = val_len - len(str(data.get(key)))
                        # csv_record.append(str(data.get(key)) + ' ' * space_len)
                        csv_record.append(str(data.get(key)))
                csvfile.append(csv_record)
            log.debug(str(json.dumps(csvfile)))

            fileName = endTime + "_" + campaign_data + ".csv"
            filePath = const.SFTP_UPLO_PATH + fileName
            utils.exportCsv(filePath, csvfile)
            log.info("export csv file: " + filePath)

            total_file.append(filePath)
            file_name_record=[]
            file_name_record.append(fileName)
            total_file_for_csv.append(file_name_record)
        total_file_for_csv_path = const.SFTP_UPLO_PATH + "BOTRETURNLIST_" + endTime + ".csv"
        utils.exportCsv(total_file_for_csv_path, total_file_for_csv)
        log.info("export total_file_for_csv:" + total_file_for_csv_path + " ,with data: " + str(total_file_for_csv))
        total_file.append(total_file_for_csv_path)

        log.info('total_file:' + str(total_file))
        log.debug(str(const.IS_FTP_UPLOAD))
        if str(const.IS_FTP_UPLOAD)=='true':
            log.debug('use ftp upload')
            utils.ftpUpload(total_file)
        else:
            log.debug('use sftp upload')
            utils.sftpUpload(total_file)
        log.info('process complete')
        return 'process complete'

    except Exception as e:
        log.error("transmitProcess error: "+utils.except_raise(e))
        return utils.except_raise(e)
