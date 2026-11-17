import os
from dotenv import load_dotenv
from google import genai
from google.genai import types, errors

load_dotenv()
client = genai.Client()

mensagem_cliente = """
Olá, bom dia! Comprei uma licença do sistema ontem (pedido #4829), 
o pagamento já caiu no cartão, mas quando tento fazer login aparece 
'Usuário não autorizado'. Preciso liberar isso urgente porque minha 
equipe começa a operar hoje às 14h!
"""

prompt = f"""
Você é um assistente de triagem de suporte técnico.
Analise a mensagem do cliente abaixo e retorne um JSON com:
- "categoria": (Financeiro, Acesso, Bug Técnico ou Dúvida)
- "prioridade": (Baixa, Média ou Alta)
- "resumo": resumo do problema em 1 frase curta
- "resposta_sugerida": resposta educada e objetiva para o cliente

Mensagem do cliente:
{mensagem_cliente}
"""

# Obtém automaticamente os modelos Gemini disponíveis na sua conta
modelos_disponiveis = [
    m.name for m in client.models.list()
    if "gemini" in m.name and not any(x in m.name for x in ["embedding", "image", "tts", "audio"])
]

for modelo in modelos_disponiveis:
    try:
        print(f"A tentar processar com {modelo}...")
        response = client.models.generate_content(
            model=modelo,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
            ),
        )
        print("\nResultado da triagem:")
        print(response.text)
        break
    except errors.APIError as e:
        print(f"Modelo {modelo} indisponível (erro {e.code}). A tentar o próximo...")