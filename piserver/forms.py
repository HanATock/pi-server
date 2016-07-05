from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import Required


class DeviceForm(Form):
    name = StringField('Name', validators=[Required()])
    ip_address = StringField('IP address', validators=[Required()])
    unit = StringField('Unit', validators=[Required()])
