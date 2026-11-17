# Triador Automático de Chamados com IA

Script em Python integrado à API do Google Gemini para automatizar a triagem inicial de mensagens de suporte técnico, transformando textos não estruturados em dados prontos para integração com sistemas e fluxos de automação.

## O Problema
Equipes de atendimento e suporte técnico perdem tempo precioso lendo mensagens longas e desorganizadas para identificar o assunto, definir a urgência e redigir uma primeira resposta ao cliente.

## A Solução
Este projeto recebe a mensagem original do cliente e utiliza Inteligência Artificial Generativa para:
- **Classificar a categoria** do chamado (`Financeiro`, `Acesso`, `Bug Técnico` ou `Dúvida`);
- **Definir a prioridade** de atendimento (`Baixa`, `Média` ou `Alta`);
- **Resumir o problema** em uma frase objetiva;
- **Gerar uma resposta sugerida** pronta para envio.

## Diferenciais Técnicos
- **Saída Estruturada (JSON):** Uso de `response_mime_type="application/json"` para garantir que a resposta da IA possa ser consumida diretamente por bancos de dados, webhooks ou ferramentas como n8n e Make.
- **Resiliência e Fallback Automático:** Consulta dinâmica aos modelos disponíveis na conta (`client.models.list()`) com tratamento de exceções (`errors.APIError`), alternando automaticamente entre modelos caso algum esteja indisponível ou sobrecarregado.
- **Segurança de Credenciais:** Uso de variáveis de ambiente (`.env`) isoladas pelo `.gitignore` para evitar exposição da chave de API no repositório.

## Tecnologias Utilizadas
- **Python 3**
- **Google GenAI SDK** (`google-genai`)
- **Python Dotenv** (`python-dotenv`)

## Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
git clone https://github.com/Tsyuuna/triador-chamados-ia.git
   ```

2. **Instale as dependências:**
   ```bash
   pip install google-genai python-dotenv
   ```

3. **Configure sua chave de API:**
   Crie um arquivo `.env` na raiz do projeto e adicione sua chave gerada no Google AI Studio:
   ```env
   GEMINI_API_KEY=sua_chave_api_aqui
   ```

4. **Execute o script:**
   ```bash
   python triagem.py
   ```

## Exemplo de Saída

```json
{
  "categoria": "Acesso",
  "prioridade": "Alta",
  "resumo": "Usuário não consegue acessar o sistema após a compra da licença, apresentando erro de permissão.",
  "resposta_sugerida": "Olá! Lamentamos o inconveniente. Verificamos seu pedido #4829 e nossa equipe técnica já está priorizando a liberação do seu acesso para que sua equipe possa iniciar as operações às 14h. Entraremos em contato em breve com a confirmação."
}
```
