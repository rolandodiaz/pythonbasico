Python 3.3.5rc1 (v3.3.5rc1:9ec811df548e, Feb 23 2014, 10:43:28) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a=45
>>> b=56
>>> print('su edad es ',a)
su edad es  45
>>> print ('su edad es %d' %a)
su edad es 45
>>> print ('su edad es %i' %a)
su edad es 45
>>> print ('su edad es %f2' %a)
su edad es 45.0000002
>>> print ('su edad es %f' %a)
su edad es 45.000000
>>> print ('su edad es %2f' %a)
su edad es 45.000000
>>> TNA=(((1+0.1149)**(1/12))-1)*(12*365/360)
>>> print (TNA)
0.11077660185869587
>>> cuotaIni
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    cuotaIni
NameError: name 'cuotaIni' is not defined
>>> cuotaIni;
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    cuotaIni;
NameError: name 'cuotaIni' is not defined
>>> cuotaIni=0;
>>> cuotaIni =null
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    cuotaIni =null
NameError: name 'null' is not defined
>>> cuotaIni=true
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    cuotaIni=true
NameError: name 'true' is not defined
>>> cuotaIni=
SyntaxError: invalid syntax
>>> easy_install python-dateutil
SyntaxError: invalid syntax
>>> from dateutil.relativedelta import *
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    from dateutil.relativedelta import *
ImportError: No module named 'dateutil'
>>> import os, sys, time
>>> print time.asctime()
SyntaxError: invalid syntax
>>> print (time.asctime())
Mon Mar 10 20:40:11 2014
>>> print (asctime())
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print (asctime())
NameError: name 'asctime' is not defined
>>> from time import asctime
>>> print (asctime())
Mon Mar 10 20:41:10 2014
>>> from dateutil.relativedelta import *
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    from dateutil.relativedelta import *
  File "C:\Python33\lib\site-packages\dateutil\relativedelta.py", line 12, in <module>
    from six import integer_types
