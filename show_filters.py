import streamlit as st

def show_filters (df):
    with st.expander("Filters"):
        st.selectbox("vyber zemi", options = df["Country"].unique())
        st.multiselect("Vyber product", options = df["Product Name"].unique())
        st.slider("vyber současnou cenu", 0, 100,(25,75))
        st.caption("""Příklad filtrování. Po výberu filtru se aktualizuje tabulka níže.""")
