from flask import render_template, redirect, request, url_for

from piserver import app, db
from piserver.db_models import Device
from piserver.forms import DeviceForm, OutputPinForm


@app.route('/devices', methods=['GET'])
def list_devices():
    return render_template('devices/list.html', devices=Device.query.all())


@app.route('/devices/view/<int:id>', methods=['GET', 'POST'])
def view_device(id):
    device = Device.query.get_or_404(id)

    form = None
    if device.output_pin is not None:
        form = OutputPinForm(obj=device)
        if form.validate_on_submit():
            output_state = form.output_state.data
            device.output_state = output_state
            db.session.commit()

            device.send('write_pin', dict(pin=device.output_pin,
                        value=int(output_state)))

    return render_template('devices/view.html', device=device, form=form)


@app.route('/devices/create', methods=['GET', 'POST'])
def create_device():
    form = DeviceForm()
    if form.validate_on_submit():
        device = Device()
        form.populate_obj(device)

        db.session.add(device)
        db.session.commit()

        return redirect(url_for('view_device', id=device.id))

    return render_template('devices/edit.html', form=form)


@app.route('/devices/edit/<int:id>', methods=['GET', 'POST'])
def edit_device(id):
    device = Device.query.get_or_404(id)

    form = DeviceForm(obj=device)
    if form.validate_on_submit():
        form.populate_obj(device)

        db.session.commit()

        return redirect(url_for('view_device', id=device.id))

    return render_template('devices/edit.html', form=form, device=device)


@app.route('/devices/delete/<int:id>', methods=['GET', 'POST'])
def delete_device(id):
    device = Device.query.get_or_404(id)

    if request.method == 'POST':
        db.session.delete(device)
        db.session.commit()

        return redirect(url_for('list_devices'))

    return render_template('devices/confirm_delete.html', device=device)
