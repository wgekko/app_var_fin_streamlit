import requests
import streamlit as st
from streamlit_lottie import st_lottie
import base64
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn import linear_model, tree, neighbors


import warnings
warnings.simplefilter("ignore", category=FutureWarning)


#Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Financial Analysis", page_icon=":📊:", layout="wide")

#----imagen en background y sider ---
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
    }
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background("images/main.jpg")

st.markdown("""
        <header>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Kalam:wght@300&family=Lobster&display=swap" rel="stylesheet">
        </header>
        <style>
            font-family: 'Kalam', cursive;
            font-family: 'Lobster', sans-serif;
        </style>
    """, unsafe_allow_html=True)


st.sidebar.image("images/grafico.gif", caption="Walter Gomez Financial Consultant")
st.sidebar.image("images/grafico1-1.gif", caption="Walter Gomez Financial Consultant")
st.sidebar.image("images/grafico1.gif", caption="Walter Gomez Financial Consultant")
st.sidebar.image("images/grafico2.gif", caption="Walter Gomez Financial Consultant")
st.sidebar.image("images/grafico3.gif", caption="Walter Gomez Financial Consultant")
st.sidebar.image("images/grafico4.gif", caption="Walter Gomez Financial Consultant")
st.sidebar.image("images/grafico5.gif", caption="Walter Gomez Financial Consultant")
st.sidebar.image("images/grafico6.gif", caption="Walter Gomez Financial Consultant")
st.sidebar.image("images/grafico7.gif", caption="Walter Gomez Financial Consultant")


st.markdown(
    """
<style>
sidebar  {
    background-image: ('images/sider.jpg'));
}
</style>
""",
    unsafe_allow_html=True,
)

# despliegue de imagen lottier
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# despliegue de archivo gif
file_ = open("images/data.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- Carga de componentes ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# ---- cabecera de la pagina  ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Análisis de Variables Financieras 📈")
        st.subheader("variables para el análisis son :")
        st.subheader(
            "Dólar Blue, Dólar CCL, Dólar Mep, Dólar Crypto, Indice Merval, Tasa Plazo Fijo, Inflación(ind. de precio minorista/mayorista)."
        )
        st.write("Fuente: BCRA, BYMA, ambito financiero ." )
    with right_column:
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" width="500"  alt="analisis gif">',
            unsafe_allow_html=True,
        )

# ---- Descripcion de la pagina----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("En la barra lateral accedemos :" )
        st.subheader("- Gráficos de Evolución Variables (diario)")
        st.subheader("- Gráficos Evol. Nominal vs Evol. inflación (mensual)")
        st.subheader("- Gráficos de Variables Deflactadas (mensual)")
        st.subheader("- Gráficos de rentabilidad y volatilidad (mensual)")
        st.subheader("- Gráficos de predicción de rentabilidad-animaciones de rendimientos (mensual)")
    with right_column:
        st.write("#")
        st_lottie(lottie_coding, height=300, key="coding")


# ---- Descripcion de la pagina primera pagina de evol de variables diario----
df = pd.read_excel('assets/dolar_blue.xlsx')

list_option = ['Dólar Blue', 'Dólar CCL', 'Dólar MEP', 'Dólar CRYPTO', 'Ind Merval', 'Plazo Fijo']
option = st.radio("Seleccione una opción : ", (list_option), horizontal=True )

st.write("---")
st.subheader(f"Evolución del valor Diario de :  {option} (nominal)")

if option == 'Plazo Fijo':
    st.write('el valor para las tasas de Plazo Fijo,  están expresado en % mensual (periodo diario)')

st.write("Se grafica con streamlit y con plotly debido a que se puede manipular el gráfico de alternativas distintas ")
st.write("---")
st.write("usando streamlit")
st.line_chart(
    df,
    x='fecha',
    y= option ,
    color="#FF0000",
  )
st.write("---")
st.write("usando plotly")
fig= px.line(
    df,
    x='fecha',
    y= option,
    #markers=True
)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

# ---- Descripcion de la segunda pagina de evol de variables nominal vs inflacion mensual----

df1 = pd.read_excel('assets/dolar_blue1.xlsx')

#list_option = ['Dólar Blue', 'Dólar CCL', 'Dólar MEP', 'Dólar CRYPTO', 'Ind Merval', 'Plazo Fijo']
#option = st.radio("Seleccione una opción : ",(list_option), horizontal=True )

