import random
import os


def num_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def gerar_primo(min, max):
    while True:
        numero = random.randint(min, max)
        if num_primo(numero):
            return numero

def calculo_mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gerar_chaves():
    print("Gerando chaves...")
    p1 = gerar_primo(1000, 5000)
    p2 = gerar_primo(1000, 5000)

    while p1 == p2:
        p2 = gerar_primo(1000, 5000)

    n = p1 * p2
    phi = (p1-1) * (p2-1)

    pu = random.randrange(2, phi)
    while calculo_mdc(pu, phi) != 1:
        pu = random.randrange(2, phi)

    pr = pow(pu, -1, phi)

    return (pu, n), (pr, n)


def encriptar(texto, chave):
    expoente, n = chave
    numeros_cifrados = [pow(ord(letra), expoente, n) for letra in texto]
    return numeros_cifrados

def decriptar(numeros_cifrados, chave):
    expoente, n = chave
    texto = "".join([chr(pow(numero, expoente, n)) for numero in numeros_cifrados])
    return texto


def ler_texto(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        return f.read()

def salvar_texto(nome_arquivo, texto):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(texto)

def ler_numeros(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()
        return [int(x) for x in conteudo.split(',')]

def salvar_numeros(nome_arquivo, numeros):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(",".join(map(str, numeros)))
    

def main():
    print("=== INICIANDO SISTEMA DE CRIPTOGRAFIA DE CHAVES ASSIMÉTRICAS ===")
    print("Gerando chaves para esta sessão...")
    chave_publica, chave_privada = gerar_chaves()
    print(f"Chave Pública gerada: {chave_publica}")
    print(f"Chave Privada gerada: {chave_privada}\n")

    while True:
        print("--------------------------------------------------")
        print("Escolha uma opção:")
        print("1. Encriptar um arquivo (Confidencialidade)")
        print("2. Decriptar um arquivo (Confidencialidade)")
        print("3. Assinar um arquivo (Autenticidade)")
        print("4. Verificar assinatura (Autenticidade)")
        print("5. Sair")
        
        opcao = input("Opção: ")

        if opcao == '5':
            print("Encerrando o programa...")
            break

        if opcao not in ['1', '2', '3', '4']:
            print("Opção inválida. Tente novamente.")
            continue

        arquivo_entrada = input("Digite o nome do arquivo de origem (ex: meu_texto.txt): ")
        
        if not os.path.exists(arquivo_entrada):
            print(f"ERRO: O arquivo '{arquivo_entrada}' não foi encontrado na pasta atual.")
            continue

        arquivo_saida = input("Digite o nome do arquivo para salvar o resultado (ex: resultado.txt): ")

        try:
            if opcao == '1':
                texto = ler_texto(arquivo_entrada)
                dados_encriptados = encriptar(texto, chave_publica)
                salvar_numeros(arquivo_saida, dados_encriptados)
                print(f"Sucesso! Arquivo encriptado salvo em '{arquivo_saida}'.")

            elif opcao == '2':
                dados_encriptados = ler_numeros(arquivo_entrada)
                texto_decriptado = decriptar(dados_encriptados, chave_privada)
                salvar_texto(arquivo_saida, texto_decriptado)
                print(f"Sucesso! Arquivo decriptado salvo em '{arquivo_saida}'.")

            elif opcao == '3':
                texto = ler_texto(arquivo_entrada)
                dados_assinados = encriptar(texto, chave_privada)
                salvar_numeros(arquivo_saida, dados_assinados)
                print(f"Sucesso! Arquivo assinado salvo em '{arquivo_saida}'.")

            elif opcao == '4':
                dados_assinados = ler_numeros(arquivo_entrada)
                texto_verificado = decriptar(dados_assinados, chave_publica)
                salvar_texto(arquivo_saida, texto_verificado)
                print(f"Sucesso! Arquivo verificado salvo em '{arquivo_saida}'.")

        except Exception as e:
            print(f"Ocorreu um erro ao processar o arquivo: {e}")
            print("Verifique se você escolheu a opção correta para o tipo de arquivo (texto puro vs arquivo encriptado).")



if __name__ == "__main__":
    main()