def somaDupla(nums, alvo):
    num_do_indice = {}
    
    for num_atual, num in enumerate(nums):
        complemento = alvo - num
        
        if complemento in num_do_indice:
            return [num_do_indice[complemento], num_atual]
        
        num_do_indice[num] = num_atual
        
        
nums = [1,5,4,7,9]
target = 16
print(somaDupla(nums, target))