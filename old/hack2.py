from datetime import timedelta, datetime

#OLD
def find_time(a,b):
	b = datetime.datetime.strptime(b, '%H:%M')
	b = b.time()
	sum_of_time = 0
	for time in a: # [10,20,30]
		sum_of_time += time
	change_in_time = timedelta(minutes=sum_of_time)
	new_time =  b - change_in_time
	new_time = new_time.strftime('%H:%M')

#NEW
def find_time(a,b):

	b = datetime.strptime(b, '%H:%M')
	sum_of_time = 0
	for time in a: # [10,20,30]
		sum_of_time += time
	change_in_time = timedelta(minutes=-(sum_of_time))
	new_time =  b + change_in_time
	new_time = new_time.strftime('%H:%M')
	#b = b.time()
	return new_time
