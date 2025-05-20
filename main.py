import os, time, datetime
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
        print(f"5 - Gerenciar metas")
        print(f"6 - Registrar evento")
        print(f"7 - Gerar Sugestões Personalizadas de Cuidados")
        print(f"8 - Quantidade de pets")
        print(f"0 - Fechar Programa")
        try:
            opcao = int(input())
        
            match opcao:
                case 1:
                    limpar_terminal()
                    adicionar()
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
                    limpar_terminal()
                case 4:
                    limpar_terminal()
                    deletar()
                    limpar_terminal()
                case 5:
                    limpar_terminal()
                    gerenciar_metas()
                case 6:
                    limpar_terminal()
                    registrar_evento()
                case 7:
                    limpar_terminal()
                    selecionar_sugestao()
                case 8:
                    contar_pets()
                case 0:
                    limpar_terminal()
                    break
                case _:
                    print("Seleção inválida")
        except ValueError:
            print("Valor inválido")
            input()
            limpar_terminal()

def adicionar():
    pet = {"Nome": "",
           "Espécie": "",
           "Raça": "",
           "Data de nascimento": "",
           "Peso": ""}

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
                while True:
                    print("Insira no formato (dd/mm/aaaa)")
                    try:
                        data = input()
                        datetime.datetime.strptime(data, "%d/%m/%Y")
                        pet["Data de nascimento"] = data
                        break
                    except ValueError:
                        print("Formato inválido. Use dd/mm/aaaa")

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

def salvar_dados(pet):
    try:
        with open("dados pet.txt", 'a', encoding="utf-8", newline="") as file:
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
            print(f"{i} - {pet['Nome']} ({pet['Espécie']})")

        try:
            idx = int(input("Pet para editar: "))

            if 0 <= idx < len(pets):
                pet = pets[idx]
                while True:
                    limpar_terminal()
                    print("1 - Editar nome")
                    print("2 - Editar espécie")
                    print("3 - Editar raça")
                    print("4 - Editar data de nascimento")
                    print("5 - Editar peso")
                    print("0 - Salvar e voltar")

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
                print("Esse pet não existe.")
        except ValueError:
            print("Erro")
        
        with open("dados pet.txt", 'w', newline="", encoding="utf-8") as file:
            for pet in pets:
                for key, value in pet.items():
                    file.write(f"{key}: {value}\n")
                file.write("\n")

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
            print(f"{i} - {pet['Nome']} ({pet['Espécie']})")

        print("Escolha o pet")
        print('Pressione "V" para voltar')

        answer = input()
        if answer.lower() == "v":
            pass
        else:
            idx = int(input())
            if 0 <= idx < len(pets):
                del pets[idx]
            else:
                print("Esse pet não existe.")
        
        with open("dados pet.txt", 'w', newline="", encoding="utf-8") as file:
            for pet in pets:
                for key, value in pet.items():
                    file.write(f"{key}: {value}\n")
                file.write("\n")
    
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
            print(f'{i} - {pet["Nome"]} ({pet["Espécie"]})')

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
                                coletar_evento("=== Vacinação ===", pet)
                            case 2:
                                limpar_terminal()
                                coletar_evento("=== Consulta Veterinária ===", pet)
                            case 3:
                                limpar_terminal()
                                coletar_evento("=== Aplicação de Remédio ===", pet)
                            case 0:
                                limpar_terminal()
                                break
                            case _:
                                print("Opção inválida.")
                    except ValueError:
                        print("Valor inválido.")
        except ValueError:
            print("Valor inválido")

    except FileNotFoundError:
        print('Arquivo não existe, tente "Adicionar" primeiro.')
    
def coletar_evento(tipo_evento, pet):
    date = ""
    obs = ""

    while True:
        print(tipo_evento)
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
                    if date and obs:
                        print("Salvo com sucesso!")
                        events = {"Nome": pet["Nome"],
                                  "Data": date,
                                  "Observações": obs}
                        salvar_eventos(events, tipo_evento)
                        break
                    else:
                        print("Preencha todos os campos antes de salvar.")
                case 0:
                    limpar_terminal()
                    break
                case _:
                    print("Opção inválida.")
        except ValueError:
            print("Valor inválido.")