st.write("---")
st.subheader(f"Evolución de {option} vs evolución de IPC/IPM (Mensual - nominal)")

# ---- DOLAR BLUE ----
if option == 'Dólar Blue':
    st.write("Se grafica con streamlit y con plotly debido a que se puede manipular el gráfico de alternativas distintas ")
    st.write("---")
    st.write("usando streamlit")
    st.line_chart(
        df1,
        x='meses',
        y= ['IPC', 'IPM', option],
        color=["#FF0000", '#0000FF','#00FF00']
    )
    st.write("---")
    st.write("usando plotly")
    fig1= px.line(
        df1,
        x='meses',
        y=['IPC', 'IPM', option],
        markers=True
    )
    st.plotly_chart(fig1, use_container_width=True)


# ---- DOLAR CCL ----
elif option == 'Dólar CCL':
    st.write("Se grafica con streamlit y con plotly debido a que se puede manipular el gráfico de alternativas distintas ")
    st.write("---")
    st.write("usando streamlit")
    st.line_chart(
        df1,
        x='meses',
        y= ['IPC', 'IPM', option],
        color=["#FF0000", '#0000FF','#00FF00']
    )
    st.write("---")
    st.write("usando plotly")
    fig1= px.line(
        df1,
        x='meses',
        y=['IPC', 'IPM', option],
        markers=True
    )
    st.plotly_chart(fig1, use_container_width=True)

# ---- DOLAR MEP ----
elif option == 'Dólar MEP':
    st.write("Se grafica con streamlit y con plotly debido a que se puede manipular el gráfico de alternativas distintas ")
    st.write("---")
    st.write("usando streamlit")
    st.line_chart(
        df1,
        x='meses',
        y= ['IPC', 'IPM', option],
        color=["#FF0000", '#0000FF','#00FF00']
        )
    st.write("---")
    st.write("usando plotly")
    fig1= px.line(
        df1,
        x='meses',
        y=['IPC', 'IPM', option],
        markers=True
        )
    st.plotly_chart(fig1, use_container_width=True)

# ---- DOLAR CRYPTO ----
elif option == 'Dólar CRYPTO':
    st.write("Se grafica con streamlit y con plotly debido a que se puede manipular el gráfico de alternativas distintas ")
    st.write("---")
    st.write("usando streamlit")
    st.line_chart(
        df1,
        x='meses',
        y= ['IPC', 'IPM', option],
        color=["#FF0000", '#0000FF','#00FF00']
    )
    st.write("---")
    st.write("usando plotly")
    fig1= px.line(
        df1,
        x='meses',
        y=['IPC', 'IPM', option],
        markers=True
    )
    st.plotly_chart(fig1, use_container_width=True)

# ---- MERVAL ----
elif option == 'Ind Merval':

    st.write("---")
    st.write("usando streamlit")
    st.line_chart(
        df1,
        x='meses',
        y= ['IPC', 'IPM', option],
        color=["#FF0000", '#0000FF','#00FF00']
    )
    st.write("---")
    st.write("usando plotly")
    fig1= px.line(
        df1,
        x='meses',
        y=['IPC', 'IPM', option],
        markers=True
    )
    st.plotly_chart(fig1, use_container_width=True)

# ---- PFIJO ----
elif option == 'Plazo Fijo':
    st.write('el valor % de Plazo Fijo, están expresado en % mensual (periodo diario)- capitalización mensual')
    st.write("Se grafica con streamlit y con plotly debido a que se puede manipular el gráfico de alternativas distintas ")
    st.write("---")
    st.write("usando streamlit")
    st.line_chart(
        df1,
        x='meses',
        y= ['IPC', 'IPM', option],
        color=["#FF0000", '#0000FF','#00FF00']
    )
    st.write("---")
    st.write("usando plotly")
    fig1= px.line(
        df1,
        x='meses',
        y=['IPC', 'IPM', option],
        markers=True
    )
    st.plotly_chart(fig1, use_container_width=True)

else:
    st.write("Error, en la opción elegida ")

# ---- Descripcion de la tercera pagina de evol de variables descontada la inflacion mensual----

