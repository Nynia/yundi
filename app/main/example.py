from . import main
from flask import jsonify
from app import db
from app.models import EventLog
import time, json, datetime
from flask import request

def ts_trans(ts):
    timeArray = time.localtime(ts)
    return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

@main.route('/data', methods=['POST'])
def get_data():
    print(request.data)
    print(type(request.data))
    for o in json.loads(request.data):
        ddosType = o['ddosType']
        destIp = o['destIp']
        srcIp = o['sourceIp']
        startTime = ts_trans(o['startTime'])
        endTime = ts_trans(o['endTime'])
        print(','.join([ddosType, destIp, srcIp, startTime, endTime]))

        event_log = EventLog()
        event_log.ddostype = ddosType
        event_log.destIp = destIp
        event_log.srcIp = srcIp
        event_log.startTime = startTime
        event_log.endTime = endTime
        event_log.ts = datetime.datetime.now()
        db.session.add(event_log)
        db.session.commit()
    return ''
