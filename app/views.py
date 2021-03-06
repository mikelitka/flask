import os
from flask import render_template
from app import app
from .forms import FlaskForm
from ansible.playbook import Playbook

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = FlaskForm()
	if form.validate_on_submit():
	  vmname = form.vmname.data
	  vmsize = form.vmsize.data
	  vmos = form.vmos.data
	  pb = Playbook(playbook='/common/conf/ansible/playbooks/test.yaml')
	  pb.run()
	  return render_template('result.html',title='Build Result', vmname=vmname, vmsize=vmsize, vmos=vmos)
	return render_template('request.html',
				title='Build VM',
				form=form)