df2 = pd.read_excel('assets/dolar_blue2.xlsx')
st.subheader(f"Evolución del Valor de : {option} descontado inflación (IPC)")
st.write('periodo mensual expresado en base=100 dic/2019')
st.write("Se grafica con streamlit y con plotly debido a que se puede manipular el gráfico de alternativas distintas ")
st.write("---")
st.write("usando streamlit")
# --- DOLAR BLUE ---
if option == 'Dólar Blue':
    st.line_chart(
        df2,
        x= 'meses',
        y= option,
        color="#FF0000",
    )
    st.write("usando plotly")
    fig= px.line(
        df2,
        x='meses',
        y= option,
        markers=True
    )
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

# --- DOLAR CCL ---
elif option == 'Dólar CCL':
    st.line_chart(
        df2,
        x= 'meses',
        y= option,
        color="#FF0000",
    )
    st.write("usando plotly")
    fig= px.line(
        df2,
        x='meses',
        y= option,
        markers=True
    )
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

# --- DOLAR MEP ---
elif option == 'Dólar MEP':
    st.line_chart(
        df2,
        x= 'meses',
        y= option,
        color="#FF0000",
    )
    st.write("usando plotly")
    fig= px.line(
        df2,
        x='meses',
        y= option,
        markers=True
    )
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

# --- DOLAR CRYPTO ---
elif option == 'Dólar CRYPTO':
    st.line_chart(
        df2,
        x= 'meses',
        y= option,
        color="#FF0000",
    )
    st.write("usando plotly")
    fig= px.line(
        df2,
        x='meses',
        y= option,
        markers=True
    )
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

# --- MERVAL ---
elif option == 'Ind Merval':
    st.line_chart(
        df2,
        x= 'meses',
        y= option,
        color="#FF0000",
    )
    st.write("usando plotly")
    fig= px.line(
        df2,
        x='meses',
        y= option,
        markers=True
    )
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

# --- PFIJO ---
elif option == 'Plazo Fijo':
    st.line_chart(
        df2,
        x= 'meses',
        y= option,
        color="#FF0000",
    )
    st.write("usando plotly")
    fig= px.line(
        df2,
        x='meses',
        y= option,
        markers=True
    )
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

else:
   st.write("Error, en la opción elegida")

# ---- Descripcion de la cuarta pagina de evol de variables descontada la inflacion mensual----

df3 = pd.read_excel('assets/dolar_blue3.xlsx')

#list_option = ['Dólar Blue', 'Dólar CCL', 'Dólar MEP', 'Dólar CRYPTO', 'Ind Merval', 'Plazo Fijo']
#option = st.radio("Seleccione una opción : ", (list_option), horizontal=True )

st.subheader(f"Gráficos de dispersión de : {option} ")
st.write("datos expresados en %, para medir la variación del valor en un periodo mensual(se aplica log natural)")
st.write("y para medir la volatilidad se aplica la desv. standar sobre la muestra de datos (periodo mensual)")

