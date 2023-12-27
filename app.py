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

# set up chatgpt API
import os
import openai

openai_client = openai.OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
)

def chatgpt(prompt: str, context: str = "You are a helpful assistant.", model: str = "gpt-3.5-turbo") -> str:
    response = openai_client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": context,
            },
             {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
    )
    return response.choices[0].message.content

# customized assistant
def custom_assistant(prompt: str, general_instructions: str, page_context: str) -> str:
    """
    Custom logic for our assistant
    """
    context = f"{general_instructions}\n{page_context}"
    return chatgpt(prompt, context)

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
def navigationButtons(include_prev: bool = True, include_next: bool = True):
    """
    Navigation buttons between pages with `include_prev` and `include_next` toggles for first and last page
    """
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        pass
    with col2:
        if include_prev:
            st.button('Previous', type="secondary", use_container_width=True, on_click=prevPage)
        else:
            pass
    with col3:
        pass
    with col4:
        if include_next:
            st.button('Next', type="primary", use_container_width=True, on_click=nextPage)
        else: 
            pass
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
    st.markdown(f"<h1 style='text-align: center; font-family: {config['markdown']['font']}; color: {config['markdown']['textColor']};'>{text}</h1>", unsafe_allow_html=True)

def text(text: str):
    st.markdown(f"<p style='font-family: {config['markdown']['font']}; color: {config['markdown']['textColor']};'>{text}</h1>", unsafe_allow_html=True)

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
        st.markdown(f"<h4 style='font-family: {config['markdown']['font']}; color: {config['markdown']['textColor']}; font-weight: bold; text-stroke: 1px black;'>Your AI assistant to explore the Solar System and Space!</h4>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='font-family: {config['markdown']['font']}; color: {config['markdown']['textColor']}; font-weight: bold;'>Begin your journey at Earth!</h4>", unsafe_allow_html=True)
        spacer()

        # button to navigate to Earth
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button('Go to Earth', type="secondary", use_container_width=True, on_click=earthPage)
        with col2:
            pass
        with col3:
            pass


# page template populate from content.py
import content

if 'last_page_assistant_called_on' not in st.session_state: st.session_state.last_page_assistant_called_on = -1

def page_template(page_num):
    """
    Template that is populated based on `page_num`
    """ 
    page_content = content.content[page_num]

    # set background, header, and image
    set_background(page_content["background_img"])
    center_head(page_content["header"])
    with st.columns(page_content["column_widths"])[1]:
        st.image(page_content["image"], use_column_width = True)

    # define and display information for the page
    text_box_content = f"""
        <div style="background-color: {config['theme']['backgroundColor']}; padding: 10px; border-radius: 10px;">
            <h6 style="font-family: {config['markdown']['font']}; color: {config['markdown']['textColor']};">{page_content['information']}</h6>
        </div>
    """
    st.markdown(text_box_content, unsafe_allow_html=True)

    # chat interface
    user_input = st.text_input(" ", placeholder="Have more questions? Ask it here!", label_visibility="hidden", key="user_input")       

    if user_input and st.session_state.prev_input != user_input:
        # get response based on user input
        response = custom_assistant(user_input, content.instructions, page_content['additional_llm_context'])

        # display the response
        text_box_content = f"""
        <div style="background-color: {config['theme']['secondaryBackgroundColor']}; padding: 10px; border-radius: 10px;">
            <h6 style="color: {config['theme']['textColor']};">{response}</h6>
        </div>
        """
        st.markdown(text_box_content, unsafe_allow_html=True)

        # update the page number that the assistant was last called on - this allows the chat to be asked when the page swaps
        st.session_state.last_page_assistant_called_on = page_num

    # update the session input variable
    st.session_state.prev_input = user_input

    spacer()

    # handle logic for first and last page
    include_prev = page_num != content.first_page_num
    include_next = page_num != content.last_page_num
    navigationButtons(include_prev, include_next)

# sun page
if st.session_state.page == 0:
    with page.container():
        page_template(0)

# mercury page
if st.session_state.page == 1:
    with page.container():
        page_template(1)

# venus page
if st.session_state.page == 2:
    with page.container():
        page_template(2)

# earth page
if st.session_state.page == 3:
    with page.container():
        page_template(3)

# mars page
if st.session_state.page == 4:
    with page.container():
        page_template(4)

# jupiter page
if st.session_state.page == 5:
    with page.container():
        page_template(5)

# saturn page
if st.session_state.page == 6:
    with page.container():
        page_template(6)

# uranus page
if st.session_state.page == 7:
    with page.container():
        page_template(7)

# neptune page
if st.session_state.page == 8:
    with page.container():
        page_template(8)

# pluto page
if st.session_state.page == 9:
    with page.container():
        page_template(9)