def selecionar_sugestao():
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
            print(f'{i} - {pet["Nome"]} ({pet["Espécie"]})')

        try:
            idx = int(input())
            limpar_terminal()
            if 0 <= idx < len(pets):
                pet = pets[idx]

                while True:
                    print("1 - Brinquedos Ideais")
                    print("2 - Alimentos Recomendados")
                    print("3 - Exercícios Adequados")
                    print("4 - Outros Cuidados")
                    print("0 - Voltar")

                    option = int(input())

                    match option:
                        case 1:
                            limpar_terminal()
                            sugestao_selecionada("=== Brinquedos Ideais ===", pet) 
                        case 2:
                            limpar_terminal()
                            sugestao_selecionada("=== Alimentos Recomendados ===", pet)
                        case 3:
                            limpar_terminal()
                            sugestao_selecionada("=== Exercícios Adequados ===", pet)
                        case 4:
                            limpar_terminal()
                            sugestao_selecionada("=== Outros Cuidados ===", pet)
                        case 0:
                            limpar_terminal()
                            break
                        case _:
                            print("Opção Inválida.")

        except ValueError:
            print("Valor Inválido.")
    except ValueError:
            print("Valor Inválido.")

def sugestao_selecionada(tipo_sugestao, pet):
    data_nascimento = pet["Data de nascimento"]
    dia, mes, ano = map(int, data_nascimento.split('/'))
    data_nascimento = datetime.datetime(ano, mes, dia)
    data_atual = datetime.datetime.now()
    idade = data_atual.year - data_nascimento.year - (
        (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day)
    )

    especie_entrada = pet["Espécie"].strip().capitalize()

    especie_mapa = {
        "Cachorro": "Cão",
        "Cão": "Cão",
        "Gato": "Gato",
        "Coelho": "Coelho",
        "Hamster": "Hamster",
        "Ave": "Ave"
    }

    especie = especie_mapa.get(especie_entrada, "Desconhecido")
    faixa = ""

    if especie == "Desconhecido":
        limpar_terminal()
        print(f"Espécie '{especie_entrada}' não reconhecida.")
        input("\nPressione Enter para continuar...")
        limpar_terminal()
        return

    if especie in ["Cão", "Gato"]:
        if idade < 1:
            faixa = "Filhote"
        elif idade < 7:
            faixa = "Adulto"
        else:
            faixa = "Idoso"
    elif especie == "Coelho":
        if idade < 1 and (data_atual - data_nascimento).days < 183:
            faixa = "Filhote"
        elif idade < 5:
            faixa = "Adulto"
        else:
            faixa = "Idoso"
    elif especie == "Hamster":
        if idade < 1 and (data_atual - data_nascimento).days < 183:
            faixa = "Filhote"
        elif idade < 2:
            faixa = "Adulto"
        else:
            faixa = "Idoso"
    elif especie == "Ave":
        if idade < 1:
            faixa = "Filhote"
        elif idade < 8:
            faixa = "Adulto"
        else:
            faixa = "Idoso"

    sugestoes = {
        "Cão": {
            "Filhote": {
                "=== Brinquedos Ideais ===": "Mordedores de borracha, brinquedos macios",
                "=== Alimentos Recomendados ===": "Ração premium para filhotes, rica em DHA",
                "=== Exercícios Adequados ===": "Caminhadas leves, brincadeiras curtas",
                "=== Outros Cuidados ===": "Vacinação, vermifugação, socialização precoce"
            },
            "Adulto": {
                "=== Brinquedos Ideais ===": "Bola, frisbee, brinquedos interativos",
                "=== Alimentos Recomendados ===": "Ração balanceada para adultos",
                "=== Exercícios Adequados ===": "Caminhadas diárias, adestramento, correr",
                "=== Outros Cuidados ===": "Controle de pulgas/carrapatos, check-ups"
            },
            "Idoso": {
                "=== Brinquedos Ideais ===": "Brinquedos mentais, pelúcias",
                "=== Alimentos Recomendados ===": "Ração sênior com condroitina/glucosamina",
                "=== Exercícios Adequados ===": "Caminhadas leves, estimulação mental",
                "=== Outros Cuidados ===": "Avaliação ortopédica, cuidados dentários"
            }
        },
        "Gato": {
            "Filhote": {
                "=== Brinquedos Ideais ===": "Varinhas com penas, bolinhas leves",
                "=== Alimentos Recomendados ===": "Ração para filhotes rica em proteínas e taurina",
                "=== Exercícios Adequados ===": "Subir e descer móveis, caça simulada",
                "=== Outros Cuidados ===": "Castração, vacinação, arranhadores"
            },
            "Adulto": {
                "=== Brinquedos Ideais ===": "Brinquedos interativos, laser, túneis",
                "=== Alimentos Recomendados ===": "Ração premium com controle de peso",
                "=== Exercícios Adequados ===": "Brincadeiras diárias, enriquecimento ambiental",
                "=== Outros Cuidados ===": "Escovação de pelos, vermifugação"
            },
            "Idoso": {
                "=== Brinquedos Ideais ===": "Brinquedos lentos, almofadas aromatizadas",
                "=== Alimentos Recomendados ===": "Ração sênior de fácil digestão",
                "=== Exercícios Adequados ===": "Atividades leves, observação em janelas seguras",
                "=== Outros Cuidados ===": "Monitoramento renal, cuidados articulares"
            }
        },
        "Coelho": {
            "Filhote": {
                "=== Brinquedos Ideais ===": "Tubos de papelão, bolas de feno",
                "=== Alimentos Recomendados ===": "Feno à vontade, ração para filhotes, vegetais leves",
                "=== Exercícios Adequados ===": "Espaço seguro para pulos, exploração supervisionada",
                "=== Outros Cuidados ===": "Castração precoce, socialização"
            },
            "Adulto": {
                "=== Brinquedos Ideais ===": "Túnel de tecido, blocos para roer",
                "=== Alimentos Recomendados ===": "Feno, verduras frescas, ração equilibrada",
                "=== Exercícios Adequados ===": "Tempo diário fora da gaiola, enriquecimento ambiental",
                "=== Outros Cuidados ===": "Vacinação (VHD/Mixomatose), controle de unhas"
            },
            "Idoso": {
                "=== Brinquedos Ideais ===": "Brinquedos calmos, mordedores leves",
                "=== Alimentos Recomendados ===": "Feno, vegetais macios, ração sênior leve",
                "=== Exercícios Adequados ===": "Movimentos suaves, acesso fácil aos recursos",
                "=== Outros Cuidados ===": "Monitoramento dental, avaliação articular"
            }
        },
        "Hamster": {
            "Filhote": {
                "=== Brinquedos Ideais ===": "Roda de exercícios, túneis",
                "=== Alimentos Recomendados ===": "Ração para roedores, pequenas frutas e legumes",
                "=== Exercícios Adequados ===": "Esconderijos, escalada leve",
                "=== Outros Cuidados ===": "Limpeza diária da gaiola, cuidado com temperatura"
            },
            "Adulto": {
                "=== Brinquedos Ideais ===": "Labirintos, blocos para roer",
                "=== Alimentos Recomendados ===": "Mix de sementes, proteína ocasional (ovo cozido)",
                "=== Exercícios Adequados ===": "Atividades noturnas, exploração em ambiente seguro",
                "=== Outros Cuidados ===": "Observação de comportamento, rotação de brinquedos"
            },
            "Idoso": {
                "=== Brinquedos Ideais ===": "Materiais suaves, brinquedos com pouco esforço",
                "=== Alimentos Recomendados ===": "Alimento macio, menos sementes oleaginosas",
                "=== Exercícios Adequados ===": "Movimentação reduzida, espaço acolchoado",
                "=== Outros Cuidados ===": "Acesso fácil à comida e água, supervisão veterinária"
            }
        },
        "Ave": {
            "Filhote": {
                "=== Brinquedos Ideais ===": "Espelhos, guizos, balanços",
                "=== Alimentos Recomendados ===": "Ração extrusada para filhotes, frutas e verduras",
                "=== Exercícios Adequados ===": "Voo supervisionado (se possível), interação social",
                "=== Outros Cuidados ===": "Anilhamento, adaptação gradual ao ambiente"
            },
            "Adulto": {
                "=== Brinquedos Ideais ===": "Brinquedos coloridos, desafios cognitivos",
                "=== Alimentos Recomendados ===": "Ração extrusada balanceada, frutas, sementes com moderação",
                "=== Exercícios Adequados ===": "Voo diário, socialização com humanos/outros pássaros",
                "=== Outros Cuidados ===": "Banho de sol, enriquecimento com galhos naturais"
            },
            "Idoso": {
                "=== Brinquedos Ideais ===": "Brinquedos com texturas variadas, de fácil acesso",
                "=== Alimentos Recomendados ===": "Ração leve, alimentos fáceis de digerir",
                "=== Exercícios Adequados ===": "Exercícios suaves com supervisão",
                "=== Outros Cuidados ===": "Avaliações regulares, prevenção de bico e penas"
            }
        }
    }

    limpar_terminal()
    print(f"Espécie: {especie}")
    
    if idade < 1:
        meses = (data_atual.year - data_nascimento.year) * 12 + (data_atual.month - data_nascimento.month)
        if data_atual.day < data_nascimento.day:
            meses -= 1
        print(f"Idade: {meses} meses ({faixa})")
    else:
        print(f"Idade: {idade} anos ({faixa})")

    print(tipo_sugestao)
    print("\nSugestão personalizada:")
    try:
        sugestao = sugestoes[especie][faixa][tipo_sugestao]
        print(f"> {sugestao}")
    except KeyError:
        print("Informação indisponível.")

    input("\nPressione Enter para continuar...")
    limpar_terminal()

