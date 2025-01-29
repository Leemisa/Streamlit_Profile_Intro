import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Projects", "STEM Data Explorer", "Contact"],
)


# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Profile information
    name = "Leemisa Moleko"
    field = "Computer Science and Information Technology"
    institution = "North-West University"
    role = "Tutor, and Student Assistant"
    interests = "Software Development, Testing, Automation, Data Science, AI, and Innovation"
    
    # Profile section layout
    st.image("./Images/file.png", width=200)
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    st.write(f"**Role:** {role}")
    st.write(f"**Research Interests:** {interests}")

elif menu == "Projects":
    st.title("Projects")
    st.sidebar.header("Project Details")
    
    projects = [
        {"Title": "CRUD RESTful API for Telemetry Data", "Technology": "C#, .NET Core, Azure, GitHub"},
        {"Title": "Web App GUI Design", "Technology": "Blazor, HTML, CSS, JavaScript"},
        {"Title": "Power BI Report for NWU Tech Trends", "Technology": "Power BI, SQL, Data Analytics"},
        {"Title": "Automated UI Tasks with UiPath", "Technology": "UiPath, Excel, RPA"}
    ]
    df_projects = pd.DataFrame(projects)
    st.dataframe(df_projects)

elif menu == "STEM Data Explorer":
    st.title("STEM Data Explorer")
    st.sidebar.header("Data Selection")

    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore", 
        ["Software Development", "Robotic Process Automation", "Power BI Data Analysis"]
    )

elif menu == "Contact":
    st.header("Contact Information")
    email = "leemisamoleko@gmail.com"
    linkedin = "https://www.linkedin.com/in/leemisamoleko"
    github = "https://github.com/leemisamoleko"
    
    st.write(f"You can reach Leemisa Moleko at {email}.")
    st.write(f"**LinkedIn:** [Leemisa Moleko]({linkedin})")
    st.write(f"**GitHub:** [Leemisa Moleko]({github})")
