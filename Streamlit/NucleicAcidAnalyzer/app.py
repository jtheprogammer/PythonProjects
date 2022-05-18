import streamlit as st
from multipage import MultiPage
from apps import DNA, RNA

app = MultiPage()

st.title("Nucleotide Count Web App")


# Add all your applications (pages) here
app.add_page("DNA Count", DNA.app)
app.add_page("RNA Count", RNA.app)


# The main app
app.run()