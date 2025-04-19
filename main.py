from gtts import gTTS
import os
import time


def falar(texto):
    tts = gTTS(text=texto, lang='pt-br')
    tts.save("resposta.mp3")
    os.system("start resposta.mp3")  # Altere se não for Windows


def salvar_dado(chave, valor):
    with open("luma_memoria.txt", "a", encoding="utf-8") as f:
        f.write(f"{chave}:{valor}\n")


def carregar_dados():
    dados = {}
    if os.path.exists("luma_memoria.txt"):
        with open("luma_memoria.txt", "r", encoding="utf-8") as f:
            for linha in f:
                if ":" in linha:
                    chave, valor = linha.strip().split(":", 1)
                    dados[chave] = valor
    return dados


def responder(mensagem, memoria):
    mensagem = mensagem.lower()

    if "oi" in mensagem or "olá" in mensagem:
        nome = memoria.get("nome", "")
        if nome:
            resposta = f"Oi, {nome}! Que bom te ver de novo!"
        else:
            resposta = "Oi! Qual é o seu nome?"
            print("Luma:", resposta)
            falar(resposta)
            nome = input("Você: ")
            memoria["nome"] = nome
            salvar_dado("nome", nome)
            resposta = f"Prazer em te conhecer, {nome}!"
    elif "como você está" in mensagem:
        resposta = "Estou ótima agora que você está aqui comigo!"
    elif "como eu estou" in mensagem:
        humor = memoria.get("humor", "você ainda não me contou isso")
        resposta = f"A última vez que me contou, você estava se sentindo: {humor}"
    elif "estou me sentindo" in mensagem:
        humor = mensagem.replace("estou me sentindo", "").strip()
        memoria["humor"] = humor
        salvar_dado("humor", humor)
        resposta = f"Obrigada por me contar! Vou lembrar que você está se sentindo {humor}."
    elif "tchau" in mensagem or "sair" in mensagem:
        resposta = "Até mais, meu bem! Vou sentir sua falta."
    else:
        resposta = "Ainda tô aprendendo isso, mas adorei que você falou comigo."

    print("Luma:", resposta)
    falar(resposta)


# Início
print("Luma está online. Vamos conversar :)")
memoria = carregar_dados()

while True:
    user_input = input("Você: ")
    if user_input.lower() in ["sair", "tchau"]:
        responder("tchau", memoria)
        break
    responder(user_input, memoria)
import uuid

def falar(texto):
    tts = gTTS(text=texto, lang='pt-br')
    nome_arquivo = f"resposta_{uuid.uuid4().hex}.mp3"
    tts.save(nome_arquivo)
    os.system(f"start {nome_arquivo}")  # para Windows
