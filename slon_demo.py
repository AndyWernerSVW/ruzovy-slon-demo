import streamlit as st
import pandas as pd
import numpy as np
import show_filters as sf
import support_table as stt
import random

# Sample data
def logic_options():
    return ["Follow Min", "Follow Min + 5%", "Follow Median", "Follow Alza - 1%"]

def create_data(logic_options):
    import pandas as pd

    column_config = {}

    # Define the lists and range for generating the dataframe
    adjectives = ["Sensual", "Alluring", "Provocative", "Seductive", "Flirtatious", "Intimate", "Tempting", "Sultry", "Risqué", "Passionate"]
    animals = ["Kitten", "Puppy", "Hamster", "Chinchilla", "Bunny", "Hedgehog", "Ferret", "Guinea Pig", "Sugar Glider", "Pomeranian"]
    product_names = []
    # Create product names
    for _ in range(50):
        product_names.append(f"{random.choice(adjectives)} {random.choice(animals)}")
    column_config["Product Name"] = st.column_config.TextColumn(help = "Product Name as shown in Abra", disabled= True)

    # Set Country
    country = np.random.choice(["CZ","HU", "PL"], size=len(product_names))
    column_config["Country"] = st.column_config.TextColumn(help = "Country, where we are dealing", disabled= True)

    # Set Currency
    currency = np.random.choice(["CZK"], size=len(product_names))
    column_config["Currency"] = st.column_config.TextColumn(help = "Currency of price", disabled= True)

    # Set Aggregator link
    agg_link = np.random.choice(["heureka.cz/xxx"], size=len(product_names))
    column_config["Aggregator Link"] = st.column_config.LinkColumn(help = "From this link the prices are collected", disabled= True)
    
    # Generate current prices
    current_prices = np.random.randint(300, 1501, size=len(product_names))
    column_config["Current Price"] = st.column_config.NumberColumn(help = "Price as set today in Abra", disabled= True, format = "%.2f")
    
    # Generate proposed prices within 10% range of current prices
    proposed_prices = [np.random.uniform(price * 0.9, price * 1.1) for price in current_prices]
    column_config["Proposed Price"] = st.column_config.NumberColumn(help = "Price as calculated by select logic.", disabled= True, format = "%.2f")
    
    # Assign logic values randomly
    logic_values = np.random.choice(logic_options, size=len(product_names))
    column_config["Logic"] = st.column_config.SelectboxColumn(options = logic_options, help = "Select logic to use for pricing. Logics will be defined in advance. No other paramters are available",disabled= False)

    # Assign manual override values with 90% False
    manual_override_values = np.random.choice([False, True], size=len(product_names), p=[0.9, 0.1])
    column_config["Manual Override"] = st.column_config.CheckboxColumn(help = "False = product will be priced based on select logic. True = Manually set price will be used",disabled= False)

    manual_price = current_prices
    column_config["Manual Price"] = st.column_config.NumberColumn(help = "If Manual ovveride = true, then this price will be used", disabled= False, format = "%.2f")

    # Create the dataframe
    df = pd.DataFrame({
    "Product Name": product_names,
    "Country": country,
    "Currency": currency,
    "Aggregator Link": agg_link,
    "Current Price": current_prices,
    "Proposed Price": proposed_prices,
    "Logic": logic_values,
    "Manual Override": manual_override_values,
    "Manual Price": manual_price})
    
    return df,column_config

def create_non_editable_columns(df,editable_columns):
    columns_list = df.columns.tolist()
    non_editable_columns = [column for column in columns_list if column not in editable_columns]
    return non_editable_columns




# Streamlit app
def main():
    # Check if data is already in session state
    if 'data' not in st.session_state:
        st.session_state['data'],st.session_state["column_config"] = create_data(logic_options())

    st.title("Nastav strategii")
    
    ########### Show Filters ############
    sf.show_filters(st.session_state['data'])

    ########### Display the data ############
    st.subheader("Hlavní tabulka")
    st.caption("""Toto je hlavní tabulka. Zde uživatel vidí záklaní informace a nastavuje hlavní paramatry""")
    edited_df = st.data_editor(st.session_state['data'],width = 2000, use_container_width = False, column_config = st.session_state["column_config"])
   
    
    ########### Support Data ############

    stt.minor_table(st.session_state['data'])
    ########### Ovládací prvky ############
    st.subheader("Ovládací prvky")
    st.caption("Demonstrace toho, že uživatel odsud může kontrolovat Backend")
    col1, col2 = st.columns([1, 1])
    col1.button("Spusť scraper", type="primary")
    col2.button("Vynuť přepis dat", type="primary")
    
    


if __name__ == "__main__":
    main()

# filtering and editing Data: https://discuss.streamlit.io/t/filter-data-in-data-editor/52055/14