"""
Design Decision:

Welcome splash page, where they are welcome and can start on earth (need explicit click)

Sun > Mercury > Venus > Earth > Mars > Jupiter > Saturn > Uranus > Neptune > Pluto > Milky Way Galaxy > Andromeda Galaxy >  Virgo Supercluster
"""

import streamlit as st

# set the page / tab title
st.set_page_config(page_title="NebulaGPT")

# access toml configuration
import toml
config = toml.load(".streamlit/config.toml")

# set background image
import base64

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

# load in custom CSS 
import style

def local_css(css):
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

local_css(style.css)

# web-app elements
def navigationButtons():
    # navigation buttons
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        pass
    with col2:
        st.button('Previous', type="secondary", use_container_width=True, on_click=prevPage)
    with col3:
        pass
    with col4:
        st.button('Next', type="primary", use_container_width=True, on_click=nextPage)
    with col5:
        pass

def spacer(height: int = 50):
    st.markdown(
        f"""
        <style>
            .custom-spacer {{
                height: {height}px;  /* Adjust the height as needed */
            }}
        </style>
        <div class="custom-spacer"></div>
        """,
        unsafe_allow_html=True
    )

def center_head(text: str):
    st.markdown(f"<h1 style='text-align: center; font-family: {config['theme']['font']}; color: {config['theme']['textColor']};'>{text}</h1>", unsafe_allow_html=True)

def text(text: str):
    st.markdown(f"<p style='font-family: {config['theme']['font']}; color: {config['theme']['textColor']};'>{text}</h1>", unsafe_allow_html=True)

# pages functionality 
if 'page' not in st.session_state: st.session_state.page = -1
def prevPage(): st.session_state.page -= 1 # move back a page
def nextPage(): st.session_state.page += 1 # move forward a page
def earthPage(): st.session_state.page = 3 # go to Earth page

# create a page container
page = st.empty()

# welcome page
if st.session_state.page == -1:
    with page.container():
        set_background("images/homepage_background.jpeg")
        center_head("Welcome to NebulaGPT")
        st.markdown(f"<h4 style='font-family: {config['theme']['font']}; color: {config['theme']['textColor']}; font-weight: bold; text-stroke: 1px black;'>Your AI assistant to explore the Solar System and Space!</h4>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='font-family: {config['theme']['font']}; color: {config['theme']['textColor']}; font-weight: bold;'>Begin your journey at Earth!</h4>", unsafe_allow_html=True)
        spacer()

        # button to navigate to Earth
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button('Go to Earth', type="secondary", use_container_width=True, on_click=earthPage)
        with col2:
            pass
        with col3:
            pass

# sun page
if st.session_state.page == 0:
    pass

# mercury page
if st.session_state.page == 1:
    pass

# venus page
if st.session_state.page == 2:
    pass

# earth page
if st.session_state.page == 3:
    with page.container():
        set_background("images/solar_system_background.jpeg")
        center_head("Earth")
        with st.columns([1, 2, 1])[1]:
            st.image("images/earth.png", use_column_width = True)
        
        # Define the background color and text color
        background_color = "#141317"
        text_color = "#ffffff"

        # Define the content for the text box
        text_box_content = f"""
            <div style="background-color: {background_color}; padding: 10px; border-radius: 10px;">
                <h6 style="color: {text_color};">Information about Earth</h6>
            </div>
        """

        # Display the text box using markdown
        st.markdown(text_box_content, unsafe_allow_html=True)

        def get_response(prompt):
            # Replace this with your logic to generate a response based on the input prompt
            # For now, let's just echo the prompt as a response
            return f":green[You said: {prompt}]"
        

        user_input = st.text_input(" ", placeholder="Have more questions? Ask it here!", label_visibility="hidden", key="user_input")

        # Check if the user pressed Enter (carriage return)
        if user_input and st.session_state.prev_input != user_input:
            # Get response based on user input
            response = get_response(user_input)

            # Display the response
            text_box_content = f"""
            <div style="background-color: #FFFFFF; padding: 10px; border-radius: 10px;">
                <h2 style="color: #000000;">{response}</h2>
                <p style="color: #000000;">This is a sample text box with a background color.</p>
            </div>
            """
            st.markdown(text_box_content, unsafe_allow_html=True)

        # Update the previous input
        st.session_state.prev_input = user_input

        spacer()
        navigationButtons()






#         st.header("This is page 1")
#         st.button("Go to page 2",on_click=nextPage)
#         st.write(st.session_state.page)
#         time.sleep(2)
#         nextPage()
#         st.write(st.session_state.page)




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


# import streamlit as st

# # st.set_page_config(layout="wide")

# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# local_css("style.css")

# import base64
# import time

# # Set the background image using HTML and CSS
# def get_base64(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# def set_background(png_file):
#     bin_str = get_base64(png_file)
#     page_bg_img = '''
#     <style>
#     .stApp {
#     background-image: url("data:image/png;base64,%s");
#     background-size: cover;
#     }
#     </style>
#     ''' % bin_str
#     st.markdown(page_bg_img, unsafe_allow_html=True)

# Display the background image using st.markdown
# set_background("images/solar_system_background.jpeg")

# # Add other Streamlit components below
# st.title("My Streamlit App")
# st.write("This is my Streamlit app with a custom background image.")

# # Function to show the welcome message
# def show_welcome_message():
#     with content_placeholder.container(): 
#         st.title("Welcome to the Planets App!")
#         st.write("Loading...")

# # Placeholder for dynamic content
# content_placeholder = st.empty()

# # Show the welcome message initially
# show_welcome_message()

# # Simulate a delay for loading the main app
# time.sleep(2)

