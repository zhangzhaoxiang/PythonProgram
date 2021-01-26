import time
import calendar
from datetime import datetime, timedelta

localtime = time.asctime()  # 返回当前时间字符串
print('本地时间: ', localtime)

# 格式化时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S"))  # 默认输出当前时间
print(time.strftime("%Y-%m-%d"))

# 获取当前时间
now_time = datetime.now()
print(now_time)

# 获取日期
print(now_time.date())
# 获取时间
print(now_time.time())
# 获取时间戳
print(now_time.timestamp())

# 格式化时间字符串
now_time_strftime = now_time.strftime("%Y-%m-%d %H:%M:%S")
print(type(now_time_strftime), now_time_strftime)
# 格式化字符串转化为时间
now_time_strptime = datetime.strptime(now_time_strftime, "%Y-%m-%d %H:%M:%S")
print(type(now_time_strptime), now_time_strptime)

# 时间计算
print(now_time)
print(now_time+timedelta(days=1))

# 计算每月天数
month_range = calendar.monthrange(2021, 1)
print(month_range)  # 第0位表示该月第一天是星期几， 第1位表示这个月有几天

# 得到每月天数
month_ranges = calendar.mdays
print(month_ranges)  # 第0位没有意义
print(month_ranges[9])  # 获取9月天数

# 获取某月日历
cal = calendar.month(2021, 1)
print(cal)


