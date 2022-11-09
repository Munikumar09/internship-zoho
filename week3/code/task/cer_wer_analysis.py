import pandas as pd
import streamlit as st
import plotly.graph_objects as go


def get_files_dict(files):
    file_list = {}
    for file in files:
        name = "_".join((file.name.split("_"))[0:2])
        file_list[name] = file
    return file_list


if "data" not in st.session_state:
    st.session_state["data"] = []

rad = st.sidebar.radio("Navigation", ["Home", "upload files", "compare data"])
if rad == "Home":
    st.write(
        """
             This is small application to compare and visualize the data
             """
    )
if rad == "upload files":
    text = "please select the files from your system"
    uploads = st.sidebar.file_uploader(
        "upload data set files in jsonl format",
        accept_multiple_files=True,
        type=[".jsonl"],
    )
    if len(uploads) > 0:
        text = "files are successfully uploaded you can move to next section to compare the data"
    for file in uploads:
        st.session_state["data"].append(file)
    st.write(text)

if rad == "compare data":
    files_list = get_files_dict(st.session_state["data"])
    if len(files_list) > 0:

        options = st.sidebar.multiselect(
            "please select 2 models for comparison",
            list(files_list.keys()),
        )
        if len(options) == 2:
            df1 = pd.read_json(files_list[options[0]], lines=True)
            df2 = pd.read_json(files_list[options[1]], lines=True)
            df1_cols = list(df1)
            df2_cols = list(df2)
            dataframe_long = pd.DataFrame(
                {
                    df1_cols[0]: df1[df1_cols[0]],
                    options[0] + "_cer": df1[df1_cols[1]] * 100,
                    options[1] + "_cer": df2[df2_cols[1]] * 100,
                    options[0] + "_wer": df1[df1_cols[2]] * 100,
                    options[1] + "_wer": df2[df2_cols[2]] * 100,
                    "per_change_cer": (1 - df2[df1_cols[1]] / df1[df1_cols[1]]) * 100,
                    "per_change_wer": (1 - df2[df1_cols[2]] / df1[df1_cols[2]]) * 100,
                }
            )

            def color_survived(val):
                color = "green" if val > 0 else "red"
                return f"background-color: {color}"
            st.markdown("""
                        ### comparison of two models based on their cer and wer score""")
            st.dataframe(
                dataframe_long.style.applymap(
                    color_survived, subset=["per_change_wer", "per_change_cer"]
                )
            )
            st.text("Lower the value better the accuracy of the model")
            st.markdown("""
                        ### Character Error Count (CER) Distribution
                        """)
            bar_chart_cer = go.Figure()
            bar_chart_cer.add_trace(
                go.Bar(
                    x=dataframe_long["dataset"],
                    y=dataframe_long[options[0] + "_cer"],
                    name=options[0],
                    marker_color="yellow",
                )
            )
            bar_chart_cer.add_trace(
                go.Bar(
                    x=dataframe_long["dataset"],
                    y=dataframe_long[options[1] + "_cer"],
                    name=options[1],
                    marker_color="brown",
                )
            )
            bar_chart_cer.update_traces(texttemplate='%{text:.2s}', textposition='outside')
            bar_chart_cer.update_layout(
                yaxis=dict(
                title='CER Accuracy',
                titlefont_size=16,
                tickfont_size=14,
    ),
                xaxis=dict(
                title='Various Test',
                titlefont_size=16,
                tickfont_size=14,
    ),
                barmode="group",uniformtext_minsize=8,uniformtext_mode='hide')
            st.plotly_chart(bar_chart_cer)
            st.markdown("""
                        ### Word Error Count (WER) Distribution
                        """)
            bar_chart_wer = go.Figure()
            bar_chart_wer.add_trace(
                go.Bar(
                    x=dataframe_long["dataset"],
                    y=dataframe_long[options[0] + "_wer"],
                    name=options[0],
                    marker_color="yellow",
                )
            )
            bar_chart_wer.add_trace(
                go.Bar(
                    x=dataframe_long["dataset"],
                    y=dataframe_long[options[1] + "_wer"],
                    name=options[1],
                    marker_color="brown",
                )
            )
            bar_chart_wer.update_layout(
                yaxis=dict(
                title='WER Accuracy',
                titlefont_size=16,
                tickfont_size=14,
    ),
                xaxis=dict(
                title='Various Test',
                titlefont_size=16,
                tickfont_size=14,
    ),
                barmode="group")
            st.plotly_chart(bar_chart_wer)

        else:
            st.write("please select only two models for comparison")
    else:
        st.write("Please select two models for comparison")
