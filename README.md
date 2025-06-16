# projetoFIA
# Analisador de Reviews com IA 💬

## Descrição

Aplicação web desenvolvida com **Streamlit** que utiliza a API do Google Generative AI para analisar avaliações e comentários de clientes. O sistema classifica cada review como **Positivo** ou **Negativo** e gera uma justificativa breve para a classificação.

---

## Funcionalidades

- Interface simples e intuitiva para inserir múltiplos reviews.
- Análise automática via modelo de linguagem generativa (Google Gemini).
- Resultado exibido em formato claro e organizado.
- Tratamento de erros e mensagens para chaves inválidas ou ausência de reviews.

---

## Tecnologias

- Python 3.x
- Streamlit
- Google Generative AI (`google.generativeai`)
- python-dotenv (para variáveis de ambiente localmente)
- Git/GitHub para controle de versão

---

## Como usar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/renan013/projetoFIA.git
   cd projetoFIA
Crie e ative um ambiente virtual (Windows):

python -m venv venv
.\venv\Scripts\activate

Instale as dependências:
pip install -r requirements.txt

Crie um arquivo .env na raiz do projeto com a sua chave da API do Google Gemini:

GEMINI_API_KEY="sua_chave_api_aqui"
Rode a aplicação:

streamlit run app.py
Acesse http://localhost:8501 no navegador.

Configuração para deploy no Streamlit Cloud
Faça o push do código para o GitHub.

No painel do Streamlit Cloud, configure a variável secreta (Secret) chamada GEMINI_API_KEY com sua chave da API (no formato TOML, ex: GEMINI_API_KEY="sua_chave_api_aqui").

Certifique-se que o arquivo requirements.txt contenha todas as dependências (incluindo python-dotenv).

Faça deploy/importação do repositório na plataforma Streamlit Cloud.


