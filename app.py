# import streamlit as st

# import base64

# @st.cache_data(allow_output_mutation=True)
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# def set_png_as_page_bg(png_file):
#     bin_str = get_base64_of_bin_file(png_file)
#     page_bg_img = '''
#     <style>
#     body {
#     background-image: url("data:image/png;base64,%s");
#     background-size: cover;
#     }
#     </style>
#     ''' % bin_str
    
#     st.markdown(page_bg_img, unsafe_allow_html=True)
#     return

# set_png_as_page_bg('images/solar_system_background.jpeg')


# # Function to display planet information
# def display_planet_info(planet):
#     st.write(f"## {planet.capitalize()} Information")
#     # Add information about the planet
#     # You can customize this based on your needs

# def main():

#     st.title("Solar System Explorer")

#     planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]

#     selected_planet = st.sidebar.selectbox("Select a Planet", planets)

#     # Display planet icon in the sidebar
#     st.sidebar.image(f"images/{selected_planet}.png", use_column_width=True)

#     # Display planet information
#     display_planet_info(selected_planet)

# if __name__ == "__main__":
#     main()


import streamlit as st
import base64

# Set the background image using HTML and CSS
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Display the background image using st.markdown
set_background("images/solar_system_background.jpeg")

# Add other Streamlit components below
st.title("My Streamlit App")
st.write("This is my Streamlit app with a custom background image.")
