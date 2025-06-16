import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

# --- Configurações Iniciais ---
st.set_page_config(
    page_title="Analisador de Reviews",
    page_icon="💬",
    layout="centered"
)

# --- Carregamento da chave da API ---
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configuração da API do Google Gemini
try:
    if not api_key:
        raise ValueError("Chave da API não encontrada. Verifique o arquivo .env.")
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    st.error(f"Erro ao configurar a API do Google. Verifique sua chave. Detalhes: {e}")
    st.stop()

# --- Título e Instruções ---
st.title("Analisador de Reviews com IA 💬")
st.markdown("Cole abaixo os comentários ou avaliações de clientes. A IA irá classificá-los como **positivos** ou **negativos** com uma justificativa para cada.")

# --- Entrada do Usuário ---
avaliacoes = st.text_area(
    "Cole aqui os reviews (uma por linha):",
    height=200,
    placeholder="Exemplo:\nO atendimento foi excelente!\nO produto chegou quebrado..."
)

botao_analise = st.button("Analisar Reviews", use_container_width=True)

# --- Processamento e Resposta da IA ---
if botao_analise:
    avaliacoes_lista = [linha.strip() for linha in avaliacoes.strip().split('\n') if linha.strip()]

    if not avaliacoes_lista:
        st.warning("Por favor, insira a review para análise, se houver mais de uma coloque uma abaixo da outra")
    else:
        prompt = f"""
Você é um analista de Reviews. Classifique cada review a seguir como **Positivo** ou **Negativo**. Em seguida, forneça uma breve justificativa (1 a 2 linhas) explicando o motivo da classificação com base nas palavras e contexto do review.

Reviews:
{chr(10).join([f"{i+1}. {rev}" for i, rev in enumerate(avaliacoes_lista)])}

Formato da resposta:
Número. Classificação: Positivo/Negativo  
Justificativa: (motivo da classificação)
"""
        with st.spinner("Analisando Reviews..."):
            try:
                response = model.generate_content(prompt)
                st.markdown("---")
                st.subheader("Resultado da Análise")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Houve um problema ao gerar a análise. Detalhes: {e}")
