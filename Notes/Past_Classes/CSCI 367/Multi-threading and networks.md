### Thread
threading library in python

demo:
```
import threading
def func1():
	for i in range (1,11):
		print(i)

def func2():
	for i in range (1,11):
		print(i)

def func3():
	for i in range (1,11):
		print(i)
def main():
	#create threads
	t1 = threading.Thread(target=func1)
	t2 = threading.Thread(target=func2)
	t3 = threading.Thread(target=func3)
	
	t1.start()
	t2.start()
	t3.start()

	t1.join()
	t2.join()
	t3.join()

	print("All threads are done")

if __name__ == "__main__":
	main()
```

### Lock

used when updating a global shared resource

```
import threading

#Shared resources
account_balance = 100
balance_lock = threading.Lock()

def widthdraw(amount)
	global account_balance
	with balance_lock:
		current_balance = account_balance
		current_balance -= amount
		account_balance = current balance

def deposit(amount)
	global account_balance
	with balance_lock:
		current_balance = account_balance
		current_balance += amount
		account_balance = current balance

def main():
	t1 = threading.Thread(target=withdraw, args(50,))
	t2 = threading.Thread(target=withdraw, args(30,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()
	print("Both threads have finished")

if __name__ == "__main__":
	main()

```
