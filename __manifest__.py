{
    'name': 'Gửi email khi đến thời gian',
    'version': '1.0',
    'category': 'Other',
    'summary': 'Gửi email thông báo cho lịch hẹn',
    'sequence': '1',
    'author': 'Thịnh Nguyễn',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/cron.xml',
        'data/mail_template.xml',
        # 'data/sequence.xml',
        'views/reminders.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

