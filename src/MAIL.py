import smtplib
from src import ToMail
from email.mime.text import MIMEText
from email.utils import formataddr


def set_msg(datas, to):
    msg = ''
    if to == 'student':
        msg = ToMail.to_student(datas)
    elif to == 'teacher':
        msg = ToMail.to_teacher(datas)
    elif to == 'delete':
        msg = ToMail.del_to_mail(datas)
    return msg


def mail(datas, my_sender, my_user, my_pass, to):
    msg = set_msg(datas, to)
    try:
        mail_msg = MIMEText(msg, 'html', 'utf-8')
        mail_msg['From'] = formataddr(["泽众教育", my_sender])
        mail_msg['To'] = my_user
        if to == 'student':
            mail_msg['Subject'] = "您的预约信息请注意查收"
        elif to == 'teacher':
            mail_msg['Subject'] = "有预约信息请注意查收"
        elif to == 'delete':
            mail_msg['Subject'] = "有取消预约信息请注意查收"
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(my_sender, my_pass)
        server.sendmail(my_sender, [my_user, ], mail_msg.as_string())
        server.quit()
    except Exception as err:
        print(err)


def mailto(data):
    my_sender = '2195007463@qq.com'
    my_pass = 'wtkdlhjwyblrdica'
    my_user = data['mail']
    # teacher_mails = ['2195007463@qq.com']
    use_data = {
        'teacher': data['teacher'],
        'name': data['name'],
        'school': data['school'],
        'grade': data['grade'],
        'subjects': data['subjects'],
        'date': data['date'],
        'time': data['time']
    }
    mail(use_data, my_sender, my_user, my_pass, 'student')
    # for teacher_mail in teacher_mails:
    #     mail(use_data, my_sender, teacher_mail, my_pass, 'teacher')


def del_mailto(data):
    my_sender = '2195007463@qq.com'
    my_pass = 'wtkdlhjwyblrdica'
    teacher_mails = ['2195007463@qq.com']
    use_data = {
        'teacher': data['teacher'],
        'name': data['name'],
        'date': data['date'],
        'time': data['time']
    }
    for teacher_mail in teacher_mails:
        mail(use_data, my_sender, teacher_mail, my_pass, 'delete')
