import streamlit as st
from scraper import scrape
from image_processing import merge_images, image_to_text
from analysis import perform_analysis
from langchain_groq import ChatGroq

# Initialize the ChatGroq model
chat = ChatGroq(
    model="llama-3.2-11b-vision-preview",  # you can use an of the suited models
    temperature=0.6,
    max_tokens=1024,
    timeout=None,
    max_retries=2,
    groq_api_key='groq_api_key'  # Replace with your Groq API key
)

def main():
    st.title("RetailCheck AI: Transforming Product Quality Control in Retail")

    # Input section for item link
    item_link = st.text_input("Enter the product link (e.g., Amazon link):")

    if st.button("Scrape Data"):
        if item_link:
            # Step 1: Scrape product specifications from the website
            scraped_data = scrape(item_link)

            # Step 2: Display scraped data
            st.subheader("Scraped Data:")
            st.write(scraped_data)
        else:
            st.error("Please enter a valid product link.")

    # Upload section for images
    uploaded_files = st.file_uploader("Upload images for OCR", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])

    if st.button("Analyze Images"):
        if uploaded_files:
            images = [Image.open(uploaded_file) for uploaded_file in uploaded_files]

            # Step 4: Merge images
            merged_image = merge_images(images, direction='vertical')  # Merge images

            # Step 5: Perform OCR on the merged image
            img_txt = image_to_text(merged_image)

            # Step 6: Convert img_txt elements to a single string
            img_txt_str = " ".join([str(element.text) for element in img_txt if hasattr(element, 'text')])

            # Step 7: Prepare the prompt for comparison
            prompt = (
                f"You are an AI assistant that helps to find the differences between the real product specifications "
                f"from the website and the user-given image data. \n\n"
                f"Site Data:\n{scraped_data}\n\n"
                f"Image Data:\n{img_txt_str}\n\n"
                "Please analyze the specifications mentioned in the site data as part of the image data and give your analysis report in detail"
            )

            # Step 9: Send the message to the model
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                    ],
                }
            ]
            response = chat.invoke(messages)

            # Display the analysis report
            st.subheader("Analysis Report:")
            st.write(response.content)
        else:
            st.error("Please upload at least one image.")

if __name__ == "__main__":
    main()
