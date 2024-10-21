from langchain_groq import ChatGroq

def perform_analysis(scraped_data, img_txt_str, chat):
    """Prepares the prompt and sends it to the ChatGroq model."""
    prompt = (
        f"You are an AI assistant that helps to find the differences between the real product specifications "
        f"from the website and the user-given image data. \n\n"
        f"Site Data:\n{scraped_data}\n\n"
        f"Image Data:\n{img_txt_str}\n\n"
        "Please analyze the specifications mentioned in the site data as part of the image data and give your analysis report in detail"
    )

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
            ],
        }
    ]
    response = chat.invoke(messages)
    return response.content
