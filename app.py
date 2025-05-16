import os, time

def tela_inicial():
    start = \
    """       ██╗   ██╗██╗██████╗  █████╗     ██████╗ ███████╗████████╗
       ██║   ██║██║██╔══██╗██╔══██╗    ██╔══██╗██╔════╝╚══██╔══╝
       ██║   ██║██║██║  ██║███████║    ██████╔╝█████╗     ██║   
       ╚██╗ ██╔╝██║██║  ██║██╔══██║    ██╔═══╝ ██╔══╝     ██║   
        ╚████╔╝ ██║██████╔╝██║  ██║    ██║     ███████╗   ██║   
         ╚═══╝  ╚═╝╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚══════╝   ╚═╝"""

    for line in start.splitlines():
        print(line)
        time.sleep(0.2)

    input("\nPressione Enter para continuar...")
    limpar_terminal()
    menu()

def menu():
    while True:
        print(f"1 - Adicionar")
        print(f"2 - Visualizar")
        print(f"3 - Editar")
        print(f"4 - Excluir")
        print(f"5 - Registrar evento")
        print(f"0 - Fechar Programa")
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
                        try:
                            add = int(input())
                        except ValueError:
                            print("Inválido")
                            continue
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
                                salvar_dados(pet)
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
                        try:
                            voltar = int(input())
                        except ValueError:
                            print("Inválido")
                            continue
                        if voltar == 0:
                            limpar_terminal()
                            break
                        else:
                            print("Seleção inválida")
                case 3:
                    limpar_terminal()
                    editar_arquivos()
                    input()
                    limpar_terminal()
                case 4:
                    limpar_terminal()
                    deletar()
                    input()
                    limpar_terminal()
                case 5:
                    limpar_terminal()
                    registrar_evento()
                case 0:
                    limpar_terminal()
                    break
                case _:
                    print("Seleção inválida")
        except ValueError:
            print("Valor inválido")
            input()
            limpar_terminal()

def salvar_dados(pet):
    try:
        with open("dados pet.txt", 'a', newline="", encoding="utf-8") as file:
            for key, value in pet.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")
    except:
        print("Erro ao salvar.")

def salvar_eventos(events, tipo_evento):
    with open("eventos.txt", 'a', encoding="utf-8") as file:
        file.write(f"{tipo_evento}\n")
        for key, value in events.items():
            file.write(f"{key}: {value}\n")
        file.write("\n")
