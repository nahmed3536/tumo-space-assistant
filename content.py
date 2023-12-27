"""
Contains information and custom prompts for the app
"""

# custom instruction for LLM
instructions = """
Instructions:
You are an educational assistant helping students learn about the solar system and space.
Answer all questions in a friendly, educational manner (as if speaking to a student).
Any questions not related to space or the solar system, please answer with: "I can only answer questions about space!"
Keep your answers as a paragraph with 3-5 sentences maximum (no more than 500 words).
Thank you!

More specialized instructions:
"""

# page information organized by page index
content = {
    0: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Sun",
        "column_widths": [1, 2, 1],
        "image": "images/sun.png",
        "information": "The sun, a luminous and massive celestial body, plays a pivotal role in sustaining life on Earth. Powered by nuclear fusion reactions in its core, the sun releases an unfathomable amount of energy in the form of light and heat. This energy drives Earth's climate, weather systems, and the vital process of photosynthesis, providing the foundation for the entire food chain. Understanding the sun's intricate processes is fundamental to unraveling the mysteries of astrophysics, as it serves as a natural laboratory for studying high-energy phenomena, magnetic fields, and stellar evolution. Researchers employ various instruments, such as solar telescopes and space probes, to scrutinize the sun's surface, atmosphere, and solar wind, contributing to our knowledge of both our immediate cosmic neighborhood and the broader universe.",
        "additional_llm_context": "Answer all questions with a focus on our solar system's Sun",
    }, 
    1: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Mercury",
        "column_widths": [1, 2, 1],
        "image": "images/mercury.png",
        "information": "Mercury, the smallest and innermost planet in our solar system, is a rocky world with a myriad of unique characteristics. Boasting extreme temperature variations due to its lack of a substantial atmosphere, Mercury experiences scorching daytime temperatures that can reach up to 800 degrees Fahrenheit (427 degrees Celsius) and frigid nighttime lows plunging to -290 degrees Fahrenheit (-179 degrees Celsius). Despite being the closest planet to the sun, its surface is not uniform, featuring expansive plains, steep cliffs, and impact craters. Mercury's slow rotation on its axis results in a 2:3 resonance with its orbit around the sun, meaning it completes three rotations for every two orbits. This peculiarity contributes to its peculiar day-night cycle, lasting approximately 176 Earth days, and showcases the fascinating dynamics at play in our solar system's innermost realms.",
        "additional_llm_context": "Answer all questions with a focus on Mercury",
    }, 
    2: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Venus",
        "column_widths": [1, 2, 1],
        "image": "images/venus.png",
        "information": "fill me in",
        "additional_llm_context": "Answer all questions with a focus on Venus",
    },
    3: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Earth",
        "column_widths": [1, 2, 1],
        "image": "images/earth.png",
        "information": "fill me in",
        "additional_llm_context": "Answer all questions with a focus on Earth",
    },
    4: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Mars",
        "column_widths": [1, 2, 1],
        "image": "images/mars.png",
        "information": "fill me in",
        "additional_llm_context": "Answer all questions with a focus on Mars",
    },
    5: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Jupiter",
        "column_widths": [1, 2, 1],
        "image": "images/jupiter.png",
        "information": "fill me in",
        "additional_llm_context": "Answer all questions with a focus on Jupiter",
    },
    6: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Saturn",
        "column_widths": [1, 2, 1],
        "image": "images/saturn.png",
        "information": "fill me in",
        "additional_llm_context": "Answer all questions with a focus on Saturn",
    },
    7: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Uranus",
        "column_widths": [1, 2, 1],
        "image": "images/uranus.png",
        "information": "fill me in",
        "additional_llm_context": "Answer all questions with a focus on Uranus",
    },
    8: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Neptune",
        "column_widths": [1, 2, 1],
        "image": "images/neptune.png",
        "information": "fill me in",
        "additional_llm_context": "Answer all questions with a focus on Neptune",
    },
    9: {
        "background_img": "images/solar_system_background.jpeg",
        "header": "Pluto",
        "column_widths": [1, 2, 1],
        "image": "images/pluto.png",
        "information": "fill me in",
        "additional_llm_context": "Answer all questions with a focus on Pluto",
    },
}
sorted_page_nums = sorted(content.keys())
first_page_num = sorted_page_nums[0]
last_page_num = sorted_page_nums[-1]