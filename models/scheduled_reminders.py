from odoo import api, models, fields
from odoo.exceptions import ValidationError
import datetime


class ScheduledReminders(models.Model):
	_name = 'scheduled.reminders'
	_inherit = ['mail.thread', 'mail.activity.mixin']
	_description = 'Reminders Record'
	
	# @api.model
	# def create(self, vals):
	# 	if vals.get('name_seq', ('New')) == ('New'):
	# 		vals['name_seq'] = self.env['ir.sequence'].next_by_code('reminder.sequence') or ('New')
	# 	result = super(ScheduledReminders, self).create(vals)
	# 	return result
	
	# @api.multi
	# def name_get(self):
	# 	# name get function for the model executes automatically
	# 	res = []
	# 	for rec in self:
	# 		res.append((rec.id, '%s - %s' % (rec.name_seq, rec.hih)))
	# 	return res
	
	name = fields.Char('Thu')
	
	recipients = fields.Many2many('res.partner', 'mail_compose_message_res_partner_rel1',
        'wizard_id1', 'partner_id1', 'Recipients')
	description = fields.Text(string="Messenger")
	user_id = fields.Many2many('res.users')
	time_reminder = fields.Datetime(string='Time send')
	
	# Sending Email in Button Click
	@api.multi
	def action_send_email(self):
		# sending the email recipients via email

		template_id = self.env.ref('scheduled_reminders.reminder_email_template').id
		template = self.env['mail.template'].browse(template_id)
		template.send_mail(self.id, force_send=True)
	
	# @api.multi
	# def action_send_email(self):
	# 	for recipient in self.recipients:
	# 		template_rec = self.env.ref('scheduled_reminders.reminder_email_template')
	# 		template_rec.write({'email_to': recipient.email})
	# 		template_rec.send_mail(self.id, force_send=True)
	
	

	def send_email(self):
		email = self.env['scheduled.reminders'].search([])
		for rc in email:
			if datetime.datetime.today() >= rc.time_reminder:
				rc.action_send_email()