# # Replace the content with the main app
# content_placeholder = st.empty()



# # Placeholder data for planets
# planets_data = {
#     'Mercury': {'image_url': 'images/mercury.png', 'info': 'Information about Mercury'},
#     'Venus': {'image_url': 'images/venus.png', 'info': 'Information about Venus'},
#     'Earth': {'image_url': 'images/earth.png', 'info': 'Information about Earth'},
#     'Mars': {'image_url': 'images/mars.png', 'info': 'Information about Mars'},
#     'Jupiter': {'image_url': 'images/jupiter.png', 'info': 'Information about Jupiter'},
#     'Saturn': {'image_url': 'images/saturn.png', 'info': 'Information about Saturn'},
#     'Uranus': {'image_url': 'images/uranus.png', 'info': 'Information about Uranus'},
#     'Neptune': {'image_url': 'images/neptune.png', 'info': 'Information about Neptune'}
# }


# # Create a container for the header
# header_container = st.container()

# # Set the layout for the header
# header_container.markdown(
#     f'<div style="display: flex; justify-content: space-between; align-items: center;">'
#     f'<div>Left Button</div>'
#     f'<div style="text-align: center;"><h1>Explore Planets</h1></div>'
#     f'<div style="text-align: right;">Right Button</div>'
#     f'</div>',
#     unsafe_allow_html=True
# )


# col1, col2, col3 = st.columns(3)

# with col1:
#     # Button on the left
#     left_button = st.button("Left Button")

# with col2:
#     # Title in the center
#     st.title("Explore Planets")

# with col3:
#     # Button on the right
#     right_button = st.button("Right Button")


# col1, col2, col3 , col4, col5 = st.columns(5)

# with col1:
#     pass
# with col2:
#     st.button('Previous')
# with col3:
#     pass
# with col4:
#     st.button('Next',  type="primary")
# with col5:
#     pass

# # Pages logic 
# if 'page' not in st.session_state: st.session_state.page = 0
# def nextPage(): st.session_state.page += 1
# def firstPage(): st.session_state.page = 0

# ph = st.empty()

# ## Page 0
# if st.session_state.page == 0:
#     with ph.container():
#         st.header("This is page 1")
#         st.button("Go to page 2",on_click=nextPage)
#         st.write(st.session_state.page)
#         time.sleep(2)
#         nextPage()
#         st.write(st.session_state.page)

# ## Page 1
# elif st.session_state.page == 1:
#     with ph.container():
#         st.header("This is page 2")
#         st.write("Other stuff in page 2")
#         st.write("More stuff in page 2")
#         st.write("More more stuff in page 2")
#         st.write("More more more stuff in page 2")
#         st.button("Go to page 3",on_click=nextPage)

# ## Page 2
# elif st.session_state.page == 2:
#     with ph.container():
#         st.header("This is page 3")
#         st.image("https://placekitten.com/g/1400/600",caption=f"Meowhy")
#         st.button("Go back",on_click=firstPage)


# # Display clickable images along the main section
# st.title("Explore Planets")

# st.button(st.image("images/mars.png"))

# for planet, data in planets_data.items():
#     st.subheader(planet)

#     # Add a button to show/hide the chat window when the image is clicked
#     if st.button(f"Show Chat about {planet}", key=f"button_{planet}"):
#         st.header(f"Chat about {planet}")
#         question = st.text_input("Type your question here:")
#         if st.button("Ask"):
#             st.success(f"You asked about {planet}: {question}")

#     # Display the image within the button
#     if st.button("", key=f"button_image_{planet}"):
#         st.image(data['image_url'], use_column_width=True, caption=f"Click to chat about {planet}")

#     # Display the information about the planet
#     st.write(data['info'])

#     # Add a separator between planets
#     st.markdown("---")


# # Loop through each planet and display information vertically
# for planet, data in planets_data.items():
#     st.subheader(planet)
#     st.image(data['image_url'], use_column_width=True)
    
#     # Add a button to open a chat window for each planet
#     if st.button(st.image(data['image_url'], use_column_width=False)):
#         st.header(f"Chat about {planet}")
#         question = st.text_input("Type your question here:")
#         if st.button("Ask"):
#             st.success(f"You asked about {planet}: {question}")

#     # Display the information about the planet
#     st.write(data['info'])

#     # Add a separator between planets
#     st.markdown("---")


# # Create a horizontally scrollable row of images with a button for each planet
# col1, col2, col3 = st.columns(3)
# selected_planet_index = 0

# with col1:
#    st.header("A cat")
#    st.image("https://static.streamlit.io/examples/cat.jpg")

# with col2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg")

# with col3:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg")

# # Function to show the planet information
# def show_planet_info(planet):
#     st.image(planets_data[planet]['image_url'], use_column_width=True)
#     st.info(planets_data[planet]['info'])

# # Display the current planet
# current_planet = list(planets_data.keys())[selected_planet_index]
# show_planet_info(current_planet)

# # Add buttons for navigation
# with st.container():
#     prev_button = st.button("Previous", key="prev_button")
#     st.text(f"Current Planet: {current_planet}")
#     next_button = st.button("Next", key="next_button")

# # Handle button clicks
# if prev_button and selected_planet_index > 0:
#     selected_planet_index -= 1
# elif next_button and selected_planet_index < len(planets_data) - 1:
#     selected_planet_index += 1

# # Update and display the selected planet
# current_planet = list(planets_data.keys())[selected_planet_index]
# show_planet_info(current_planet)


# # Add a chat box for questions
# st.header("Ask Questions")
# question = st.text_input("Type your question here:")
# if st.button("Ask"):
#     st.success(f"You asked: {question}")
