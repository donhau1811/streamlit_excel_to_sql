import streamlit as st
import pandas as pd
from io import StringIO
from postgres import postgres_engine
from sqlalchemy import create_engine
import xlrd 

# streamlit run app.py


def load_data_to_postgresql(df):
    engine = create_engine(postgres_engine())
    df.to_sql(
        "E01OrderType",
        engine,
        if_exists="append",
        index=False,
    )

uploaded_file = st.file_uploader(label="Choose a file", type='xlsx')
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    edited_df = st.data_editor(df, num_rows="dynamic")
    # st.dataframe(df)

    wdist1, wdist2, wdist3 = st.columns(3)

    with wdist2:
        if st.button('Upload to Database'):
            load_data_to_postgresql(df)
            st.write('Done')