ImportError: No module named 'six'
>>> from dateutil.relativedelta import *
>>> from dateutil.relativedelta import *
>>> from dateutil.relativedelta import *
>>> from dateutil.easter import *
>>> from dateutil.rrule import *
>>> from dateutil.parser import *
>>> from datetime import *
import commands
SyntaxError: multiple statements found while compiling a single statement
>>> from datetime import *
>>> import commands
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    import commands
ImportError: No module named 'commands'
>>> today = date.today()
year = rrule(YEARLY,bymonth=8,bymonthday=16,byweekday=FR)[0].year
rdelta = relativedelta(easter(year), today)
print "Hoy es:", today
print "El próximo año en que el 13 de agosto es viernes es el :", year
print "Faltan %s días para el Día de Pascua." %(rdelta)
print "Pascua de ese año es el %s." %(today+rdelta)
SyntaxError: multiple statements found while compiling a single statement
>>> today = date.today()
>>> year = rrule(YEARLY,bymonth=8,bymonthday=16,byweekday=FR)[0].year
>>> rdelta = relativedelta(easter(year), today)
>>> print "Hoy es:", today
SyntaxError: invalid syntax
>>> print ("Hoy es:", today)
Hoy es: 2014-03-10
>>> print (El próximo año en que el 13 de agosto es viernes es el :", year)
       
SyntaxError: invalid syntax
>>> print ("El próximo año en que el 13 de agosto es viernes es el :", year)
El próximo año en que el 13 de agosto es viernes es el : 2019
>>> print ("Faltan %s días para el Día de Pascua." %(rdelta))
Faltan relativedelta(years=+5, months=+1, days=+11) días para el Día de Pascua.
>>> print ("Pascua de ese año es el %s." %(today+rdelta))
Pascua de ese año es el 2019-04-21.
>>> 

>>> import datetime import *
SyntaxError: invalid syntax
>>> from datetime import  *
>>> fechaval=datetime(input("INGRESE LA FECHA"));
INGRESE LA FECHA2014-03-13
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    fechaval=datetime(input("INGRESE LA FECHA"));
TypeError: an integer is required (got type str)
>>> fechaval=input("INGRESE LA FECHA");
INGRESE LA FECHA2014-03-13
>>> today=fechaval
>>> print("today")
today
>>> print(today)
2014-03-13
>>> print(today+1)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(today+1)
TypeError: Can't convert 'int' object to str implicitly
>>> 
>>> 
>>> 
>>> 
>>> 

>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 
>>> from datetime import *
>>> year = timedelta(days=365)
>>> print(year)
365 days, 0:00:00
>>> year = timedelta(days=360)
>>> print(year)
360 days, 0:00:00
>>> help (timedelta)
Help on class timedelta in module datetime:

class timedelta(builtins.object)
 |  Difference between two datetime values.
 |  
 |  Methods defined here:
 |  
 |  __abs__(...)
 |      x.__abs__() <==> abs(x)
 |  
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |  
 |  __bool__(...)
 |      x.__bool__() <==> x != 0
 |  
 |  __divmod__(...)
 |      x.__divmod__(y) <==> divmod(x, y)
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __floordiv__(...)
 |      x.__floordiv__(y) <==> x//y
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __hash__(...)
 |      x.__hash__() <==> hash(x)
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __mod__(...)
 |      x.__mod__(y) <==> x%y
 |  
 |  __mul__(...)
 |      x.__mul__(y) <==> x*y
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __neg__(...)
 |      x.__neg__() <==> -x
 |  
 |  __pos__(...)
 |      x.__pos__() <==> +x
 |  
 |  __radd__(...)
 |      x.__radd__(y) <==> y+x
 |  
 |  __rdivmod__(...)
 |      x.__rdivmod__(y) <==> divmod(y, x)
 |  
 |  __reduce__(...)
 |      __reduce__() -> (cls, state)
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __rfloordiv__(...)
 |      x.__rfloordiv__(y) <==> y//x
 |  
 |  __rmod__(...)
 |      x.__rmod__(y) <==> y%x
 |  
 |  __rmul__(...)
 |      x.__rmul__(y) <==> y*x
 |  
 |  __rsub__(...)
 |      x.__rsub__(y) <==> y-x
 |  
 |  __rtruediv__(...)
 |      x.__rtruediv__(y) <==> y/x
 |  
 |  __str__(...)
 |      x.__str__() <==> str(x)
 |  
 |  __sub__(...)
 |      x.__sub__(y) <==> x-y
 |  
 |  __truediv__(...)
 |      x.__truediv__(y) <==> x/y
 |  
 |  total_seconds(...)
 |      Total seconds in the duration.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  days
 |      Number of days.
 |  
 |  microseconds
 |      Number of microseconds (>= 0 and less than 1 second).
 |  
 |  seconds
 |      Number of seconds (>= 0 and less than 1 day).
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T
 |  
 |  max = datetime.timedelta(999999999, 86399, 999999)
 |  
 |  min = datetime.timedelta(-999999999)
 |  
 |  resolution = datetime.timedelta(0, 0, 1)

>>> hoy=date.today()
>>> print(hoy)
2014-03-10
>>> mes=hoy.month
>>> print(mes)
3
>>> help(relativedelta)
Help on class relativedelta in module dateutil.relativedelta:

class relativedelta(builtins.object)
 |  The relativedelta type is based on the specification of the excelent
 |  work done by M.-A. Lemburg in his mx.DateTime extension. However,
 |  notice that this type does *NOT* implement the same algorithm as
 |  his work. Do *NOT* expect it to behave like mx.DateTime's counterpart.
 |  
 |  There's two different ways to build a relativedelta instance. The
 |  first one is passing it two date/datetime classes:
 |  
 |      relativedelta(datetime1, datetime2)
 |  
 |  And the other way is to use the following keyword arguments:
 |  
 |      year, month, day, hour, minute, second, microsecond:
 |          Absolute information.
 |  
 |      years, months, weeks, days, hours, minutes, seconds, microseconds:
 |          Relative information, may be negative.
 |  
 |      weekday:
 |          One of the weekday instances (MO, TU, etc). These instances may
 |          receive a parameter N, specifying the Nth weekday, which could
 |          be positive or negative (like MO(+1) or MO(-2). Not specifying
 |          it is the same as specifying +1. You can also use an integer,
 |          where 0=MO.
 |  
 |      leapdays:
 |          Will add given days to the date found, if year is a leap
 |          year, and the date found is post 28 of february.
 |  
 |      yearday, nlyearday:
 |          Set the yearday or the non-leap year day (jump leap days).
 |          These are converted to day/month/leapdays information.
 |  
 |  Here is the behavior of operations with relativedelta:
 |  
 |  1) Calculate the absolute year, using the 'year' argument, or the
 |     original datetime year, if the argument is not present.
 |  
 |  2) Add the relative 'years' argument to the absolute year.
 |  
 |  3) Do steps 1 and 2 for month/months.
 |  
 |  4) Calculate the absolute day, using the 'day' argument, or the
 |     original datetime day, if the argument is not present. Then,
 |     subtract from the day until it fits in the year and month
 |     found after their operations.
 |  
 |  5) Add the relative 'days' argument to the absolute day. Notice
 |     that the 'weeks' argument is multiplied by 7 and added to
 |     'days'.
 |  
 |  6) Do steps 1 and 2 for hour/hours, minute/minutes, second/seconds,
 |     microsecond/microseconds.
 |  
 |  7) If the 'weekday' argument is present, calculate the weekday,
 |     with the given (wday, nth) tuple. wday is the index of the
 |     weekday (0-6, 0=Mon), and nth is the number of weeks to add
 |     forward or backward, depending on its signal. Notice that if
 |     the calculated date is already Monday, for example, using
 |     (0, 1) or (0, -1) won't change the day.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, other)
 |  
 |  __bool__(self)
 |  
 |  __div__(self, other)
 |  
 |  __eq__(self, other)
 |  
 |  __init__(self, dt1=None, dt2=None, years=0, months=0, days=0, leapdays=0, weeks=0, hours=0, minutes=0, seconds=0, microseconds=0, year=None, month=None, day=None, weekday=None, yearday=None, nlyearday=None, hour=None, minute=None, second=None, microsecond=None)
 |  
 |  __mul__(self, other)
 |  
 |  __ne__(self, other)
 |  
 |  __neg__(self)
 |  
 |  __radd__(self, other)
 |  
 |  __repr__(self)
 |  
 |  __rsub__(self, other)
 |  
 |  __sub__(self, other)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> |          be positive or negative (like MO(+1) or MO(-2). Not specifying
				    
SyntaxError: invalid syntax
>>> print(hoy)
2014-03-10
>>> diasf=relativedelta((hoy.month+1),hoy)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    diasf=relativedelta((hoy.month+1),hoy)
  File "C:\Python33\lib\site-packages\dateutil\relativedelta.py", line 117, in __init__
    raise TypeError("relativedelta only diffs datetime/date")
TypeError: relativedelta only diffs datetime/date
>>> 
