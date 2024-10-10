# Função para verificar se um número pertence à sequência de Fibonacci
def pertence_fibonacci(num):
    if num < 0:
        return False
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or num == 0  # Verifica se num é 0 ou igual a b
num_verificar = int(input("Digite o número que você deseja verificar: "))
if pertence_fibonacci(num_verificar):
    print(f"{num_verificar} pertence à sequência de Fibonacci.")
else:
    print(f"{num_verificar} NÃO pertence à sequência de Fibonacci.")
