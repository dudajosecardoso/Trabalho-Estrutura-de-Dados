from Calculadora import*

def menu():
    print("-------------------------")
    print("\033[0;34mBEM VINDO AO MENU PRINCIPAL\033[m")
    print("1. Calcular uma expressão")
    print("2. Sair do sistema")
    opc = int(input("Digite a ação que deseja realizar: "))

    return opc

def main():
    while True:
        opc = menu()
        try:
            if opc == 1:
                expression= str(input("Digite a Expressão: "))
                result = calculate(expression)
                print(f'Resultado: {result}')
            
            if opc == 2:
                print("Obrigado por usar nossa aplicação. Volte sempre!")
                break

        except ValueError:
            print("Você não digitou uma opção válida!")
            return opc

if __name__== '__main__':
    main()
    hfhffhf
