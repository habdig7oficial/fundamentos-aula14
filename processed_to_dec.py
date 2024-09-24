valor = input() 


def bin_to_dec(valor: str,): 
	dec = 0 
	i = 0 
	while i < len(valor): 
		if int(valor[i]) == 1: 
			dec += 2 ** (len(valor) - (i + 1)) 
			print(f"DEC: {dec} {len(valor)} - {i + 1}") 

		i += 1 

	return dec 



print(bin_to_dec(valor)) 
