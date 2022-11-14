import xlwt
from src import func
from io import BytesIO
from flask import make_response


def login(data):
    sql = f"SELECT A_id,学生姓名,性别,学校,年级,选科,家长姓名,联系方式,邮箱,估分,状态  FROM UserInfo WHERE " \
          f"A_id ={data['A_id']} AND 学生姓名='{data['name']}'"
    data = func.fetchone(sql)
    if data:
        state = data[10]
        if state == '0':
            return {
                'A_id': data[0],
                'name': data[1],
                'state': data[10]
            }
        else:
            return {
                'A_id': data[0],
                'name': data[1],
                'sex': data[2],
                'grade': data[4],
                'fraction': data[9],
                'subjects': data[5],
                'school': data[3],
                'parents': data[6],
                'phoneNumber': data[7],
                'mail': data[8],
                'state': data[10]
            }
    else:
        return {
            'state': "error",
            "error": "你输入的学生姓名或A_id错误"
        }


def a_login(data):
    user = data['user']
    password = data['password']
    sql = f"SELECT * FROM Admin WHERE 账号 ='{user}' AND 密码='{password}'"
    data = func.fetchone(sql)
    if data:
        return {'state': 'ok'}
    else:
        return {
            'state': 'error',
            'error': '账号或密码错误'
        }


def update_user_data(data):
    sql = f"UPDATE UserInfo SET 学生姓名='{data['name']}',学校='{data['school']}',性别='{data['sex']}'," \
          f"年级='{data['grade']}',选科='{data['subjects']}',家长姓名='{data['parents']}',联系方式='{data['phoneNumber']}'" \
          f",邮箱='{data['mail']}',估分={int(data['fraction'])},状态='1' WHERE A_id ='{data['A_id']}'"
    func.execute_query(sql)


def get_teacher():
    sql = "SELECT * FROM Teacher"
    teachers_list = []
    teachers = func.fetchall(sql)
    for teacher in teachers:
        teacher_list = {
            'id': teacher[0],
            'name': teacher[1],
            'grade': teacher[2],
            'title': teacher[3]
        }
        teachers_list.append(teacher_list)
    return teachers_list


def get_reserve(teacher):
    sql = f"SELECT 日期,时间段 FROM Reserve where 教师='{teacher}'"
    reserves_list = ''
    reserves = func.fetchall(sql)
    for reserve in reserves:
        reserve_list = [
            reserve[0] + " " + reserve[1],
        ]
        reserves_list += ','.join(reserve_list) + ","
    sql = f"SELECT 时间,时间段 FROM RestDay where 教师='{teacher}'"
    rest_day_time = func.fetchall(sql)
    for reserve in rest_day_time:
        reserve_list = [
            reserve[0] + " " + reserve[1],
        ]
        reserves_list += ','.join(reserve_list) + ","
    return reserves_list


def a_get_reserve():
    sql = f"SELECT 教师,学生姓名,日期,时间段 FROM Reserve ORDER BY 日期 DESC,时间段 DESC"
    return get_reserve_over(sql)


def my_get_reserve(name, A_id):
    sql = f"SELECT 教师,学生姓名,日期,时间段 FROM Reserve WHERE 学生姓名='{name}' AND A_ID='{A_id}'" \
          f" ORDER BY 日期 DESC,时间段 DESC"
    return get_reserve_over(sql)


def get_reserve_over(sql):
    my_reserves_list = []
    my_reserves = func.fetchall(sql)
    for reserve in my_reserves:
        my_reserve_list = {
            'teacher': reserve[0],
            'name': reserve[1],
            'date': reserve[2],
            'time': reserve[3],
        }
        my_reserves_list.append(my_reserve_list)
    return my_reserves_list


