"""
Contains information and custom prompts for the app
"""

# custom instruction for LLM
instructions = """
"""

# page information organized by page index
content = {
    0: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Sun",
        "column_widths": [1, 2, 1],
        "image": "images/sun.png",
        "information": "fill me in",
        "additional_llm_context": ""
    }, 
    1: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Mercury",
        "column_widths": [1, 2, 1],
        "image": "images/mercury.png",
        "information": "fill me in",
        "additional_llm_context": ""
    }, 
    2: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Venus",
        "column_widths": [1, 2, 1],
        "image": "images/venus.png",
        "information": "fill me in",
        "additional_llm_context": ""
    },
    3: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Earth",
        "column_widths": [1, 2, 1],
        "image": "images/earth.png",
        "information": "fill me in",
        "additional_llm_context": ""
    },
    4: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Mars",
        "column_widths": [1, 2, 1],
        "image": "images/mars.png",
        "information": "fill me in",
        "additional_llm_context": ""
    },
    5: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Jupiter",
        "column_widths": [1, 2, 1],
        "image": "images/jupiter.png",
        "information": "fill me in",
        "additional_llm_context": ""
    },
    6: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Saturn",
        "column_widths": [1, 2, 1],
        "image": "images/saturn.png",
        "information": "fill me in",
        "additional_llm_context": ""
    },
    7: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Uranus",
        "column_widths": [1, 2, 1],
        "image": "images/uranus.png",
        "information": "fill me in",
        "additional_llm_context": ""
    },
    8: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Neptune",
        "column_widths": [1, 2, 1],
        "image": "images/neptune.png",
        "information": "fill me in",
        "additional_llm_context": ""
    },
    9: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Pluto",
        "column_widths": [1, 2, 1],
        "image": "images/pluto.png",
        "information": "fill me in",
        "additional_llm_context": ""
    },
}
sorted_page_nums = sorted(content.keys())
first_page_num = sorted_page_nums[0]
last_page_num = sorted_page_nums[-1]