from datetime import *
hoy = date.today()
print(hoy)

mes=hoy.month
print(mes)

totaldias=date.today() - timedelta(days=2)
print(totaldias)

hoyes=date.today()
print(hoyes)

iniciomes="%s-%s-01" % (hoyes.year, hoyes.month)

print (iniciomes)

fechaini='2014-03-11'

fec=datetime.strptime(fechaini,'%Y-%m-%d')

print(fec)

iniciome="%s-%s-01" % (fec.year, hoyes.month)

print (iniciome)



fechainicial='2014-03-11'

fechainicial=datetime.strptime(fechainicial,'%Y-%m-%d')

print(fechainicial)


import datetime
import calendar

today=datetime.datetime.now()

dateMonthStart="%s-%s-01" % (today.year, today.month)
dateMonthEnd="%s-%s-%s" % (today.year, today.month, calendar.monthrange(today.year-1, today.month)[1])

print ("primer dia del mes: %s" % dateMonthStart)
print ("segundo dia del mes: %s" % dateMonthEnd)


for i in range(-9, 10):
    print (i)

