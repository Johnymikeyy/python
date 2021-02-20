try:
    x = 4 / 1
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')


#output
Nothing went wrong


#################

try:
	x = 3 / 0
except:
	print('Something went wrong')
finally:
	print('Always execute this')
 
 #output
 
Something went wrong
Always execute this


################

try:
    x = 2/0
except ZeroDivisionError:
    print('Attempt to divide by zero')
except:
    print('Something else went wrong')
    
    #output
    Attempt to divide by zero

 