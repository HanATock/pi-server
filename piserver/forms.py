from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import Required


class DeviceForm(Form):
    name = StringField('Name', validators=[Required()])
    ip_address = StringField('IP address', validators=[Required()])
    output_pin = StringField('Output pin')


class OutputPinForm(Form):
    output_state = BooleanField('Output state')
