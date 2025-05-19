# Vida Pet

**Vida Pet** é um sistema em Python que permite gerenciar informações de animais de estimação via terminal.  
Você pode cadastrar pets, editar dados, registrar eventos (como vacinações ou consultas), gerenciar metas e receber sugestões de cuidados personalizados.

## Funcionalidades

1. Adicionar pets (nome, espécie, raça, data de nascimento, peso)  
2. Visualizar todos os pets cadastrados  
3. Editar informações dos pets  
4. Excluir pets do sistema  
5. Gerenciar metas
6. Registrar eventos importantes:  
   - Vacinações  
   - Consultas veterinárias  
   - Aplicação de remédios  
7. Gerar sugestões personalizadas de cuidados com base na espécie e idade do pet  

## Armazenamento

Os dados são armazenados localmente em arquivos `.txt`:  
- `dados pet.txt` – Armazena os dados de cada pet  
- `eventos.txt` – Registra eventos vinculados aos pets
- `metas.txt` - Registra as metas atuais

## Como usar

1. Clone este repositório ou copie os arquivos do projeto.  
2. Execute o script principal.
3. Use o menu para navegar entre as funcionalidades.

---

## Requisitos

- Python 3.8 ou superior  
- Sistema compatível com terminal/console

---

## Observações

- As sugestões de cuidados são baseadas na espécie (cão, gato, coelho, etc.) e idade do pet (filhote, adulto, idoso).  
- O sistema é totalmente baseado em leitura/escrita de arquivos `.txt`.

---

## Exemplos de uso

Ao iniciar o sistema, aparecerá um menu assim:
```plaintext
1 - Adicionar  
2 - Visualizar  
3 - Editar  
4 - Excluir
5 - Gerenciar metas  
6 - Registrar evento  
7 - Gerar Sugestões Personalizadas de Cuidados  
0 - Fechar Programa  
```
Para usar, digite o número correspondente à opção desejada e pressione Enter.

1 - **Adicionar**: Cadastre um novo pet no sistema.
    _Cadastre todas as informações do pet, sem faltar **nenhuma**_

2 - **Visualizar**: Veja a lista dos pets cadastrados e seus detalhes.

3 - **Editar**: Modifique as informações de um pet existente.

4 - **Excluir**: Remova um pet do sistema.

5 - **Gerenciar metas**: Defina ou revise metas de cuidado para seus pets.

6 - **Registrar evento**: Anote eventos importantes relacionados ao pet, como consultas ou vacinas.

7 - **Gerar Sugestões Personalizadas de Cuidados**: Receba recomendações baseadas na espécie e idade do pet.

0 - **Fechar Programa**: Encerre o sistema com segurança.
