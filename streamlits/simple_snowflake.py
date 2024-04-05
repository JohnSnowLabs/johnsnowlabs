import streamlit as st
from snowflake.snowpark.context import get_active_session
session = get_active_session()
data = st.text_area("Type Your Text", value='Sample text', height=200)
udf_response = session.sql(f"""SELECT JSL_DEIDENTIFY_CLINICAL('{data}')""",)
st.write(udf_response.collect()[0].as_dict())