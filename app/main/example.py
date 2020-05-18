from . import main
from flask import jsonify
from app import db
from app.models import AttackLog, PhishingLog
import time, json, datetime
from flask import request

def ts_trans(ts):
    timeArray = time.localtime(ts)
    return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

@main.route('/data1', methods=['POST'])
def get_data():
    print(request.data)
    for o in json.loads(request.data):
        ddosType = o['ddosType']
        destIp = o['destIp']
        srcIp = o['sourceIp']
        startTime = ts_trans(o['startTime'])
        endTime = ts_trans(o['endTime'])
        print(','.join([ddosType, destIp, srcIp, startTime, endTime]))

        attack_log = AttackLog()
        attack_log.ddostype = ddosType
        attack_log.destIp = destIp
        attack_log.srcIp = srcIp
        attack_log.startTime = startTime
        attack_log.endTime = endTime
        attack_log.ts = datetime.datetime.now()
        db.session.add(attack_log)
        db.session.commit()
    return ''

@main.route('/data2', methods=['POST'])
def get_data2():
    print(request.data)
    for o in json.loads(request.data):
        clientIp = o['clientIp']
        clientPort = o['clientPort']
        requestTime = o['requestTime']
        serverIp = o['serverIp']
        serverDomain = o['serverDomain']


        phishing_log = PhishingLog()
        phishing_log.clientIp = clientIp
        phishing_log.clientPort = clientPort
        phishing_log.serverIp = serverIp
        phishing_log.serverDomain = serverDomain
        phishing_log.requestTime = requestTime
        phishing_log.ts = datetime.datetime.now()
        db.session.add(phishing_log)
        db.session.commit()
    return ''
