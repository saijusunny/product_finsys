from dateutil.relativedelta import relativedelta
from datetime import date,datetime, timedelta

mnt=date.today().month
year=date.today().year
print(mnt)
print(year)
today_gt2 = date.today()
firsty_gt2= today_gt2.replace(day=1)
last_monthy_gt2 = firsty_gt2 -relativedelta(months=12)+relativedelta(months=12)

end_todayy_gt2 = last_monthy_gt2
end_firsty_gt2 = end_todayy_gt2.replace(day=1)
end_monthy_gt2 = end_firsty_gt2 -relativedelta(days=1)+relativedelta(years=1)
print(last_monthy_gt2)

print(end_monthy_gt2)