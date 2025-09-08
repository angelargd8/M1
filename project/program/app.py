import streamlit as st
import numpy as np
import sys
from antlr4 import *
from gen.CompiscriptLexer import CompiscriptLexer
from gen.CompiscriptParser import CompiscriptParser
from AstBuilder import AstBuilder
from AstVisualization import render_ast
from SemanticAnalyzer import SemanticAnalyzer


# Título de la aplicación
st.title("Demo de Streamlit")

# Descripción
st.write("Esta es una aplicación de demostración creada con Streamlit.")

# Entrada interactiva: Número
st.sidebar.header("Configuración")
num_points = st.sidebar.slider("Selecciona el número de puntos", min_value=10, max_value=100, value=50)





# Entrada de texto
user_input = st.text_input("Escribe algo:", "¡Hola, Streamlit!")
st.write(f"Tu entrada: {user_input}")