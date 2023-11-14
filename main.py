from pathlib import Path

import streamlit as st
from PIL import Image
import pandas as pd
from bokeh.plotting import figure








current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
profile_pic = current_dir / "assets" / "profile-pic.png"

PAGE_TITLE = "CV | GABRIEL GARCIA"
PAGE_ICON = "😁"
NAME = "Gabriel Garcia"
DESCRIPTION = """
Étudiant à Paris Ynov Campus.
"""
EMAIL = "garciagabriel78@ynov.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/gabriel-g-04a9aa13b/",
    "GitHub": "https://github.com/Gabriel78630",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

    
profile_pic = Image.open(profile_pic)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    
    st.write("📫", EMAIL)

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write("#")
st.subheader("Competénces")
st.write(
    """
- ✔️ CAPACITES D’ANALYSE
- ✔️ ESPRIT DE RESPONSABILITE
- ✔️ TRAVAIL EN EQUIPE
- ✔️ CAPACITE D’ADAPTATION
- ✔️ GESTION DU STRESS

"""
)

st.write("#")
st.subheader("Competénces en informatiques")
st.write(
    """
Java | Python | Golang | C# | C++ | Javascript |
HTML | CSS | Git  La gestion de reseaux, (windows server,
ubuntu, debian)

"""
)



st.write("#")
st.subheader("Data Skills")
st.write(
    """
- 👩‍💻 Programmation: Python, SQL, Go Lang, Bash, JavaScript
- 🗄️ Databases: Postgres, SambaDB, MySQL, SQLlite
"""
)

st.write("#")
st.subheader("🌍 Langues")

# Load the CSV data into a Pandas DataFrame
data = pd.DataFrame({'Language': ['Espagnol', 'Français', 'Anglais'], 'Scores': [5, 10, 10]})

# Create a Bokeh figure
p = figure(y_range=data['Language'], height = 300, width=600, title="Language Scores")
p.hbar(y=data['Language'], right=data['Scores'], height=0.9)

# Show the Bokeh figure in Streamlit
st.bokeh_chart(p)

# st.write("#")
st.write("---")
# st.write("#")

st.subheader("Formations")

st.write(" - 📚 Baccalauréat (Physique, Mathématiques et Informatique)")
st.write("École de l'ambassade de la Fédération de Russie, Vietnam(Vung Tau) - 09.2016 / 06.2019")
st.write(" - 📙 Mastère Informatique")
st.write("Paris Ynov Campus, Nanterre - 09.2020 / 04.2025")

# st.write("\n")
st.write("---")
# st.write("\n")

st.subheader("Expérience étudiant")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Hangman web")
   st.image("./assets/Hangmanweb.png")

with col2:
   st.header("Projet Forum")
   st.image("./assets/forum.jpeg")

with col3:
   st.header("Projet SQL")
   st.image("./assets/sql.png")


st.subheader("Expériences professionelles")
st.write("🪖🫡 Armée de terre")
st.write("2019-2022")
st.write("Sergent dans l'armée de terre")

# st.write("#")
st.write("---")
# st.write("#")

st.subheader("Intérêts")
st.write("- ⚽️ | 🦾 | 🎧 | 🎵")

# st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")