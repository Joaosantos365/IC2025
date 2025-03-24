import streamlit as st

st.title("Inversor de Frases")

frase = st.text_input("Digite uma frase:")

if st.button("Inverter frase"):
    if frase:
        frase_invertida = frase[::-1]
        st.write("Frase invertida:", frase_invertida)
    else:
        st.write("Por favor, digite uma frase para inverter.")