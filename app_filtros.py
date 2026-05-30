import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
    "Vendas": [120, 145, 98, 200, 175, 230],
    "Clientes": [40, 55, 35, 80, 70, 95]
})


# titulo da pagina 
st.title("Painel de Vendas")
# um texto simples
st.write("Resumo dos últimos 6 meses")

st.subheader("Dados brutos")
st.dataframe(df, use_container_width=True)

# grafico de barras com Plotly
st.subheader("Vendas por mês")
fig_bar = px.bar(df, x="Mês", y="Vendas")
st.plotly_chart(fig_bar, use_container_width=True)

# grafico de linha
st.subheader("Tendência de clientes")
fig_line = px.line(df, x="Mês", y="Clientes", markers=True)
st.plotly_chart(fig_line, use_container_width=True)

# filtro de mes 
mes = st.selectbox("Mês", df.Mês.unique())
df_filtrado = df[df['Mês'] == mes]
st.dataframe(df_filtrado)

# grafico de barras filtrado
st.subheader("Vendas por mês - Filtro Selectbox")
fig_filtrado = px.bar(df_filtrado, x="Mês", y="Vendas")
st.plotly_chart(fig_filtrado, use_container_width=True)

# filtro de vendas usando slider 
minimo = st.slider(
    "Vendas mínimas",
    min_value=0,
    max_value=230,
    value=100
)

filtrado = df[df.Vendas >= minimo]
st.dataframe(filtrado) 

st.subheader("Vendas por mês - Filtro Slider")
fig_filtrado_slider = px.bar(filtrado, x="Mês", y="Vendas")
st.plotly_chart(fig_filtrado_slider, use_container_width=True)


# Multiselect 
meses = st.multiselect(
    "Selecione os Meses",
    options=df["Mês"].tolist(),
    default=["Jan", "Fev"]
)

if meses:
    multfiltro = df[df["Mês"].isin(meses)]
    st.dataframe(multfiltro)
else:
    st.warning("Selecione ao menos um mês.")
    

st.subheader("Vendas por mês - Filtro Multiselect")
fig_filtrado_multiselect = px.bar(multfiltro, x="Mês", y="Vendas")
st.plotly_chart(fig_filtrado_multiselect, use_container_width=True)