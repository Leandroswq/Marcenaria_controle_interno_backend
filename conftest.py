import sys
import os

# Obtenha o caminho absoluto para a pasta raiz do projeto
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Adicione o caminho raiz ao sys.path
sys.path.insert(0, root_path)