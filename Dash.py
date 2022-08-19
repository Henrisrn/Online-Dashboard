import pandas as pd
import hvplot.pandas
import hvplot as hv
import panel as pn
import plotly.express as px
import streamlit as st
import openpyxl
pn.extension('tabulator',sizing_mode="stretch_width")
hv.extension("bokeh")

st.set_page_config(page_title="Test",
                   page_icon=":bar_chart:",
                   layout="wide")

Palette = ["#F067A5","#4FD8F0","#F0E47F"]

#pn.Row(
#    pn.layout.HSpacer(height=50,background=Palette[0]),
#    pn.layout.HSpacer(height=50,background=Palette[1])
#    pn.layout.HSpacer(height=50,background=Palette[2])
#)

# ---- READ EXCEL ----
@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="Flightschedule.xlsx",
        #engine="openpyxl",
        sheet_name="Sheet1",
        usecols="B:R",
        nrows=1000,
    )
    return df

df = get_data_from_excel()

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
city = st.sidebar.multiselect(
    "Select the Passarrival:",
    options=df["Passarrival"].dropna().unique(),
    default=df["Passarrival"].dropna().unique()
)

compagnie = st.sidebar.multiselect(
    "Select the Company:",
    options=df["Company"].dropna().unique(),
    default=df["Company"].dropna().unique()
)

customer_type = st.sidebar.multiselect(
    "Select the Passdepat:",
    options=df["Passdepat"].dropna().unique(),
    default=df["Passdepat"].dropna().unique(),
)

gender = st.sidebar.multiselect(
    "Select the depart:",
    options=df["depart"].dropna().unique(),
    default=df["depart"].dropna().unique()
)

df_selection = df.query(
    "Passarrival == @city & Passdepat ==@customer_type & depart == @gender & Company==@compagnie"
)
print(df_selection)
# ---- MAINPAGE ----
st.title(":bar_chart: Flight Dashboard")
st.markdown("##")

st.dataframe(df_selection)

oo = df_selection["Passdepat"].dropna()
compteurterm = oo.value_counts()
nomterm = oo.drop_duplicates()

fig_product_sales = px.bar(
    x=compteurterm,
    y=nomterm,
    orientation="h",
    title="<b>Sales by Product Line</b>",
    color_discrete_sequence=["#0083B8"] * len(nomterm),
    template="plotly_white",
)

fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

bb = list(df_selection['Company'].value_counts())
print(bb)
aa = list(df_selection['Company'].value_counts().index)
print(aa)

fig = px.pie(values=bb, names=aa)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig, use_container_width=True)
right_column.plotly_chart(fig_product_sales, use_container_width=True)
st.slider("Test slider")
print(openpyxl.__version__)
#REGARDER POUR D'AUTRE GRAPH AVEC PX EN FONCTION DES DEMANDES
#POSSIBLE D'ADAPTER AVEC D'AUTRE DATA BASE ETC...