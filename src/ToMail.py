def to_student(datas):
    return f"""
<table class="body-wrap"
       style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px;
       width: 100%; background-color: #f6f6f6; margin: 0;"
       bgcolor="#f6f6f6">
    <tbody>
    <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px;
     margin: 0;">
        <td style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px;
         vertical-align: top; margin: 0;"
            valign="top"></td>
        <td class="container" width="600"
            style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px;
             vertical-align: top; display: block !important; max-width: 600px !important; clear: both !important;
              margin: 0 auto;" valign="top">
            <div class="content"
                 style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box;
                  font-size: 14px; max-width: 600px; display: block; margin: 0 auto; padding: 20px;">
                <table class="main" width="100%" cellpadding="0" cellspacing="0"
                       style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box;
                        font-size: 14px; border-radius: 3px; background-color: #fff; margin: 0;
                         border: 1px solid #e9e9e9;" bgcolor="#fff">
                    <tbody>
                    <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box;
                     font-size: 14px; margin: 0;">
                        <td class="content-wrap aligncenter"
                            style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box;
                             font-size: 14px; vertical-align: top; text-align: center; margin: 0; padding: 20px;"
                            align="center" valign="top">
                            <table width="100%" cellpadding="0" cellspacing="0"
                                   style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                   box-sizing: border-box; font-size: 14px; margin: 0;">
                                <tbody>
                                <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                box-sizing: border-box; font-size: 14px; margin: 0;">
                                    <td class="content-block"
                                        style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                         box-sizing: border-box; font-size: 14px; vertical-align: top;
                                          margin: 0; padding: 0 0 20px;"
                                        valign="top">
                                        <h1 class="aligncenter"
                                            style="font-family: 'Helvetica Neue',Helvetica,Arial,'Lucida Grande',
                                            sans-serif; box-sizing: border-box; font-size: 32px; color: #000;
                                             line-height: 1.2em; font-weight: 500;
                                              text-align: center; margin: 40px 0 0;" align="center">泽众教育</h1>
                                    </td>
                                </tr>
                                <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                 box-sizing: border-box; font-size: 14px; margin: 0;">
                                    <td class="content-block"
                                        style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                        box-sizing: border-box; font-size: 14px; vertical-align: top;
                                        margin: 0; padding: 0 0 20px;"
                                        valign="top">
                                        <h2 class="aligncenter"
                                            style="font-family: 'Helvetica Neue',Helvetica,Arial,'Lucida Grande',
                                            sans-serif;
                                             box-sizing: border-box; font-size: 24px; color: #000;
                                             line-height: 1.2em; font-weight: 400; text-align: center;
                                              margin: 40px 0 0;"
                                            align="center">泽众教育预约信息</h2>
                                    </td>
                                </tr>
                                <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                box-sizing: border-box; font-size: 14px; margin: 0;">
                                    <td class="content-block aligncenter"
                                        style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                        box-sizing: border-box; font-size: 14px; vertical-align: top;
                                         text-align: center; margin: 0; padding: 0 0 20px;"
                                        align="center" valign="top">
                                        <table class="invoice"
                                               style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                               box-sizing: border-box; font-size: 14px; text-align: left; width: 80%;
                                                margin: 40px auto;">
                                            <tbody>
                                            <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                            box-sizing: border-box; font-size: 14px; margin: 0;">
                                                <td style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                                box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0;
                                                 padding: 5px 0;" valign="top">您好, {datas['name']}
                                                </td>
                                            </tr>
                                            <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                            box-sizing: border-box; font-size: 14px; margin: 0;">
                                                <td style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                                box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0;
                                                 padding: 5px 0;" valign="top">您在泽众教育预约系统的预约信息请注意查收
                                                </td>
                                            </tr>
                                            <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                            box-sizing: border-box; font-size: 14px; margin: 0;">
                                                <td style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                                box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0;
                                                 padding: 5px 0;" valign="top">
                                                    <p>预约咨询师:<b>{datas['teacher']}</b></p>
                                                    <p>预约日期:<b>{datas['date']}</b></p>
                                                    <p>预约时间段:<b>{datas['time']}</b></p>
                                                </td>
                                            </tr>
                                            <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                            box-sizing: border-box; font-size: 14px; margin: 0;">
                                                <td>
                                                    如需取消请点击
                                        <a href="http://127.0.0.1:8080/del?date={datas['date']}&time={datas['time']}">
                                                    <b>取消</b></a>
                                                </td>
                                            </tr>
                                            <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                            box-sizing: border-box; font-size: 14px; margin: 0;">
                                                <td class="content-block aligncenter"
                                                    style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                                    box-sizing: border-box; font-size: 14px; vertical-align: top;
                                                    text-align: center; margin: 0; padding: 0 0 20px;" align="center"
                                                    valign="top">
                                                </td>
                                            </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                                </tbody>
                            </table>
                            <div class="footer"
                                 style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing:
                                 border-box; font-size: 14px; width: 100%; clear: both; color: #999;
                                 margin: 0; padding: 20px;">
                                <table width="100%"
                                       style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                       box-sizing: border-box; font-size: 14px; margin: 0;">
                                    <tbody>
                                    <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                    box-sizing: border-box; font-size: 14px; margin: 0;">
                                        <td>泽众教育</td>
                                    </tr>
                                    </tbody>
                                </table>
                            </div>
                        </td>
                        <td style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing:
                        border-box; font-size: 14px; vertical-align: top; margin: 0;" valign="top"></td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </td>
    </tr>
    </tbody>
</table>
    """