with st.container():
    st.subheader("Gráfico de Rendimiento/Volatilidad(mensual) con streamlit")
    # ---- DOLAR BLUE ----
    if option == 'Dólar Blue':
        grafico = alt.Chart(df3).mark_circle().encode(
            x="blue_vol",
            y="blue_rend",
            size="blue_rend",
            color=alt.value('yellow')
            )
        st.altair_chart(grafico, use_container_width=True)

        st.subheader("Gráfico de Histograma de Rendimiento (mensual)")
        grafico2=alt.Chart(df3).mark_bar(color="green").encode(
            alt.X("blue_rend", bin=True),
            y='count()',
        )
        st.altair_chart(grafico2, use_container_width=True)

        st.subheader("Gráfico de ajuste polinómico con transformación de regresión (mensual)")
        x = df3["blue_vol"]
        y = df3["blue_rend"]
        source = pd.DataFrame({"x": x, "y": y})
        # Define the degree of the polynomial fits
        degree_list = [1, 3, 5]

        base = alt.Chart(source).mark_circle(color="yellow").encode(
            alt.X("x"),
            alt.Y("y")
        )

        grafico3 = [
            base.transform_regression(
                "x", "y", method="poly", order=order, as_=["x", str(order)]
            )
            .mark_line()
            .transform_fold([str(order)], as_=["degree", "y"])
            .encode(alt.Color("degree:N"))
            for order in degree_list
        ]
        alt.layer(base, *grafico3)
        st.altair_chart(alt.layer(base, *grafico3),use_container_width=True)

      # ---- DOLAR CCL ----
    elif option == 'Dólar CCL':
        grafico = alt.Chart(df3).mark_circle().encode(
            x="ccl_vol",
            y="ccl_rend",
            size="ccl_rend",
            color=alt.value('yellow')
            )
        st.altair_chart(grafico, use_container_width=True)

        st.subheader("Gráfico de Histograma de Rendimiento (mensual)")
        grafico2=alt.Chart(df3).mark_bar(color="green").encode(
            alt.X("ccl_rend", bin=True),
            y='count()',
        )
        st.altair_chart(grafico2, use_container_width=True)

        st.subheader("Gráfico de ajuste polinómico con transformación de regresión (mensual)")
        x = df3["ccl_vol"]
        y = df3["ccl_rend"]
        source = pd.DataFrame({"x": x, "y": y})
        # Define the degree of the polynomial fits
        degree_list = [1, 3, 5]

        base = alt.Chart(source).mark_circle(color="yellow").encode(
            alt.X("x"),
            alt.Y("y")
        )
        grafico3 = [
            base.transform_regression(
                "x", "y", method="poly", order=order, as_=["x", str(order)]
            )
            .mark_line()
            .transform_fold([str(order)], as_=["degree", "y"])
            .encode(alt.Color("degree:N"))
            for order in degree_list
        ]
        alt.layer(base, *grafico3)
        st.altair_chart(alt.layer(base, *grafico3),use_container_width=True)

      # ---- DOLAR MEP ----
    elif option == 'Dólar MEP':
        grafico = alt.Chart(df3).mark_circle().encode(
            x="mep_vol",
            y="mep_rend",
            size="mep_rend",
            color=alt.value('yellow')
            )
        st.altair_chart(grafico, use_container_width=True)

        st.subheader("Gráfico de Histograma de Rendimiento (mensual)")
        grafico2=alt.Chart(df3).mark_bar(color="green").encode(
            alt.X("mep_rend", bin=True),
            y='count()',
        )
        st.altair_chart(grafico2, use_container_width=True)

        st.subheader("Gráfico de ajuste polinómico con transformación de regresión (mensual)")
        x = df3["mep_vol"]
        y = df3["mep_rend"]
        source = pd.DataFrame({"x": x, "y": y})
        # Define the degree of the polynomial fits
        degree_list = [1, 3, 5]

        base = alt.Chart(source).mark_circle(color="yellow").encode(
            alt.X("x"),
            alt.Y("y")
        )

        grafico3 = [
            base.transform_regression(
                "x", "y", method="poly", order=order, as_=["x", str(order)]
            )
            .mark_line()
            .transform_fold([str(order)], as_=["degree", "y"])
            .encode(alt.Color("degree:N"))
            for order in degree_list
        ]
        alt.layer(base, *grafico3)
        st.altair_chart(alt.layer(base, *grafico3),use_container_width=True)
    # ---- DOLAR CRYPTO ----
    elif option == 'Dólar CRYPTO':
        grafico = alt.Chart(df3).mark_circle().encode(
            x="crypto_vol",
            y="crypto_rend",
            size="crypto_rend",
            color=alt.value('yellow')
            )
        st.altair_chart(grafico, use_container_width=True)

        st.subheader("Gráfico de Histograma de Rendimiento (mensual)")
        grafico2=alt.Chart(df3).mark_bar(color="green").encode(
            alt.X("crypto_rend", bin=True),
            y='count()',
        )
        st.altair_chart(grafico2, use_container_width=True)

        st.subheader("Gráfico de ajuste polinómico con transformación de regresión (mensual)")
        x = df3["crypto_vol"]
        y = df3["crypto_rend"]
        source = pd.DataFrame({"x": x, "y": y})
        # Define the degree of the polynomial fits
        degree_list = [1, 3, 5]

        base = alt.Chart(source).mark_circle(color="yellow").encode(
            alt.X("x"),
            alt.Y("y")
        )

        grafico3 = [
            base.transform_regression(
                "x", "y", method="poly", order=order, as_=["x", str(order)]
            )
            .mark_line()
            .transform_fold([str(order)], as_=["degree", "y"])
            .encode(alt.Color("degree:N"))
            for order in degree_list
        ]
        alt.layer(base, *grafico3)
        st.altair_chart(alt.layer(base, *grafico3),use_container_width=True)
    # ---- MERVAL ----
    elif option == 'Ind Merval':
        grafico = alt.Chart(df3).mark_circle().encode(
            x="merval_vol",
            y="merval_rend",
            size="merval_rend",
            color=alt.value('yellow')
            )
        st.altair_chart(grafico, use_container_width=True)

        st.subheader("Gráfico de Histograma de Rendimiento (mensual)")
        grafico2=alt.Chart(df3).mark_bar(color="green").encode(
            alt.X("merval_rend", bin=True),
            y='count()',
        )
        st.altair_chart(grafico2, use_container_width=True)

        st.subheader("Gráfico de ajuste polinómico con transformación de regresión (mensual)")
        x = df3["merval_vol"]
        y = df3["merval_rend"]
        source = pd.DataFrame({"x": x, "y": y})
        # Define the degree of the polynomial fits
        degree_list = [1, 3, 5]

        base = alt.Chart(source).mark_circle(color="yellow").encode(
            alt.X("x"),
            alt.Y("y")
        )

        grafico3 = [
            base.transform_regression(
                "x", "y", method="poly", order=order, as_=["x", str(order)]
            )
            .mark_line()
            .transform_fold([str(order)], as_=["degree", "y"])
            .encode(alt.Color("degree:N"))
            for order in degree_list
        ]
        alt.layer(base, *grafico3)
        st.altair_chart(alt.layer(base, *grafico3),use_container_width=True)
    # ---- PLAZO FIJO ----
    elif option == 'Plazo Fijo':
        grafico = alt.Chart(df3).mark_circle().encode(
            x="pfijo_vol",
            y="pfijo_rend",
            size="pfijo_rend",
            color=alt.value('yellow')
            )
        st.altair_chart(grafico, use_container_width=True)

        st.subheader("Gráfico de Histograma de Rendimiento (mensual)")
        grafico2=alt.Chart(df3).mark_bar(color="green").encode(
            alt.X("pfijo_rend", bin=True),
            y='count()',
        )
        st.altair_chart(grafico2, use_container_width=True)

        st.subheader("Gráfico de ajuste polinómico con transformación de regresión (mensual)")
        x = df3["pfijo_vol"]
        y = df3["pfijo_rend"]
        source = pd.DataFrame({"x": x, "y": y})
        # Define the degree of the polynomial fits
        degree_list = [1, 3, 5]

        base = alt.Chart(source).mark_circle(color="yellow").encode(
            alt.X("x"),
            alt.Y("y")
        )

        grafico3 = [
            base.transform_regression(
                "x", "y", method="poly", order=order, as_=["x", str(order)]
            )
            .mark_line()
            .transform_fold([str(order)], as_=["degree", "y"])
            .encode(alt.Color("degree:N"))
            for order in degree_list
        ]
        alt.layer(base, *grafico3)
        st.altair_chart(alt.layer(base, *grafico3),use_container_width=True)
    else:
       st.write("Error, verifique la opción seleccinada")

