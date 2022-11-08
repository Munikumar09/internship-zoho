import pandas as pd
import streamlit as st
import altair as alt
path_to_data={"conformer beam":"/app/internship-zoho/week3/code/task/data/conformer_beam_overall_summary.jsonl",
              "conformer greedy":"/app/internship-zoho/week3/code/task/data/conformer_greedy_overall_summary.jsonl",
              "w2l beam":"data/w2l_beam_overall_summary.jsonl",
              "w2l greedy":"data/w2l_greedy_overall_summary.jsonl"}
def display_dataframes(options:list):
    df_1=pd.read_json(path_to_data[options[0]],lines=True)
    df_2=pd.read_json(path_to_data[options[1]],lines=True)
    df_1_new=pd.DataFrame(
        {
         "dataset":df_1['dataset'],
         options[0]:df_1['cer'],
         options[1]:df_2['cer'],
            })
    df_2_new=pd.DataFrame(
        {
            "dataset":df_2['dataset'],
            options[0]:df_1['wer'],
            options[1]:df_2['wer']
        }
    )
    df_1_new=df_1_new.set_index('dataset')
    df_2_new=df_2_new.set_index('dataset')
    col1,col2=st.columns(2)
    col1.dataframe(df_1)
    col2.dataframe(df_2)
    st.markdown(f"""
                ### Comparing <p class="a">{options[0]} and {options[1]} on the basis of character error rate(cer)</p>
                """,unsafe_allow_html=True)
    st.bar_chart(df_1_new)
    st.markdown(f"""
                ### Comparing <p class="a">{options[0]} and {options[1]} on the basis of word error rate(wer)</p>
                """,unsafe_allow_html=True)
    st.bar_chart(df_2_new)
    st.markdown("""
                **Note:** lower the value is better
                """)
options = st.multiselect(
    'Select two models from the below options',
    path_to_data.keys()
    )
if len(options)==2:
    display_dataframes(options)
elif len(options)!=2 and len(options)>0: 
    st.text("Please select two models from the below options to compare them")
