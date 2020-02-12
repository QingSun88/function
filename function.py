#function是用来【收纳】程式码的
#它是个功能

def wash(dry= False, water= 8):
	print('add water', water, 'deep')
	print('add washing powder')
	print('turning')
	if dry:
		print('drying clothes')

wash(True) 
wash(False)   #使用function
wash(water= 10)  #强调参数值

def add(x, y):
	print(x + y) #function可以有多个参数

def add(x=0, y=1):  #function可以有预设值
	print(x + y)

add(5)   #function 的参数是依次设定
add(y=4) #function 的参数可以强制给


#return回传功能
def add(x, y):
	return x + y
result = add(3, 4)  #只有return之后才能把结果存下来 
print(result)

def average(numbers):
	return sum(numbers) / len(numbers)

print(average([23,45,98]))
