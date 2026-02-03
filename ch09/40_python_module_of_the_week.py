# 40_python_module_of_the_week.py

# 9-16. Python Module of the Week: Once excellent resource for exploring the
# Python standard library is a site called Python Module of the Week. Go to
# https://pymotw.com/ and look at the table of contents. Find a module that
# looks interesting to you and read about it, perhaps starting with the random
# module.

# datetime -- Date/time value manipulation

# Purpose: The datetime module includes functions and classes for doing date
# and time parsing, formatting, and arithmetic.

# Avaliable In: 2.3 and later

# datetime contains functions and classes for working with dates and times,
# separately and together.

# Times

# Time values are represented with the time class. Times have attributes for
# hour, minute, second, and microsecond. They can also include time zone
# information. The arguments to initialize a time instance are optional, but the
# default of 0 is unlikely to be what you want.

import datetime

t = datetime.time(1, 2, 3)
print(t)
print(f"hour : {t.hour}")
print(f"minute : {t.minute}")
print(f"second : {t.second}")
print(f"microsecond : {t.microsecond}")