with st.container():
    st.subheader(" Gráfico de Rendimiento/Volatilidad(mensual) con plotly")
    # ---- DOLAR BLUE ----
    if option == 'Dólar Blue':
        fig = px.scatter(
                df3,
                x="blue_vol",
                y="blue_rend",
                color="blue_rend",
                trendline='ols', trendline_color_override='darkblue',
                color_continuous_scale="reds"
            )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

        fig1 = px.scatter(df3, x = "blue_vol", y = "blue_rend",
                    marginal_x = "histogram", marginal_y = "histogram",
                    trendline='ols', trendline_options=dict(log_x=True),
                    trendline_color_override='darkblue',
                    )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.write('se grafica el log a la regresion')
                st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig1, theme=None, use_container_width=True)

    # ---- DOLAR CCL ----
    elif option == 'Dólar CCL':
        fig = px.scatter(
                df3,
                x="ccl_vol",
                y="ccl_rend",
                color="ccl_rend",
                trendline='ols', trendline_color_override='darkblue',
                color_continuous_scale="reds"
            )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

        fig1 = px.scatter(df3, x = "ccl_vol", y = "ccl_rend",
                    marginal_x = "histogram", marginal_y = "histogram",
                    trendline='ols', trendline_options=dict(log_x=True),
                    trendline_color_override='darkblue',
                    )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.write('se grafica el log a la regresion')
                st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig1, theme=None, use_container_width=True)
    # ---- DOLAR MEP ----
    elif option == 'Dólar MEP':
        fig = px.scatter(
                df3,
                x="mep_vol",
                y="mep_rend",
                color="mep_rend",
                trendline='ols', trendline_color_override='darkblue',
                color_continuous_scale="reds"
            )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

        fig1 = px.scatter(df3, x = "mep_vol", y = "mep_rend",
                    marginal_x = "histogram", marginal_y = "histogram",
                    trendline='ols', trendline_options=dict(log_x=True),
                    trendline_color_override='darkblue',
                    )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.write('se grafica el log a la regresion')
                st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig1, theme=None, use_container_width=True)

    # ---- DOLAR CRYPTO ----
    elif option == 'Dólar CRYPTO':
        fig = px.scatter(
                df3,
                x="crypto_vol",
                y="crypto_rend",
                color="crypto_rend",
                trendline='ols', trendline_color_override='darkblue',
                color_continuous_scale="reds"
            )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

        fig1 = px.scatter(df3, x = "crypto_vol", y = "crypto_rend",
                    marginal_x = "histogram", marginal_y = "histogram",
                    trendline='ols', trendline_options=dict(log_x=True),
                    trendline_color_override='darkblue',
                    )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.write('se grafica el log a la regresion')
                st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig1, theme=None, use_container_width=True)

    # ---- MERVAL ----
    elif option == 'Ind Merval':
        fig = px.scatter(
                df3,
                x="merval_vol",
                y="merval_rend",
                color="merval_rend",
                trendline='ols', trendline_color_override='darkblue',
                color_continuous_scale="reds"
            )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

        fig1 = px.scatter(df3, x = "merval_vol", y = "merval_rend",
                    marginal_x = "histogram", marginal_y = "histogram",
                    trendline='ols', trendline_options=dict(log_x=True),
                    trendline_color_override='darkblue',
                    )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.write('se grafica el log a la regresion')
                st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig1, theme=None, use_container_width=True)

    # ---- PLAZO FIJO ----
    elif option == 'Plazo Fijo':
        fig = px.scatter(
                df3,
                x="pfijo_vol",
                y="pfijo_rend",
                color="pfijo_rend",
                trendline='ols', trendline_color_override='darkblue',
                color_continuous_scale="reds"
            )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

        fig1 = px.scatter(df3, x = "pfijo_vol", y = "pfijo_rend",
                    marginal_x = "histogram", marginal_y = "histogram",
                    trendline='ols',
                    trendline_color_override='darkblue',
                    )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.write('se grafica  la regresion')
                st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig1, theme=None, use_container_width=True)

    else:
        st.write("Error, verifique la opción seleccinada")