def visualizar_arquivos():
    try:
        with open("dados pet.txt", 'r', newline="", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print("Não existe nenhum arquivo ainda, tente utilizar o \"Adicionar\" primeiro.")

def editar_arquivos():
    try:
        with open("dados pet.txt", 'r', newline="", encoding="utf-8") as file:
            content = file.read().strip()

        blocks = content.split("\n\n")
        pets = []

        for block in blocks:
            pet = {}
            lines = block.split("\n")
            for line in lines:
                key, value = line.split(": ", 1)
                pet[key] = value
            
            pets.append(pet)
        
        for i, pet in enumerate(pets):
            print(f"{i} - {pet["Nome"]} ({pet["Espécie"]})")

        try:
            idx = int(input("Número para editar: "))
            
            if 0 <= idx < len(pets):
                pet = pets[idx]
                while True:
                    limpar_terminal()
                    print("1 - Editar nome")
                    print("2 - Editar espécie")
                    print("3 - Editar raça")
                    print("4 - Editar data de nascimento")
                    print("5 - Editar peso")
                    print("0 - Salvar")

                    option = int(input())

                    match option:
                        case 1:
                            limpar_terminal()
                            pet["Nome"] = input()
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
                        case 0:
                            break
                        case _:
                            print("Inválido")
            else:
                print("Indíce inválido")
        except ValueError:
            print("Erro")
        
        with open("dados pet.txt", 'w', newline="", encoding="utf-8") as file:
            for pet in pets:
                for key, value in pet.items():
                    file.write(f"{key}: {value}\n")
                file.write("\n")

        print("Informações atualizadas")
        print("Pressione Enter para continuar...")

    except FileNotFoundError:
        print("Arquivo não existe")    

def deletar():
    try:
        with open("dados pet.txt", 'r', newline="", encoding="utf-8") as file:
            content = file.read().strip()
 
        blocks = content.split("\n\n")
        pets = []

        for block in blocks:
            pet = {}
            lines = block.split("\n")
            
            for line in lines:
                key, value = line.split(": ", 1)
                pet[key] = value

            pets.append(pet)

        for i, pet in enumerate(pets):
            print(f"{i} - {pet["Nome"]} ({pet["Espécie"]})")
        
        try:
            idx = int(input("Número para excluir: "))

            del pets[idx]
        except ValueError:
            print("Valor Inválido")
        
        with open("dados pet.txt", 'w', newline="", encoding="utf-8") as file:
            for pet in pets:
                for key, value in pet.items():
                    file.write(f"{key}: {value}\n")

        print("Informações atualizadas")
        print("Pressione Enter para continuar...")
    
    except FileNotFoundError:
        print("Arquivo não encontrado")

def registrar_evento():
    try:
        with open("dados pet.txt", 'r', encoding="utf-8") as file:
            content = file.read().strip()

        blocks = content.split("\n\n")
        pets = []

        for block in blocks:
            pet = {}
            lines = block.split("\n")
            
            for line in lines:
                key, value = line.split(": ", 1)
                pet[key] = value
            
            pets.append(pet)

        for i, pet in enumerate(pets):
            print(f"{i} - {pet["Nome"]} ({pet["Espécie"]})")

        try:
            idx = int(input())
            limpar_terminal()

            if 0 <= idx < len(pets):
                pet = pets[idx]

                while True:
                    print("1 - Registrar vacinações")
                    print("2 - Registrar consultas veterinárias")
                    print("3 - Registrar aplicação de remédios")
                    print("0 - Voltar")

                    try:
                        choice = int(input())
                        match choice:
                            case 1:
                                limpar_terminal()

                                while True:
                                    print("=== Vacinação ===")
                                    print("1 - Data")
                                    print("2 - Observações")
                                    print("3 - Salvar")
                                    print("0 - Voltar")

                                    try:
                                        escolha = int(input())

                                        match escolha:
                                            case 1:
                                                limpar_terminal()
                                                date = input()
                                            case 2:
                                                limpar_terminal()
                                                obs = input()
                                            case 3:
                                                limpar_terminal()
                                                print("Salvo com sucesso!")
                                                tipo = "=== Vacinação ==="
                                                events = {"Nome": pet["Nome"],
                                                          "Data": date,
                                                          "Observações": obs}
                                                
                                                salvar_eventos(events, tipo)
                                            case 0:
                                                limpar_terminal()
                                                break
                                            case _:
                                                print("Opção inválida.")

                                    except ValueError:
                                        print("Valor inválido.")

                            case 2:
                                limpar_terminal()
                                while True:
                                    print("=== Consulta Veterinária ===")
                                    print("1 - Data")
                                    print("2 - Observações")
                                    print("3 - Salvar")
                                    print("0 - Voltar")
                                    
                                    try:
                                        escolha = int(input())

                                        match escolha:
                                            case 1:
                                                limpar_terminal()
                                                date = input()
                                            case 2:
                                                limpar_terminal()
                                                obs = input()
                                            case 3:
                                                limpar_terminal()
                                                tipo = "===Consulta Veterinária==="
                                                events = {"Nome": pet["Nome"],
                                                          "Data": date,
                                                          "Observação": obs}
                                                salvar_eventos(events, tipo)
                                            case 0:
                                                limpar_terminal()
                                                break
                                            case _:
                                                print("Opção inválida")
                                    except ValueError:
                                        print("Valor inválido")
                            case 3:
                                limpar_terminal()
                                while True:
                                    print("=== Aplicação de Remédios ===")
                                    print("1 - Data")
                                    print("2 - Observações")
                                    print("3 - Salvar")
                                    print("0 - Voltar")

                                    try:
                                        escolha = int(input())

                                        match escolha:
                                            case 1:
                                                limpar_terminal()
                                                date = input()
                                            case 2:
                                                limpar_terminal()
                                                obs = input()
                                            case 3:
                                                limpar_terminal()
                                                tipo = "===Aplicação de Remédios==="
                                                events = {"Nome": pet["Nome"],
                                                          "Data": date,
                                                          "Observações": obs}
                                                salvar_eventos(events, tipo)
                                            case 0:
                                                limpar_terminal()
                                                break
                                            case _:
                                                print("Opção inválida")
                                    except ValueError:
                                        print("Valor inválido.")
                            case 0:
                                limpar_terminal()
                                break
                    except ValueError:
                        print("Valor inválido.")

                    except ValueError:
                        print("Valor inválido.")
        except ValueError:
            print("Valor inválido")

    except FileNotFoundError:
        print("Arquivo não existe, tente \"Adicionar\" primeiro.")

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

tela_inicial()