def to_teacher(datas):
    return f"""
<table class="body-wrap"
       style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px;
       width: 100%; background-color: #f6f6f6; margin: 0;"
       bgcolor="#f6f6f6">
    <tbody>
    <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px;
     margin: 0;">
        <td style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px;
         vertical-align: top; margin: 0;"
            valign="top"></td>
        <td class="container" width="600"
            style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px;
             vertical-align: top; display: block !important; max-width: 600px !important; clear: both !important;
              margin: 0 auto;" valign="top">
            <div class="content"
                 style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box;
                  font-size: 14px; max-width: 600px; display: block; margin: 0 auto; padding: 20px;">
                <table class="main" width="100%" cellpadding="0" cellspacing="0"
                       style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box;
                        font-size: 14px; border-radius: 3px; background-color: #fff; margin: 0;
                         border: 1px solid #e9e9e9;" bgcolor="#fff">
                    <tbody>
                    <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box;
                     font-size: 14px; margin: 0;">
                        <td class="content-wrap aligncenter"
                            style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box;
                             font-size: 14px; vertical-align: top; text-align: center; margin: 0; padding: 20px;"
                            align="center" valign="top">
                            <table width="100%" cellpadding="0" cellspacing="0"
                                   style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                   box-sizing: border-box; font-size: 14px; margin: 0;">
                                <tbody>
                                <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                box-sizing: border-box; font-size: 14px; margin: 0;">
                                    <td class="content-block"
                                        style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                         box-sizing: border-box; font-size: 14px; vertical-align: top;
                                          margin: 0; padding: 0 0 20px;"
                                        valign="top">
                                        <h1 class="aligncenter"
                                            style="font-family: 'Helvetica Neue',Helvetica,Arial,'Lucida Grande',
                                            sans-serif; box-sizing: border-box; font-size: 32px; color: #000;
                                             line-height: 1.2em; font-weight: 500;
                                              text-align: center; margin: 40px 0 0;" align="center">泽众教育</h1>
                                    </td>
                                </tr>
                                <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                 box-sizing: border-box; font-size: 14px; margin: 0;">
                                    <td class="content-block"
                                        style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                        box-sizing: border-box; font-size: 14px; vertical-align: top;
                                        margin: 0; padding: 0 0 20px;"
                                        valign="top">
                                        <h2 class="aligncenter"
                                            style="font-family: 'Helvetica Neue',Helvetica,Arial,'Lucida Grande',
                                            sans-serif;
                                             box-sizing: border-box; font-size: 24px; color: #000;
                                             line-height: 1.2em; font-weight: 400; text-align: center;
                                              margin: 40px 0 0;"
                                            align="center">泽众教育预约信息</h2>
                                    </td>
                                </tr>
                                <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                box-sizing: border-box; font-size: 14px; margin: 0;">
                                    <td class="content-block aligncenter"
                                        style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                        box-sizing: border-box; font-size: 14px; vertical-align: top;
                                         text-align: center; margin: 0; padding: 0 0 20px;"
                                        align="center" valign="top">
                                        <table class="invoice"
                                               style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                               box-sizing: border-box; font-size: 14px; text-align: left; width: 80%;
                                                margin: 40px auto;">
                                            <tbody>
                                            <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                            box-sizing: border-box; font-size: 14px; margin: 0;">
                                                <td style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                                box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0;
                                                 padding: 5px 0;" valign="top">有预约信息请注意查收
                                                </td>
                                            </tr>
                                            <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                            box-sizing: border-box; font-size: 14px; margin: 0;">
                                                <td style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                                box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0;
                                                 padding: 5px 0;" valign="top">
                                                    <p>预约咨询师:<b>{datas['teacher']}</b></p>
                                                    <p>预约学员姓名:<b>{datas['name']}</b></p>
                                                    <p>学员学校:<b>{datas['school']}</b></p>
                                                    <p>学员年级:<b>{datas['grade']}</b></p>
                                                    <p>学员选科:<b>{datas['subjects']}</b></p>
                                                    <p>预约日期:<b>{datas['date']}</b></p>
                                                    <p>预约时间段:<b>{datas['time']}</b></p>
                                                </td>
                                            </tr>
                                            <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                            box-sizing: border-box; font-size: 14px; margin: 0;">
                                                <td class="content-block aligncenter"
                                                    style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                                    box-sizing: border-box; font-size: 14px; vertical-align: top;
                                                    text-align: center; margin: 0; padding: 0 0 20px;" align="center"
                                                    valign="top">
                                                </td>
                                            </tr>

                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                                </tbody>
                            </table>
                            <div class="footer"
                                 style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing:
                                 border-box; font-size: 14px; width: 100%; clear: both; color: #999;
                                 margin: 0; padding: 20px;">
                                <table width="100%"
                                       style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                       box-sizing: border-box; font-size: 14px; margin: 0;">
                                    <tbody>
                                    <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                    box-sizing: border-box; font-size: 14px; margin: 0;">
                                        <td>泽众教育</td>
                                    </tr>
                                    </tbody>
                                </table>
                            </div>
                        </td>
                        <td style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing:
                        border-box; font-size: 14px; vertical-align: top; margin: 0;" valign="top"></td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </td>
    </tr>
    </tbody>
</table>
    """