# ---- Descripcion de la quinta pagina de prediccion de rendimientos y animación mensual ----

df4 = pd.read_excel('assets/dolar_blue3.xlsx')

#list_option = ['Dólar Blue', 'Dólar CCL', 'Dólar MEP', 'Dólar CRYPTO', 'Ind Merval', 'Plazo Fijo']
#option = st.radio("Seleccione una opción : ", (list_option), horizontal=True )

st.subheader(f"Gráficos de dispersión animado de : {option} ")
st.write("datos expresados en %, para medir la variación del valor en un periodo mensual(se aplica log natural)")
st.write("y para medir la volatilidad se aplica la desv. standar sobre la muestra de datos (periodo mensual)")

with st.container():
     # ---- DOLAR BLUE ----
    if option == 'Dólar Blue':
        df5 = pd.DataFrame(df4)
        grafico = px.scatter(df5,
                                x=df5['blue_vol'],
                                y=df5['blue_rend'],
                                animation_frame= "meses",
                                animation_group="blue_rend",
                                size="blue_vol",
                                color='blue_rend',
                                hover_name='blue_rend',
                                size_max=45, range_x=[-5,40], range_y=[-20,50]

                              )
        st.plotly_chart(grafico, use_container_width=True)
    # ---- DOLAR CCL ----
    elif option == 'Dólar CCL':
        df5 = pd.DataFrame(df4)
        grafico = px.scatter(df5,
                                x=df5['ccl_vol'],
                                y=df5['ccl_rend'],
                                animation_frame= "meses",
                                animation_group="ccl_rend",
                                size="ccl_vol",
                                color='ccl_rend',
                                hover_name='ccl_rend',
                                size_max=45, range_x=[-5,40], range_y=[-20,50]

                              )
        st.plotly_chart(grafico, use_container_width=True)

    # ---- DOLAR MEP ----
    elif option == 'Dólar MEP':
        df5 = pd.DataFrame(df4)
        grafico = px.scatter(df5,
                                x=df5['mep_vol'],
                                y=df5['mep_rend'],
                                animation_frame= "meses",
                                animation_group="mep_rend",
                                size="mep_vol",
                                color='mep_rend',
                                hover_name='mep_rend',
                                size_max=45, range_x=[-5,40], range_y=[-20,50]

                              )
        st.plotly_chart(grafico, use_container_width=True)

    # ---- DOLAR CRYPTO ----
    elif option == 'Dólar CRYPTO':
        df5 = pd.DataFrame(df4)
        grafico = px.scatter(df5,
                                x=df5['crypto_vol'],
                                y=df5['crypto_rend'],
                                animation_frame= "meses",
                                animation_group="crypto_rend",
                                size="crypto_vol",
                                color='crypto_rend',
                                hover_name='crypto_rend',
                                size_max=45, range_x=[-5,40], range_y=[-20,50]

                              )
        st.plotly_chart(grafico, use_container_width=True)

    # ---- DOLAR MERVAL ----
    elif option == 'Ind Merval':
        df5 = pd.DataFrame(df4)
        grafico = px.scatter(df5,
                                x=df5['merval_vol'],
                                y=df5['merval_rend'],
                                animation_frame= "meses",
                                animation_group="merval_rend",
                                size="merval_vol",
                                color='merval_rend',
                                hover_name='merval_rend',
                                size_max=45, range_x=[-5,40], range_y=[-20,50]

                              )
        st.plotly_chart(grafico, use_container_width=True)

    # ---- DOLAR PLAZO FIJO ----
    elif option == 'Plazo Fijo':
        df5 = pd.DataFrame(df4)
        grafico = px.scatter(df5,
                                x=df5['pfijo_vol'],
                                y=df5['pfijo_rend'],
                                animation_frame= "meses",
                                animation_group="pfijo_rend",
                                size="pfijo_vol",
                                color='pfijo_rend',
                                hover_name='pfijo_rend',
                                size_max=45, range_x=[-5,40], range_y=[-20,50]

                              )
        st.plotly_chart(grafico, use_container_width=True)
    else:
        st.write('Error, opcion no valida....!!!')


