# Dicionário para armazenar os usuários
# A chave será o e-mail, e o valor será outro dicionário com nome e senha
usuarios = {}

# Função para registrar um novo usuário
def registrar_usuario():
    print("\n--- Registro de Usuário ---")  # Exibe o título com uma quebra de linha antes

    # Solicita dados do usuário
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    senha = input("Digite a senha: ")

    # Verifica se o e-mail já foi cadastrado
    if email in usuarios:
        print("❌ Email já cadastrado!\n")
    else:
        # Adiciona o usuário ao dicionário
        usuarios[email] = {"nome": nome, "senha": senha}
        print("✅ Usuário registrado com sucesso!\n")

# Função para logar um usuário já cadastrado
def login_usuario():
    print("\n--- Login de Usuário ---")  # Exibe o título

    # Solicita e-mail e senha
    email = input("Digite o email: ")
    senha = input("Digite a senha: ")

    # Verifica se o e-mail existe e se a senha está correta
    if email in usuarios and usuarios[email]["senha"] == senha:
        print(f"✅ Bem-vindo(a), {usuarios[email]['nome']}!\n")  # Mensagem de boas-vindas
    else:
        print("❌ Email ou senha incorretos!\n")  # Erro no login

# Função para exibir todos os usuários cadastrados
def exibir_usuarios():
    print("\n--- Lista de Usuários ---")  # Título

    # Verifica se o dicionário está vazio
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
    else:
        # Percorre o dicionário e exibe os dados
        for email, dados in usuarios.items():
            print(f"Nome: {dados['nome']}, Email: {email}")
        print()  # Quebra de linha ao final

# Função principal com o menu interativo
def menu():
    while True:  # Loop infinito até o usuário escolher sair
        # Exibe o menu de opções
        print("=== Sistema de Cadastro ===")
        print("1. Registrar usuário")
        print("2. Fazer login")
        print("3. Exibir usuários")
        print("4. Sair")

        # Captura a opção do usuário
        escolha = input("Escolha uma opção: ")

        # Chama a função correspondente à escolha
        if escolha == "1":
            registrar_usuario()
        elif escolha == "2":
            login_usuario()
        elif escolha == "3":
            exibir_usuarios()
        elif escolha == "4":
            print("👋 Encerrando o programa...")
            break  # Sai do loop e encerra o programa
        else:
            print("❌ Opção inválida!\n")  # Mensagem de erro para opção inválida

# Inicia o programa executando o menu
menu()
