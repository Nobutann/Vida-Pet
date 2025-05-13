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
        print("1 - Adicionar")
        print("2 - Visualizar")
        print("3 - Editar")
        print("4 - Excluir")
        print("5 - Gerenciar Metas")
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
                    gerenciar_metas()
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

def salvar_metas(metas):
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
            print(f"{i} - {pet["Nome"] ({pet["Espécie"]})}")

        try:
            idx = int(input("Número para editar: "))

            if 0 <= idx < len(pets):
                pet = pets[idx]
                


        blocks =
    except:
        print("Erro ao salvar")
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
                            peso = input("Digite o peso de pet (em números): ")
                            pet["Peso"] = peso + "kg"
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


def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerenciar_metas():
    while True:
        print("1 - Adicionar meta")
        print("2 - Visualizar metas")
        print("3 - Alterar status de meta")
        print("4 - Excluir meta")
        print("0 - Voltar")
        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida")
            continue
        
        match escolha:
            case 1:
                limpar_terminal()
                meta = input("Descreva a meta: ")
                with open("metas.txt", 'a', encoding="utf-8") as file:
                    file.write(f"Nome: {nome}\nMeta: {meta}\nStatus: Não concluída\n\n")
                print("Meta adicionada com sucesso!\n")
            case 2:
                limpar_terminal()
                try:
                    with open("metas.txt", 'r', encoding="utf-8") as file:
                        print(file.read())
                except FileNotFoundError:
                    print("Nenhuma meta registrada ainda.\n")
            case 3:
                limpar_terminal()
                try:
                    with open("metas.txt", 'r', encoding="utf-8") as file:
                        content = file.read().strip().split("\n\n")
                
                    metas = []
                    for bloco in content:
                        meta_info = {}
                        for linha in bloco.split("\n"):
                            chave, valor = linha.split(": ", 1)
                            meta_info[chave] = valor
                        metas.append(meta_info)

                    for i, meta in enumerate(metas):
                        print(f"{i} - {meta['Nome']} | {meta['Meta']} | Status: {meta['Status']}")
                
                    idx = int(input("Número da meta para alterar status: "))
                    if metas[idx]["Status"] == "Concluída":
                        metas[idx]["Status"] = "Não concluída"
                    else:
                        metas[idx]["Status"] = "Concluída"
                
                    with open("metas.txt", 'w', encoding="utf-8") as file:
                        for meta in metas:
                            for k, v in meta.items():
                                file.write(f"{k}: {v}\n")
                            file.write("\n")
                    print("Status alterado com sucesso!\n")
                    
                except (FileNotFoundError, ValueError, IndexError):
                    print("Erro ao alterar a meta.")
            case 4:
                limpar_terminal()
                try:
                    with open("metas.txt", 'r', encoding="utf-8") as file:
                        content = file.read().strip().split("\n\n")
                
                    metas = []
                    for bloco in content:
                        meta_info = {}
                        for linha in bloco.split("\n"):
                            chave, valor = linha.split(": ", 1)
                            meta_info[chave] = valor
                        metas.append(meta_info)

                    for i, meta in enumerate(metas):
                        print(f"{i} - {meta['Nome']} | {meta['Meta']} | Status: {meta['Status']}")
                
                    idx = int(input("Número da meta para excluir: "))
                    del metas[idx]

                    with open("metas.txt", 'w', encoding="utf-8") as file:
                        for meta in metas:
                            for k, v in meta.items():
                                file.write(f"{k}: {v}\n")
                            file.write("\n")
                    print("Meta excluída com sucesso!\n")
                except (FileNotFoundError, ValueError, IndexError):
                    print("Erro ao excluir meta.")
            case 0:
                break
            case _:
                print("Opção inválida")
                
tela_inicial()            