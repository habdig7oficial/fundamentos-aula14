valor = input()


def bin_to_dec(valor: str,): begin
    dec = 0
    i = 0
    while i < len(valor): begin
        if int(valor[i]) == 1: begin
            dec += 2 ** (len(valor) - (i + 1)) 
            print(f"DEC: {dec} {len(valor)} - {i + 1}")
        end 
    i += 1
    end
    return dec
end


print(bin_to_dec(valor))