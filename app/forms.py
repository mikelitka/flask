from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, RadioField, SubmitField, SelectField
from wtforms.validators import DataRequired

class FlaskForm(FlaskForm):
	vmname = StringField('vmname')
	vmsize = RadioField('Machine Size', choices = [('S','Small - 1 CPU, 2 GB RAM'), ('M','Medium - 2 CPU, 4 GB RAM'), ('L','Large - 4 CPU, 8 GB RAM')])
	vmos = SelectField('Opearating System', choices = [('c6','CentOS 6'), ('c7','CentOS 7')])
