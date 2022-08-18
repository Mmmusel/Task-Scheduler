import calendar
from datetime import datetime


# 计算一个活动的持续时间，单位为分钟
def cal_minute_duration(start, end):
    '''
    start_time = datetime.strptime(start, "%Y/%m/%d:%H:%M")  # 输入年/月/日:时:分
    end_time = datetime.strptime(end, "%Y/%m/%d:%H:%M")  # 输入年/月/日:时:分
    '''
    start_time = datetime.strptime(start, "%H:%M")  # 输入时:分
    end_time = datetime.strptime(end, "%H:%M")  # 输入时:分
    min_duration = ((end_time - start_time).total_seconds()) / 60
    return int(min_duration)


# 计算某一天所在一周的7天日期
def cal_date_to_week(date):
    date_copy = datetime.strptime(date, '%Y/%m/%d')  # 输入年/月/日
    iso_year = date_copy.isocalendar()[0]
    iso_week = date_copy.isocalendar()[1]
    date_list = []
    for i in range(1, 8):
        d = str(date_copy.fromisocalendar(iso_year, iso_week, i))
        date_list.append(d[0:10].replace("-", "/"))
    return date_list  # 返回7个"年/月/日"


# 计算某一天所在一月的所有日期
def cal_date_to_month(date):
    year, month, day = date.split("/")
    n = calendar.monthrange(int(year), int(month))
    date_list = []
    for i in range(1, n[1] + 1):
        if 1 <= i <= 9:
            s = str(year) + "/" + str(month) + "/0" + str(i)
        else:
            s = str(year) + "/" + str(month) + "/" + str(i)
        date_list.append(s)
    return date_list  # 以"年/月/日"返回当月的所有日期