models = {'Regresión': linear_model.LinearRegression,
          'Arbol de Decisión': tree.DecisionTreeRegressor,
          'K-NN': neighbors.KNeighborsRegressor}

st.subheader(f"Gráficos de Predicción rendimientos de : {option} ")
option_list = ['Arbol de Decisión', 'Regresión', 'K-NN']
options = st.radio("Seleccione una opción : ", (option_list), horizontal=True )
st.subheader(f"Modelo desplegado de regresión  : {options} ")
st.write('x = % volatilidad, y = % rendimiento, linea = predicción  ')
with st.container():
    # ---- DOLAR BLUE ----
    if option == 'Dólar Blue':
        X = df4['blue_vol'].values[:, None]
        X_train, X_test, y_train, y_test = train_test_split(
            X, df4['blue_rend'], random_state=42)

        model = models[options]()
        model.fit(X_train, y_train)

        x_range = np.linspace(X.min(), X.max(), 800)
        y_range = model.predict(x_range.reshape(-1, 1))

        grafico1 = go.Figure([
            go.Scatter(x=X_train.squeeze(),
                       y=y_train,
                       name='train',
                       mode='markers'),
            go.Scatter(x=X_test.squeeze(),
                       y=y_test,
                       name='test',
                       mode='markers'),
            go.Scatter(x=x_range,
                       y=y_range,
                       name='prediction'),

        ])
        st.plotly_chart(grafico1,use_container_width=True)
    # ---- DOLAR CCL ----
    elif option == 'Dólar CCL':
        X = df4['ccl_vol'].values[:, None]
        X_train, X_test, y_train, y_test = train_test_split(
            X, df4['ccl_rend'], random_state=42)

        model = models[options]()
        model.fit(X_train, y_train)

        x_range = np.linspace(X.min(), X.max(), 800)
        y_range = model.predict(x_range.reshape(-1, 1))

        grafico1 = go.Figure([
            go.Scatter(x=X_train.squeeze(),
                       y=y_train,
                       name='train',
                       mode='markers'),
            go.Scatter(x=X_test.squeeze(),
                       y=y_test,
                       name='test',
                       mode='markers'),
            go.Scatter(x=x_range,
                       y=y_range,
                       name='prediction'),

        ])
        st.plotly_chart(grafico1,use_container_width=True)

    # ---- DOLAR MEP ----
    elif option == 'Dólar MEP':
        X = df4['mep_vol'].values[:, None]
        X_train, X_test, y_train, y_test = train_test_split(
            X, df4['mep_rend'], random_state=42)

        model = models[options]()
        model.fit(X_train, y_train)

        x_range = np.linspace(X.min(), X.max(), 800)
        y_range = model.predict(x_range.reshape(-1, 1))

        grafico1 = go.Figure([
            go.Scatter(x=X_train.squeeze(),
                       y=y_train,
                       name='train',
                       mode='markers'),
            go.Scatter(x=X_test.squeeze(),
                       y=y_test,
                       name='test',
                       mode='markers'),
            go.Scatter(x=x_range,
                       y=y_range,
                       name='prediction'),

        ])
        st.plotly_chart(grafico1,use_container_width=True)

    # ---- DOLAR CRYPTO ----
    elif option == 'Dólar CRYPTO':
        X = df4['crypto_vol'].values[:, None]
        X_train, X_test, y_train, y_test = train_test_split(
            X, df4['crypto_rend'], random_state=42)

        model = models[options]()
        model.fit(X_train, y_train)

        x_range = np.linspace(X.min(), X.max(), 800)
        y_range = model.predict(x_range.reshape(-1, 1))

        grafico1 = go.Figure([
            go.Scatter(x=X_train.squeeze(),
                       y=y_train,
                       name='train',
                       mode='markers'),
            go.Scatter(x=X_test.squeeze(),
                       y=y_test,
                       name='test',
                       mode='markers'),
            go.Scatter(x=x_range,
                       y=y_range,
                       name='prediction'),

        ])
        st.plotly_chart(grafico1,use_container_width=True)

    # ---- DOLAR MERVAL ----
    elif option == 'Ind Merval':
        X = df4['merval_vol'].values[:, None]
        X_train, X_test, y_train, y_test = train_test_split(
            X, df4['merval_rend'], random_state=42)

        model = models[options]()
        model.fit(X_train, y_train)

        x_range = np.linspace(X.min(), X.max(), 800)
        y_range = model.predict(x_range.reshape(-1, 1))

        grafico1 = go.Figure([
            go.Scatter(x=X_train.squeeze(),
                       y=y_train,
                       name='train',
                       mode='markers'),
            go.Scatter(x=X_test.squeeze(),
                       y=y_test,
                       name='test',
                       mode='markers'),
            go.Scatter(x=x_range,
                       y=y_range,
                       name='prediction'),

        ])
        st.plotly_chart(grafico1,use_container_width=True)

    # ---- DOLAR PFIJO ----
    elif option == 'Plazo Fijo':
        X = df4['pfijo_vol'].values[:, None]
        X_train, X_test, y_train, y_test = train_test_split(
            X, df4['pfijo_rend'], random_state=42)

        model = models[options]()
        model.fit(X_train, y_train)

        x_range = np.linspace(X.min(), X.max(), 800)
        y_range = model.predict(x_range.reshape(-1, 1))

        grafico1 = go.Figure([
            go.Scatter(x=X_train.squeeze(),
                       y=y_train,
                       name='train',
                       mode='markers'),
            go.Scatter(x=X_test.squeeze(),
                       y=y_test,
                       name='test',
                       mode='markers'),
            go.Scatter(x=x_range,
                       y=y_range,
                       name='prediction'),

        ])
        st.plotly_chart(grafico1,use_container_width=True)

    else:
        st.write('Error, no es una opción valida')



# ---- CONTACT ----
with st.container():
    st.write("---")
    st.write("&copy; - derechos reservados -  2023 -  Walter Gómez - FullStack Developer")
    st.write("##")


