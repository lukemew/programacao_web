import os
from util import calcular_media  # Importa função do módulo util.py

def ler_dados_arquivo(nome_arquivo):

    if not os.path.exists(nome_arquivo):
        raise FileNotFoundError(f"Arquivo '{nome_arquivo}' não encontrado.")
    
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    
    clientes = []
    for linha in linhas:
        nome, cidade, idade, renda = linha.strip().split(';')
        clientes.append({
            'nome': nome,
            'cidade': cidade,
            'idade': int(idade),
            'renda': float(renda),
        })
    return clientes

def calcular_estatisticas(clientes):

    idades = [cliente['idade'] for cliente in clientes]
    rendas = [cliente['renda'] for cliente in clientes]
    
    media_idade = calcular_media(idades)
    media_renda = calcular_media(rendas)
    return media_idade, media_renda

def main():
    nome_arquivo = 'clientes.txt'
    try:
        clientes = ler_dados_arquivo(nome_arquivo)
        media_idade, media_renda = calcular_estatisticas(clientes)
        print(f"Média de idade: {media_idade:.2f} anos")
        print(f"Média de renda mensal: R$ {media_renda:.2f}")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
