def circulo():
    raio = int(input("Digite qual é o raio: "))
    resultado = 3.14 * (raio * raio)
    print(f"{resultado}")
def triangulo():
    base = float(input("Digite qual é a base: "))
    altura = float(input("Digite qual é a altura: "))
    resultado = (base * altura) / 2
    print({resultado})
def quadrado():
    lado = float(input("Digite qual é o lado: "))
    resultado = lado * lado 
    print({resultado})
def retangulo():
    base = float(input("Digite qual é a base: "))
    altura = float(input("Digite qual é a altura: "))
    resultado = base * altura
    print({resultado})
def paralelogramo():
    base = float(input("Digite qual é a base: "))
    altura = float(input("Digite qual é a altura: "))
    resultado = base * altura
    print({resultado})
def losango():
    maior = float(input("Digite a diagonal maior: "))
    menor = float(input("Digite a diagonal menor: "))
    resultado = (maior * menor) / 2
    print({resultado})
def trapezio():
    maior = float(input("Digite a base maior: "))
    menor = float(input("Digite a base menor: "))
    altura = float(input("Digite a altura: "))
    resultado = (maior + menor) * altura / 2
    print({resultado})








while True:
    print ("Qual forma vc quer calcular a área?")
    print ("1 - circulo")
    print ('2 - triângulo')
    print ('3 - quadrado')
    print ('4 - retângulo')
    print ('5 - paralelogramo')
    print ('6 - losango')
    print ('7 - trapézio')
    print ('0 - sair')

    opcao = input('Escolha uma opção:')

    if opcao == "1":
        circulo()
    elif opcao == "2":
        triangulo()
    elif opcao == "3":
        quadrado()
    elif opcao == "4":
        retangulo()
    elif opcao == "5":
        paralelogramo()
    elif opcao == "6":
        losango()
    elif opcao == "7":
        trapezio()
    elif opcao == "0":
        print ("Saindo do sistema...")
        break
    else:
        print ("Opção invalida, tente novamente!!!")