import streamlit as st
from multiapp import MultiApp
from apps import home

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)

# The main app
app.run()