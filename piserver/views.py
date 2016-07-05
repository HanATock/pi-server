from flask import render_template, redirect, url_for

from piserver import app, db
from piserver.db_models import Device
from piserver.forms import DeviceForm


@app.route('/devices', methods=['GET'])
def list_devices():
    return render_template('devices/list.html', devices=Device.query.all())


@app.route('/devices/create', methods=['GET', 'POST'])
def create_device():
    form = DeviceForm()
    if form.validate_on_submit():
        device = Device()
        form.populate_obj(device)

        db.session.add(device)
        db.session.commit()

        return redirect(url_for('list_devices'))

    return render_template('devices/edit.html', form=form)
