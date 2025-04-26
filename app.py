import os

def menu():
    while True:
        print("1 - Adicionar")
        print("2 - Visualizar")
        print("3 - Editar")
        print("4 - Excluir")
        print("0 - Fechar Programa")
        try:
            opcao = int(input())
        
            match opcao:
                case 1:
                    limpar_terminal()
                    pet = {
                        "Nome": "",
                        "Espécie": "",
                        "Raça": "",
                        "Data de nascimento": "",
                        "Peso": ""
                    }

                    while True:
                        print("1 - Adicionar nome")
                        print("2 - Adicionar espécie")
                        print("3 - Adicionar raça")
                        print("4 - Adicionar data de nascimento")
                        print("5 - Adicionar peso")
                        print("6 - Salvar")
                        print("0 - Voltar")
                        add = int(input())
                        match add:
                            case 1:
                                limpar_terminal()
                                pet["Nome"]= input()
                            case 2:
                                limpar_terminal()
                                pet["Espécie"] = input()
                            case 3:
                                limpar_terminal()
                                pet["Raça"] = input()
                            case 4:
                                limpar_terminal()
                                pet["Data de nascimento"] = input()
                            case 5:
                                limpar_terminal()
                                pet["Peso"] = input()
                            case 6:
                                salvar_arquivos(pet)
                                limpar_terminal()
                                break
                            case 0:
                                limpar_terminal()
                                break
                            case _:
                                print("Seleção inválida")
                case 2:
                    limpar_terminal()
                    while True:
                        visualizar_arquivos()
                        print("\nClique \"0\" para voltar")
                        voltar = int(input())
                        if voltar == 0:
                            limpar_terminal()
                            break
                        else:
                            print("Seleção inválida")
                case 3:
                    pass
                case 4:
                    pass
                case 0:
                    limpar_terminal()
                    break
                case _:
                    print("Seleção inválida")
        except ValueError:
            print("Valor inválido")
            input()
            limpar_terminal()

def salvar_arquivos(pet):
    try:
        with open("dados pet.txt", 'a', newline="", encoding="utf-8") as file:
            for key, value in pet.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")
    except:
        print("Erro ao salvar.")
def visualizar_arquivos():
    try:
        with open("dados pet.txt", 'r', newline="", encoding="utf-8") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Não existe nenhum arquivo ainda, tente utilizar o \"Adicionar\" primeiro.")
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

menu()