def del_to_mail(datas):
    return f"""
<table class="body-wrap"
       style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px;
       width: 100%; background-color: #f6f6f6; margin: 0;"
       bgcolor="#f6f6f6">
    <tbody>
    <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px;
     margin: 0;">
        <td style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px;
         vertical-align: top; margin: 0;"
            valign="top"></td>
        <td class="container" width="600"
            style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px;
             vertical-align: top; display: block !important; max-width: 600px !important; clear: both !important;
              margin: 0 auto;" valign="top">
            <div class="content"
                 style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box;
                  font-size: 14px; max-width: 600px; display: block; margin: 0 auto; padding: 20px;">
                <table class="main" width="100%" cellpadding="0" cellspacing="0"
                       style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box;
                        font-size: 14px; border-radius: 3px; background-color: #fff; margin: 0;
                         border: 1px solid #e9e9e9;" bgcolor="#fff">
                    <tbody>
                    <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box;
                     font-size: 14px; margin: 0;">
                        <td class="content-wrap aligncenter"
                            style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box;
                             font-size: 14px; vertical-align: top; text-align: center; margin: 0; padding: 20px;"
                            align="center" valign="top">
                            <table width="100%" cellpadding="0" cellspacing="0"
                                   style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                   box-sizing: border-box; font-size: 14px; margin: 0;">
                                <tbody>
                                <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                box-sizing: border-box; font-size: 14px; margin: 0;">
                                    <td class="content-block"
                                        style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                         box-sizing: border-box; font-size: 14px; vertical-align: top;
                                          margin: 0; padding: 0 0 20px;"
                                        valign="top">
                                        <h1 class="aligncenter"
                                            style="font-family: 'Helvetica Neue',Helvetica,Arial,'Lucida Grande',
                                            sans-serif; box-sizing: border-box; font-size: 32px; color: #000;
                                             line-height: 1.2em; font-weight: 500;
                                              text-align: center; margin: 40px 0 0;" align="center">泽众教育</h1>
                                    </td>
                                </tr>
                                <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                 box-sizing: border-box; font-size: 14px; margin: 0;">
                                    <td class="content-block"
                                        style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                        box-sizing: border-box; font-size: 14px; vertical-align: top;
                                        margin: 0; padding: 0 0 20px;"
                                        valign="top">
                                        <h2 class="aligncenter"
                                            style="font-family: 'Helvetica Neue',Helvetica,Arial,'Lucida Grande',
                                            sans-serif;
                                             box-sizing: border-box; font-size: 24px; color: #000;
                                             line-height: 1.2em; font-weight: 400; text-align: center;
                                              margin: 40px 0 0;"
                                            align="center">泽众教育预约信息</h2>
                                    </td>
                                </tr>
                                <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                box-sizing: border-box; font-size: 14px; margin: 0;">
                                    <td class="content-block aligncenter"
                                        style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                        box-sizing: border-box; font-size: 14px; vertical-align: top;
                                         text-align: center; margin: 0; padding: 0 0 20px;"
                                        align="center" valign="top">
                                        <table class="invoice"
                                               style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                               box-sizing: border-box; font-size: 14px; text-align: left; width: 80%;
                                                margin: 40px auto;">
                                            <tbody>
                                            <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                            box-sizing: border-box; font-size: 14px; margin: 0;">
                                                <td style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                                box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0;
                                                 padding: 5px 0;" valign="top">有取消预约信息请注意查收
                                                </td>
                                            </tr>
                                            <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                            box-sizing: border-box; font-size: 14px; margin: 0;">
                                                <td style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                                box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0;
                                                 padding: 5px 0;" valign="top">
                                                    <p>取消预约咨询师:<b>{datas['teacher']}</b></p>
                                                    <p>取消预约学员姓名:<b>{datas['name']}</b></p>
                                                    <p>取消预约日期:<b>{datas['date']}</b></p>
                                                    <p>取消预约时间段:<b>{datas['time']}</b></p>
                                                </td>
                                            </tr>
                                            <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                            box-sizing: border-box; font-size: 14px; margin: 0;">
                                                <td class="content-block aligncenter"
                                                    style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                                    box-sizing: border-box; font-size: 14px; vertical-align: top;
                                                    text-align: center; margin: 0; padding: 0 0 20px;" align="center"
                                                    valign="top">
                                                </td>
                                            </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                                </tbody>
                            </table>
                            <div class="footer"
                                 style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing:
                                 border-box; font-size: 14px; width: 100%; clear: both; color: #999;
                                 margin: 0; padding: 20px;">
                                <table width="100%"
                                       style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                       box-sizing: border-box; font-size: 14px; margin: 0;">
                                    <tbody>
                                    <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
                                    box-sizing: border-box; font-size: 14px; margin: 0;">
                                        <td>泽众教育</td>
                                    </tr>
                                    </tbody>
                                </table>
                            </div>
                        </td>
                        <td style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing:
                        border-box; font-size: 14px; vertical-align: top; margin: 0;" valign="top"></td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </td>
    </tr>
    </tbody>
</table>
        """
