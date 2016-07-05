import json
import socket

from piserver import db


class Device(db.Model):
    __tablename__ = 'device'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255))
    ip_address = db.Column(db.String(255))

    output_pin = db.Column(db.Integer)
    output_state = db.Column(db.Boolean, default=False)

    def send(self, action, payload):
        data = json.dumps({
            'action': action,
            'payload': payload
        })

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.connect((self.ip_address, 1338))
            sock.sendall("{}\n".format(data).encode('UTF-8'))
            received = sock.recv(1024).decode('UTF-8')

            print("Sent:     {}".format(data))
            print("Received: {}".format(received))
        except:
            raise
        finally:
            sock.close()


class Measurement(db.Model):
    __tablename__ = 'measurement'

    id = db.Column(db.Integer, primary_key=True)

    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    device = db.relationship('Device', uselist=False)

    value = db.Column(db.Float)
    timestamp = db.Column(db.Integer)
