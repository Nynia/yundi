from app import db


class LowValueWhiteUser(db.Model):
    __tablename__ = 'low_quality_white_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    createtime = db.Column(db.String(255))

    def to_json(self):
        json_post = {
            'phonenum': self.name,
            'createtime': self.createtime[:4] + '-' +
                          self.createtime[4:6] + '-' +
                          self.createtime[6:8] + ' ' +
                          self.createtime[8:10] + ':' +
                          self.createtime[10:12]
        }
        return json_post

    def __repr__(self):
        return '<Phonenum %r>' % self.name


class AttackLog(db.Model):
    __tablename__ = 'attack_log'
    id = db.Column(db.Integer, primary_key=True)
    ddostype = db.Column(db.String(30))
    destIp = db.Column(db.String(30))
    srcIp = db.Column(db.String(30))
    startTime = db.Column(db.String(30))
    endTime = db.Column(db.String(30))
    ts = db.Column(db.String(30))
    def to_json(self):
        json_post = {
            'ddostype': self.name,
            'destIp': self.destIp,
            'srcIp': self.srcIp,
            'startTime': self.startTime,
            'endTime': self.endTime,
            'ts': self.dateTime
        }
        return json_post

    def __repr__(self):
        return '<DDosType %s, src: %s, dst: %s>' % self.ddostype, self.srcIp, self.destIp

class PhishingLog(db.Model):
    __tablename__ = 'phishing_log'
    id = db.Column(db.Integer, primary_key=True)
    clientIp = db.Column(db.String(30))
    clientPort = db.Column(db.Integer)
    requestTime = db.Column(db.String(30))
    serverIp = db.Column(db.String(30))
    serverDomain = db.Column(db.String(50))
    ts = db.Column(db.String(30))
    def to_json(self):
        json_post = {
            'clientIp': self.clientIp,
            'clientPort': self.clientPort,
            'serverIp': self.serverIp,
            'serverDomain': self.serverDomain,
            'requestTime': self.requestTime,
            'ts': self.dateTime
        }
        return json_post

    def __repr__(self):
        return '<phishing :%s>' % self.ts