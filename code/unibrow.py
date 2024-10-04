'''
Solution unibrow.py
'''
import streamlit as st
import pandas as pd
import pandaslib as pl

# File uploader
file_upload = st.file_uploader("Upload a file", type=['csv', 'xlsx', 'json'])

if file_upload:
    ext = pl.get_file_extension(file_upload.name)
    df = pl.load_file(file_upload, ext)
    col_names = pl.get_column_names(df)
    
    # Column multi-select, start with all columns selected
    cols_select = st.multiselect("Select Columns", df.columns, default=df.columns)
    
    # Toggle to include a filter
    include_filter = st.checkbox("Include Filter")
    
    if include_filter:
        # Dropdown for object column names
        obj_columns = [col for col in df.columns if df[col].dtype == 'object']
        filter_col = st.selectbox("Select Column for Filter", obj_columns)
        
        # Dropdown for unique values in the selected column
        if filter_col:
            unique_values = pl.get_unique_values(df, filter_col)
            filter_value = st.selectbox("Select Value for Filter", unique_values)
            
            # Filter the dataframe
            df_filtered = df[df[filter_col] == filter_value]
        else:
            df_filtered = df
    else:
        df_filtered = df
    
    # Display the filtered dataframe
    if cols_select:
        st.write(df_filtered[cols_select])
    
    # Describe the filtered dataframe
    st.write(df_filtered[cols_select].describe())



