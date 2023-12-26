import streamlit as st

background_image = """
<style>
body {
    background-image: url('images/solar_system_background.jpeg')
    background-size: cover;
}
</style>
"""

# Function to display planet information
def display_planet_info(planet):
    st.write(f"## {planet.capitalize()} Information")
    # Add information about the planet
    # You can customize this based on your needs

def main():
    st.title("Solar System Explorer")

    planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]

    selected_planet = st.sidebar.selectbox("Select a Planet", planets)

    # Display planet icon in the sidebar
    st.sidebar.image(f"images/{selected_planet}.png", use_column_width=True)

    # Display planet information
    display_planet_info(selected_planet)

if __name__ == "__main__":
    main()
