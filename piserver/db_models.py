from piserver import db


class Device(db.Model):
    __tablename__ = 'device'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255))
    ip_address = db.Column(db.String(255))
    unit = db.Column(db.String(10))

    measurements = db.relationship('Measurement', cascade='all, delete-orphan',
                                   order_by='Measurement.timestamp.desc()')

    @property
    def current_value(self):
        return self.measurements[0].value if len(self.measurements) > 0 else 0


class Measurement(db.Model):
    __tablename__ = 'measurement'

    id = db.Column(db.Integer, primary_key=True)

    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    device = db.relationship('Device', uselist=False)

    value = db.Column(db.Float)
    timestamp = db.Column(db.Integer)
