

---

# RetailCheck AI 🛍️🤖
## Transforming Product Quality Control in Retail ##


## Overview

**RetailCheck AI** is a Streamlit application designed to streamline product quality control in the retail sector. By leveraging LLMs Augmentation power,web scraping, Optical Character Recognition (OCR), and advanced AI analysis, this tool allows users to compare product specifications from various online sources with user-uploaded images, ensuring accuracy and quality.

## Features ✨

- **Web Scraping**: Automatically scrape product specifications from provided URLs. 🌐
- **Image Processing**: Upload multiple images, which are merged for OCR processing to extract text. 🖼️
- **AI Analysis**: Utilize the ChatGroq model to analyze and compare scraped data with the text extracted from images. 📊
- **User-Friendly Interface**: Easy-to-use interface built with Streamlit, providing an interactive experience. 🖥️

## Installation ⚙️

To run this project, you need to install the necessary Python packages. You can do this by using the provided `requirements.txt` file:

1. Clone the repository (or download the files):
   ```bash
   git clone https://github.com/AdityaSagarr/RetailCheck-AI.git
   cd RetailCheck-AI
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Tesseract OCR and its language packages:
   ```bash
   sudo apt install tesseract-ocr -y
   sudo apt install tesseract-ocr-kan -y
   ```

## Usage 🚀

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`. 🌍

3. Enter a product link (e.g., Amazon link) in the input field to scrape specifications. 🔗

4. Upload images for analysis using the file uploader. 📤

5. Click on the “Analyze Images” button to receive a detailed analysis report comparing the scraped data with the image data. 📝

## Code Structure 🏗️

The project is structured as follows:

```
RetailCheck-AI/
│
├── app.py                  # Main Streamlit application file
├── image_processing.py      # Functions for image merging and OCR
├── scraper.py               # Functions for web scraping
├── analysis.py              # Functions for AI analysis
└── requirements.txt         # List of required Python packages
```



## Author 🧑‍💻

**Aditya Sagar**  
[![LinkedIn Logo](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/adityasagarr)  


## Project Screenshot/Output  📸
![tuxpi com 1729519724](https://github.com/user-attachments/assets/b406f9d1-8899-411f-8249-d08763d7d3d0)


---
