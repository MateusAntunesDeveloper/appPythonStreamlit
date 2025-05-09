import requests as rt
import streamlit as st

st.set_page_config(page_title="Conversor de Criptomoedas", layout="centered")

st.title("🔄 Conversor de Criptomoedas")

API_KEY = "___API_Key_____"

pares = ["BTCUSDT", "ETHBTC", "LTCBTC", "DOGEUSDT", "BNBBTC"]

par = st.selectbox("Escolha o par de moedas (base/quote)", pares)
quantidade = st.number_input(f"Quantidade de {par[:-3]} para converter", min_value=0.0, step=0.01)


if st.button("Converter"):
    url = f"https://api.api-ninjas.com/v1/cryptoprice?symbol={par}"
    headers = {"X-Api-Key": API_KEY}
    response = rt.get(url, headers=headers)
   
    if response.status_code == 200:
        data = response.json()
        preco_unitario = float(data["price"])
        convertido = preco_unitario * quantidade
        st.success(f"{quantidade} {par[:-3]} = {convertido:.8f} {par[-3:]}")
        st.caption(f"Preço unitário: {preco_unitario:.8f} {par[-3:]}")
    else:
        st.error(f"Erro: {response.status_code} - {response.text}")
