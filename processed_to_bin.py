valor = int(input()) 


def dec_to_bin(number: int): 
	quo = number 
	res = 0 
	bin_arr = [] 
	while quo != 0 : 
		res = quo % 2 
		quo //= 2 

		print(f"{quo} - {res} ") 

		#bin_arr[i - 1] = res 

		bin_arr.insert(0, res) 

	return "".join([str(i) for i in bin_arr]) 


print(dec_to_bin(valor)) 
