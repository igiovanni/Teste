conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 1500 
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque Realizado com Sucesso!!")
    elif saque <= (saldo + cheque_especial):
        print("Saque Realizado com Sucesso Utilizando Cheque Especial!!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente")   

elif conta_universitaria:   
    if saldo >= saque:
        print("Saque Realizado com Sucesso!!")  
    else:
        print("Saldo Insuficiente!!")     

elif conta_especial:
    print("Conta especial foi selecionada!!")        

else: 
    print("Conta selecionada não reconhecido, entre em contato com sua gerência!!")


    