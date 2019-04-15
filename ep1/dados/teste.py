import datetime

print("teste")
data = datetime.datetime(year=2019,month=4,day=4,\
        hour=16,minute=41,second=33,microsecond=127000)
print(data)
data2 = datetime.datetime(year=2019,month=4,day=4,\
        hour=16,minute=41,second=33,microsecond=199000)

print(data2)

diff = data2 -data
print(diff)
print(diff.total_seconds())