def my_get_data(name):
    sql = f"SELECT 教师,学生姓名,性别,年级,选科,学校,家长姓名,联系方式,日期,时间段,邮箱 FROM Reserve WHERE 学生姓名='{name}' "
    datas = func.fetchone(sql)
    return {
        'teacher': datas[0],
        'sex': datas[2],
        'grade': datas[3],
        'subjects': datas[4],
        'school': datas[5],
        'parents': datas[6],
        'phoneNumber': datas[7],
        'date': datas[8],
        'time': datas[9],
        'mail': datas[10]
    }


def insert(data):
    sql = f"INSERT INTO Reserve" \
          f"(教师,A_ID,学生姓名,性别,年级,选科,学校,估分,家长姓名,联系方式,备注,日期,时间段,邮箱) " \
          f"VALUES ('{data['teacher']}','{data['A_id']}','{data['name']}','{data['sex']}','{data['grade']}'," \
          f"'{data['subjects']}','{data['school']}','{int(data['fraction'])}', '{data['parents']}'," \
          f"'{data['phoneNumber']}','{data['remark']}','{data['date']}','{data['time']}','{data['mail']}')"
    func.execute_query(sql)


def delete(data):
    sql = f"DELETE FROM Reserve WHERE 教师='{data['teacher']}'AND 日期='{data['date']}' AND 时间段='{data['time']}'"
    func.execute_query(sql)


def export():
    sql = f"SELECT 教师,A_ID,学生姓名,性别,学校,年级,选科,家长姓名,联系方式,邮箱,日期,时间段,备注 FROM Reserve"
    reserves = func.fetchall(sql)
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)
    sheet.write(0, 0, '教师')
    sheet.write(0, 1, 'A_ID')
    sheet.write(0, 2, '学生姓名')
    sheet.write(0, 3, '性别')
    sheet.write(0, 4, '学校')
    sheet.write(0, 5, '年级')
    sheet.write(0, 6, '选科')
    sheet.write(0, 7, '家长姓名')
    sheet.write(0, 8, '联系方式')
    sheet.write(0, 9, '邮箱')
    sheet.write(0, 10, '日期')
    sheet.write(0, 11, '时间段')
    sheet.write(0, 12, '备注')
    for r in range(0, len(reserves)):
        for child in range(0, len(reserves[r])):
            sheet.write(r + 1, child, reserves[r][child])
    sio = BytesIO()
    book.save(sio)
    sio.seek(0)
    response = make_response(sio.getvalue())
    response.headers['Content-type'] = 'application/vnd.ms-excel'
    response.headers['Content-Disposition'] = 'attachment; filename=data.xlsx'
    return response


def rest_day():
    sql = "SELECT * FROM RestDay ORDER BY 时间 DESC,时间段 DESC"
    rest_day_ist = []
    rest = func.fetchall(sql)
    for reserve in rest:
        my_reserve_list = {
            'list': reserve[0],
            'teacher': reserve[1],
            'date': reserve[2],
            'time': reserve[3],
        }
        rest_day_ist.append(my_reserve_list)
    return rest_day_ist


def setting_rest(data):
    sql = f"INSERT INTO RestDay(教师,时间,时间段) VALUES ('{data['teacher']}'" \
          f",'{data['date']}','{data['time']}')"
    func.execute_query(sql)


def del_rest(data):
    sql = f"DELETE FROM RestDay WHERE 教师='{data['teacher']}'" \
          f"AND 时间='{data['date']}' AND 时间段='{data['time']}'"
    func.execute_query(sql)


def del_teacher(data):
    sql = f"DELETE FROM Teacher where 教师姓名='{data['name']}'AND 教师级别='{data['grade']}'"
    func.execute_query(sql)


def insert_teacher(data):
    sql = f"INSERT INTO Teacher" \
          f"(教师姓名,教师级别,教师信息) VALUES ('{data['name']}','{data['grade']}','{data['title']}')"
    func.execute_query(sql)


def update_teacher(data):
    sql = f"UPDATE Teacher SET 教师姓名='{data['name']}', 教师级别='{data['grade']}', 教师信息='{data['title']}'" \
          f" WHERE 教师姓名='{data['name']}'"
    func.execute_query(sql)
