import threading 
x = 0 # global variable x

def increment(lock):
	# function to increment global variable x
	lock.acquire()
	global x 
	x += 1
	lock.release()

def thread_task(lock):
	# task for thread 
	for _ in range(100000):
		increment(lock)


def main_task():

	global x
	x = 0 # setting global variable x as 0 

	# creating threads
	lock=threading.Lock()
	t1 = threading.Thread(target=increment,args=(lock,))
	t2 = threading.Thread(target=increment,args=(lock,))

	# start threads 
	t1.start() 
	t2.start() 

	# wait until threads finish their job 
	t1.join()
	t2.join()

if __name__ == "__main__": 
	for i in range(10): 
		main_task() 
		print("Iteration {0}: x = {1}".format(i,x)) 