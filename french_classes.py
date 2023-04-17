import streamlit as st
import pandas as pd


df = pd.read_csv("french_classes.csv")

# Set page title and subtitle
st.set_page_config(page_title="French course A2", page_icon=":books:", layout="wide")
st.title("French course A2")
st.markdown('Go to the link below to access the Grammar textbooks, the Film and Series repository, the Comics and the French songs playlists.')
st.markdown("[Drive of the class](https://drive.google.com/drive/folders/1fn7NcuYZqm_2P4vdSfUAI8mXzl1_-a7C?usp=share_link)")
st.markdown('')
st.sidebar.title("Filters")

# Define sidebar options
difficulty = st.sidebar.selectbox("Select Difficulty", ["Low", "Medium", "High"])
skills_options = ["Select All", "Speaking", "Reading", "Listening", "Writing", "Writing, reading", "Speaking, writing", "Speaking, reading", "Listening, writing", "Speaking, listening", "Writing, listening", "Reading, listening"]
skills = st.sidebar.selectbox("Select Skills Involved", skills_options)
topic = st.sidebar.selectbox("Select Topic", ["All"] + list(df["Topic"].unique()))


# Define filter function
def filter_dataframe(df, difficulty, skills, topic):
    if topic != "All":
        df = df[df["Topic"] == topic]
    if difficulty:
        df = df[df["Difficulty"] == difficulty]
    if skills and skills != "Select All":
        df = df[df["Skills_involved"] == skills]
    return df

# Filter the dataframe based on selected options
filtered_df = filter_dataframe(df, difficulty, skills, topic)



# Filter the dataframe based on selected options
filtered_df = filter_dataframe(df, difficulty, skills, topic)

# Display the filtered dataframe in a table format
if st.checkbox("Show All Data"):
    st.dataframe(df)
else:
    st.dataframe(filtered_df.style.set_table_styles([{'selector': 'th', 'props': [('max-width', '150px')]}]).set_properties(**{'text-align': 'center'}))

# Add a footer
st.markdown("Use this dashboard to self-orientate within these French classes. You can select the level of difficulty you desire, the skills you want to practice, as well as the topics you want to approach. "
            ""
            "When selecting an activity, please read carefully the column 'Assignment' which tells you how to proceed, and go to the link in the columns Link1 and Link2. Sometimes, the activity is standalone and does not have a link: it's the case for challenges or games, for instance. ")
footer = st.text_input("", "© 2023 - CM")
