import openai

openai.api_key = "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"  # Replace with your OpenAI API key

def generate_slide_content(topic):
    prompt = f"Slide: {topic}\n\n"

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
    )

    return response.choices[0].text.strip()

def generate_presentation(topic, num_slides):
    slides = []

    for slide_number in range(1, num_slides+1):
        slide_content = generate_slide_content(topic)
        slides.append(slide_content)

    return slides

def generate_presentation_with_themes(topic, num_slides):
    slides = []

    for slide_number in range(1, num_slides+1):
        slide_content = generate_slide_content(topic)
        theme = generate_slide_theme(topic)
        slides.append((slide_content, theme))

    return slides

def generate_slide_theme(topic):
    # Add your logic to generate slide themes based on the topic
    # You can use libraries like pyforest or any other method to determine themes

    # For simplicity, let's assume the theme is based on the topic's length
    theme = "light" if len(topic) <= 10 else "dark"

    return theme

# Usage examples
topic = "Artificial Intelligence"
num_slides = 5

slides = generate_presentation(topic, num_slides)
for slide_number, slide_content in enumerate(slides):
    print(f"Slide {slide_number + 1}: {slide_content}")

slides_with_themes = generate_presentation_with_themes(topic, num_slides)
for slide_number, slide in enumerate(slides_with_themes):
    slide_content, theme = slide
    print(f"Slide {slide_number + 1} (Theme: {theme}): {slide_content}")
