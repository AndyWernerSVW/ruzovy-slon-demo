import streamlit as st
import pandas as pd
import altair as alt

def minor_table(main_df):
    st.subheader("Podpůrná data")
    st.caption("""Zde je možné pro jednotlivé produkty vidět další detail""")
    st.selectbox("Vyber produkt", options = main_df["Název produktu"].unique())

    competitor_prices = pd.DataFrame({"Competitor": ["Elephant Rouge","Alzaxxx", "Mallý ale šikovný", "Erotic Village", "Hungarian Bazmek"],
                                          "Price": [1000,1090,2000,300,5000 ]})
    st.markdown("""**Ceny konkurence**""")

    # Bar chart using Altair
    chart = alt.Chart(competitor_prices).mark_bar().encode(
            x='Competitor',
            y='Price'
        )
    st.altair_chart(chart, use_container_width=True)

    ostatní_data = pd.DataFrame({"Metrika": ["Nákupní cena","Fallback cena", "Marže", "Dodavatel"],
                                 "Hodnota":[900, 910, "10%", "Strhující žážitky s.r.o.",]})
    st.markdown("""**Ostatní data**""")

    st.dataframe(ostatní_data)
    