def gerenciar_metas():
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
            print(f'{i} - {pet["Nome"]} ({pet["Espécie"]})')

        try:
            idx = int(input())
            if 0 <= idx < len(pets):
                pet = pets[idx]
            else:
                print("Pet não existe.")
        except ValueError:
            print("Valor inválido")

        metas = []
        limpar_terminal()
        while True:
            print("1 - Adicionar meta")
            print("2 - Visualizar metas")
            print("0 - Salvar e Voltar")

            try:
                choice = int(input())
            except ValueError:
                print("Inválido")

            match choice:
                case 1:
                    limpar_terminal()
                    meta = input()
                    metas.append(meta.strip())
                case 2:
                    limpar_terminal()
                    try:
                        with open("metas.txt", 'r', encoding="utf-8") as file:
                            lines = file.read().splitlines()
                        block = []
                        show = False
                        for line in lines + [""]:
                            if line.startswith("Pet: "):
                                show = (line == f"Pet: {pet['Nome']}")
                            if show and line:
                                block.append(line)
                            elif show and not line:
                                break
                        if block:
                            print("Metas:\n")
                            print("\n".join(block))
                        else:
                            print("Nenhuma meta para esse pet.")
                    except FileNotFoundError:
                        print("Adicione uma meta primeiro.")
                case 0:
                    limpar_terminal()
                    break
                case _:
                    print("Inválido")

        if metas:
            with open("metas.txt", 'a', encoding="utf-8") as file:
                file.write(f"Pet: {pet['Nome']}\n")
                for meta in metas:
                    file.write(f"Meta: {meta}\n")
                file.write("\n")
        else:
            print("Nenhuma adicionada")
        
    except FileNotFoundError:
        print('Arquivo não existe. Tente "Adicionar" primeiro.')

def contar_pets():
    try:
        with open("dados pet.txt", 'r', encoding="utf-8") as file:
            lines = file.readlines()
            cont = 0
            for line in lines:
                if line.strip().startswith("Nome:"):
                    cont += 1
            print(f"Você tem {cont} pets cadastrados")
    except FileNotFoundError:
        print('O arquivo não existe. Tente "Adicionar" primeiro.')

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

tela_inicial()
