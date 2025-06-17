import json
import difflib
from datetime import datetime  # 👈 novo

def responder(pergunta_usuario):
    pergunta_usuario = pergunta_usuario.lower().strip()

    with open('data/base_conhecimento.json', 'r', encoding='utf-8') as f:
        conhecimento = json.load(f)

    if pergunta_usuario in conhecimento:
        resposta = conhecimento[pergunta_usuario]
    else:
        perguntas_conhecidas = list(conhecimento.keys())
        parecidas = difflib.get_close_matches(pergunta_usuario, perguntas_conhecidas, n=1, cutoff=0.6)

        if parecidas:
            pergunta_mais_provavel = parecidas[0]
            resposta = conhecimento[pergunta_mais_provavel]
        else:
            resposta = "Desculpe, não entendi sua pergunta. Tente reformular."

    # 👇 SALVA A PERGUNTA E RESPOSTA NO HISTÓRICO
    with open("historico.txt", "a", encoding="utf-8") as log:
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        log.write(f"[{agora}] Pergunta: {pergunta_usuario}\n")
        log.write(f"[{agora}] Resposta: {resposta}\n\n")

    return resposta
