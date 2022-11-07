import pandas as pd
import streamlit as st
import json

col1, col2 = st.columns(2)
with col1:
    with open("sample.json", "r") as f:
        data = json.load(f)
    df = pd.read_json("sample.json")
    st.json(data)
    st.dataframe(df)
    st.graphviz_chart(
        """
    digraph{
    new -> runnable
    runnable ->running
    running ->runnable
    blocked -> runnable
    running ->blocked
    running -> terminated
    blocked -> terminated
    }
    """,
        True,
    )
with col2:
    st.table(df)
    button_result = st.button("click me")
    st.write(button_result)
    if button_result:
        st.write(":smile:")
    with open("sample.json", "r") as f:
        st.download_button(
            label="download json file",
            data=f,
            file_name="employee_details.json",
            mime="text/json",
        )
