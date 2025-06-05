# titulo
# input
# a cada mensagem enviada:
    # mostrar a mensagem que o usuario enviou
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

# streamlit - frontend e backend

import streamlit as st
import time

st.title("Site teste")
st.write("Ola mundo")

msg_usuario = st.chat_input("Escreva sua mensagem aqui")

time.sleep(1)

if msg_usuario:
    print(msg_usuario)
    # user -> ser humano
    # assistant -> IA
    st.chat_message("user").write(msg_usuario)

    # resposta da IA
    resp_ia = "Vc quis dizer: " + msg_usuario

    # exibir a resposta da IA na tela
    st.chat_message("assistant").write(resp_ia)