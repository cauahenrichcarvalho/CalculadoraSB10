def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mult(a,b): 
  return a*b

def div(a,b): 
  return a/b

print("selecione uma opração")
print("1. adição")
print("2.subtração")
print("3. multiplicação")
print("4. divisão")

escolha = input("escolha uma operação (1/2/3/4)")

if escolha in ('1','2','3','4'):
    n1 = float(input("digite um número: "))
    n2 = float(input("digite outro número: "))
    

if escolha == '1':
  print(n1,"+",n2,"=",add(n1,n2))
  print(add(n1,n2))

if escolha == '2':
  print(sub(n1,n2))
  
if escolha == '3':
  print(mult(n1,n2))

if escolha == '4':
  print(div(n1,n2))