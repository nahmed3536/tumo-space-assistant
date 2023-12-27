"""
Contains information and custom prompts for the app
"""

# custom instruction for LLM
instructions = """
Instructions:
You are an educational assistant helping students learn about the solar system and space.
Answer all questions in a friendly, educational manner (as if speaking to a student).
Any questions not related to space, the planets, the solar system, please answer with: "I can only answer questions about space!"
Keep your answers as a paragraph with 3-5 sentences maximum (no more than 500 words).
Thank you!

More specialized instructions:
"""

# page information organized by page index
content = {
    0: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Sun",
        "column_widths": [1, 5, 1],
        "image": "images/sun.png",
        "information": "The Sun is the star at the center of the Solar System. It is a massive, hot ball of plasma, inflated and heated by energy produced by nuclear fusion reactions at its core.",
        "additional_llm_context": "Answer all questions with a focus on our solar system's Sun",
    }, 
    1: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Mercury",
        "column_widths": [1, 2, 1],
        "image": "images/mercury.png",
        "information": "Mercury, the smallest and innermost planet in our solar system, experiences extreme temperature variations due to its lack of a significant atmosphere, resulting in scorching daytime highs and frigid nighttime lows on its heavily cratered surface.",
        "additional_llm_context": "Answer all questions with a focus on Mercury",
    }, 
    2: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Venus",
        "column_widths": [2, 3, 2],
        "image": "images/venus.png",
        "information": "Venus is the second planet from the sun and is similar in size to Earth, often referred to as Earth's 'sister planet.' It is characterized by a thick, toxic atmosphere composed mainly of carbon dioxide, causing a runaway greenhouse effect and making it the hottest planet in our solar system.",
        "additional_llm_context": "Answer all questions with a focus on Venus",
    },
    3: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Earth",
        "column_widths": [2, 3, 2],
        "image": "images/earth.png",
        "information": "Earth is the third planet from the Sun and the only astronomical object known to harbor life. This is enabled by Earth being a water world, the only one in the Solar System sustaining liquid surface water.",
        "additional_llm_context": "Answer all questions with a focus on Earth",
    },
    4: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Mars",
        "column_widths": [2, 3, 2],
        "image": "images/mars.png",
        "information": "Mars, the fourth planet from the sun, is often called the 'Red Planet' due to its rusty appearance. It features a diverse landscape, including expansive deserts, polar ice caps, and evidence of ancient riverbeds, sparking interest in the possibility of past or present Martian life.",
        "additional_llm_context": "Answer all questions with a focus on Mars",
    },
    5: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Jupiter",
        "column_widths": [1, 5, 1],
        "image": "images/jupiter.png",
        "information": "Jupiter is the largest planet in our solar system, with a diameter over 11 times that of Earth. Known for its prominent bands of clouds and the iconic Great Red Spot—a massive storm—Jupiter is a gas giant primarily composed of hydrogen and helium.",
        "additional_llm_context": "Answer all questions with a focus on Jupiter",
    },
    6: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Saturn",
        "column_widths": [1, 7, 1],
        "image": "images/saturn.png",
        "information": "Saturn, the sixth planet from the sun, is recognized for its stunning ring system, consisting of intricate and extensive bands of ice and rock particles. This gas giant, second in size only to Jupiter, boasts a distinctive golden hue and a diverse array of moons, including the large moon Titan.",
        "additional_llm_context": "Answer all questions with a focus on Saturn",
    },
    7: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Uranus",
        "column_widths": [1, 2.5, 1],
        "image": "images/uranus.png",
        "information": "Uranus is the seventh planet from the sun and is distinguished by its unique sideways rotation, causing it to roll on its side. This ice giant is composed mainly of hydrogen, helium, and methane, and it has a faint ring system.",
        "additional_llm_context": "Answer all questions with a focus on Uranus",
    },
    8: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Neptune",
        "column_widths": [1, 3, 1],
        "image": "images/neptune.png",
        "information": "Neptune, the eighth and farthest planet from the sun, is a frigid, gaseous giant with a vivid blue hue due to the presence of methane in its atmosphere. It possesses strong winds and a notable dark storm called the Great Dark Spot, resembling Jupiter's Great Red Spot.",
        "additional_llm_context": "Answer all questions with a focus on Neptune",
    },
    9: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Pluto",
        "column_widths": [2, 1, 2],
        "image": "images/pluto.png",
        "information": "Pluto, once considered the ninth planet, is now classified as a dwarf planet in our solar system. It has a highly elliptical orbit and is characterized by a frigid environment, with temperatures reaching as low as -375 degrees Fahrenheit (-225 degrees Celsius).",
        "additional_llm_context": "Answer all questions with a focus on Pluto",
    },
}
sorted_page_nums = sorted(content.keys())
first_page_num = sorted_page_nums[0]
last_page_num = sorted_page_nums[-1]