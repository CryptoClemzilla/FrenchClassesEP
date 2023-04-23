import streamlit as st
import pandas as pd
#from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
import webbrowser

# config
st.set_page_config(page_title="French course A2",
                   page_icon=":books:",
                   layout="wide",
                   initial_sidebar_state="expanded")

# Add custom CSS FONT
st.write("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Lexend:wght@200&display=swap');
html, body, [class*="css"]  {
   font-family: 'Lexend', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# READ CSV
df = pd.read_csv("french_classes.csv")

# Set page title and subtitle
st.title(":frog: French Classes A2")
st.write('Go to the link below to access the Grammar textbooks, the Film and Series repository,'
         'the Comics and the French songs playlists')

# URL Drive button
#url = st.button('Drive')
#if url:
    #webbrowser.open('https://drive.google.com/drive/folders/1fn7NcuYZqm_2P4vdSfUAI8mXzl1_-a7C?usp=share_link')
# st.markdown("[Drive of the class](https://drive.google.com/drive/folders/1fn7NcuYZqm_2P4vdSfUAI8mXzl1_-a7C?usp=share_link)")

# Add les consignes
st.write("Use this dashboard to self-orientate within these French classes. You can select the level of difficulty "
            "you desire, the skills you want to practice, as well as the topics you want to approach. "
            "When selecting an activity, please read carefully the column 'Assignment' which tells you how to proceed, "
            "and go to the link in the columns Link1 and Link2. Sometimes, the activity is standalone and does not have "
            "a link: it's the case for challenges or games, for instance. ")
st.markdown('')

# Sidebar
st.sidebar.title('Filter your lesson!')

# Define sidebar options
st.sidebar.subheader('Parameters')
difficulty = st.sidebar.selectbox("Select a level of difficulty", ["Select All"] + list(df["Difficulty"].unique()))
format = st.sidebar.selectbox("Select your preferred format", ["Select All"] + list(df["Format"].unique()))
skills_options = ["Select All", "Speaking", "Reading", "Listening", "Writing", "Writing, reading", "Speaking, writing",
                  "Speaking, reading", "Listening, writing", "Speaking, listening", "Writing, listening",
                  "Reading, listening"]
skills = st.sidebar.selectbox("Select the skills to improve", skills_options)
topic = st.sidebar.selectbox("Select the class category", ["Select All"] + list(df["Label"].unique()))


# Define filter function
def filter_dataframe(df, difficulty, skills, topic, format):
    if topic != "Select All":
        df = df[df["Label"] == topic]
    if difficulty != "Select All":
        df = df[df["Difficulty"] == difficulty]
    if skills and skills != "Select All":
        df = df[df["Skills_involved"] == skills]
    if format != "Select All":
        df = df[df["Format"] == format]
    return df


# Filter the dataframe based on selected options
filtered_df = filter_dataframe(df, difficulty, skills, topic, format)

# Filter the dataframe based on selected options
filtered_df = filter_dataframe(df, difficulty, skills, topic, format)

# Add a search bar for the "Label" column
st.sidebar.subheader('Search by keywords')
search_term = st.sidebar.text_input("Search", key='search')
if search_term:
    filtered_df = filtered_df[filtered_df["Label"].str.contains(search_term, case=False)]

# Display the filtered dataframe in a table format
# Define ag-grid options
#gb = GridOptionsBuilder.from_dataframe(filtered_df)
#gb.configure_pagination()
#gb.configure_side_bar()
#gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
#gridOptions = gb.build()

# Display the filtered dataframe using ag-grid
#AgGrid(filtered_df, gridOptions=gridOptions, width='90%', height='800px',
       #update_mode=GridUpdateMode.SELECTION_CHANGED,
       #allow_unsafe_jscode=True, enable_enterprise_modules=True)

#footer = st.text_input("", "© 2023 - CM")

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
padding: 8px;
width: 100%;
background-color: #99ccff;
color: black;
text-align: right;
}

</style>
<div class="footer">
<p>Developed with ❤ <br> <a style='display: block; text-align: right;' href="https://www.heflin.dev/" target="_blank"> Give feedback :)</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)