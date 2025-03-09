def pertenceFibonacci(n):
    if n < 0:
        return False

    a, b = 0, 1
    while a < n:
        a, b = b, a + b

    return a == n

teste = int(input("Digite um número: "))

if pertenceFibonacci(teste):
    print(f"{teste} esta na sequencia")
else:
    print(f"{teste} nao esta na sequencia")
