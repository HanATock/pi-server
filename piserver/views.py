from flask import render_template, redirect, request, url_for
from flask_wtf import Form
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


@app.route('/devices/edit/<int:id>', methods=['GET', 'POST'])
def edit_device(id):
    device = Device.query.get_or_404(id)
    form = DeviceForm(obj=device)
    if form.validate_on_submit():
        form.populate_obj(device)

        db.session.commit()

        return redirect(url_for('list_devices'))

    return render_template('devices/edit.html', form=form, device=device)


@app.route('/devices/delete/<int:id>', methods=['GET', 'POST'])
def delete_device(id):
    device = Device.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(device)
        db.session.commit()

        return redirect(url_for('list_devices'))

    return render_template('devices/confirm_delete.html', device=device)
