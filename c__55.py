def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print ("division by zero!")
finally:
    print('In finally block for cleanup')
