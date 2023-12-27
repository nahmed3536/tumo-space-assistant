# access toml configuration
import toml
config = toml.load(".streamlit/config.toml")

# create custom css
css = f"""
button[kind="primary"] {{
  background-color: {config['buttons']['primaryBackgroundColor']};
  border: {config['buttons']['primaryBorder']};
  color: {config['buttons']['primaryColor']};
  font-family: {config['theme']['font']};
}}

button[kind="primary"]:hover {{
  background-color: {config['buttons']['primaryHoverBackgroundColor']};
  border: {config['buttons']['primaryHoverBorder']};
  color: {config['buttons']['primaryHoverColor']};
  font-family: {config['theme']['font']};
}}

button[kind="secondary"] {{
  background-color: {config['buttons']['secondaryBackgroundColor']};
  border: {config['buttons']['secondaryBorder']};
  color: {config['buttons']['secondaryColor']};
  font-family: {config['theme']['font']};
}}

button[kind="secondary"]:hover {{
  background-color: {config['buttons']['secondaryHoverBackgroundColor']};
  border: {config['buttons']['secondaryHoverBorder']};
  color: {config['buttons']['secondaryHoverColor']};
  font-family: {config['theme']['font']};
}}
"""