# Urdu OCR — Code Saviours SI-26

## Project Overview

This project is an Urdu Optical Character Recognition (OCR) system developed during the Code Saviours SI-26 Machine Learning Internship.

The system extracts Urdu text from images and converts it into editable digital text using an Urdu TrOCR-based OCR pipeline.

The project covers dataset collection, image preprocessing, OCR testing, dataset expansion, model experimentation, evaluation and Streamlit deployment.

---

## What is OCR?

OCR stands for Optical Character Recognition.

It is a technology that converts text from images into machine-readable digital text.

OCR can be used to process scanned documents, newspapers, books, signboards and other images containing text.

---

## Why is Urdu OCR Challenging?

Urdu OCR is more challenging than English OCR because Urdu uses a connected and cursive writing style.

Characters can change their appearance depending on their position within a word. Urdu also contains dots, connected characters, ligatures and different writing styles and fonts.

These characteristics make accurate Urdu text recognition more difficult.

---

## Real-World Uses

Urdu OCR can be useful for:

- Digitizing Urdu books
- Digitizing newspapers
- Converting scanned documents into editable text
- Searching Urdu documents
- Preserving historical Urdu documents
- Reading Urdu signboards
- Creating searchable Urdu archives

---

## Project Workflow

The complete project workflow was:

1. Dataset collection
2. Dataset organization
3. Image preprocessing
4. Tesseract OCR testing
5. Gap analysis
6. Dataset expansion
7. PyTorch Dataset and DataLoader preparation
8. TrOCR experimentation
9. OCR evaluation
10. Streamlit application development
11. Final project documentation

---

## Dataset

The dataset contains Urdu OCR images collected from different sources and categories.

The dataset includes images from categories such as:

- Newspapers
- Books
- Signboards
- Synthetic images
- Other Urdu text images

The images were organized and labelled for OCR experimentation.

---

## Image Preprocessing

Image preprocessing was performed to improve the quality of the OCR input.

The preprocessing workflow included:

- Converting images to grayscale
- Resizing images while maintaining aspect ratio
- Applying Gaussian blur for noise reduction
- Applying adaptive thresholding for binarization
- Saving processed images for further OCR experiments

---

## Tesseract OCR Testing

Tesseract OCR was tested on the processed Urdu images.

The results showed that general-purpose OCR tools can struggle with Urdu text.

Some outputs were empty or contained incorrect characters.

The main difficulties included:

- Connected Urdu characters
- Different Urdu fonts
- Character dots
- Image quality
- Text segmentation
- Urdu-specific writing patterns

This testing helped identify the need for a dedicated Urdu OCR approach.

---

## Gap Analysis

The Tesseract experiments showed that the OCR system did not consistently recognize Urdu text correctly.

Some outputs were empty, while others contained incorrect or incomplete characters.

Urdu is a cursive script in which characters can change depending on their position within a word.

Because of these challenges, a dedicated Urdu OCR model is required for better recognition.

---

## TrOCR Approach

The project also experimented with TrOCR-based Urdu OCR.

TrOCR is a transformer-based OCR approach that can be used to recognize text from images.

The project explored the use of an Urdu TrOCR model for recognizing Urdu text from images.

The final application uses a pretrained Urdu TrOCR model to generate Urdu text predictions.

---

## Evaluation

The pretrained Urdu TrOCR evaluation produced the following results:

- CER: 0.6288
- WER: 1.02
- Derived character-level score: approximately 37.12%

The derived character-level score is calculated as:

(1 - CER) × 100

The 37.12% value should not be interpreted as standard classification accuracy.

---

## Streamlit Application

A Streamlit application was developed to provide a simple interface for the Urdu OCR system.

### How the application works

1. The user uploads an Urdu text image.
2. The application processes the image.
3. The image is passed to the Urdu TrOCR model.
4. The model generates the predicted Urdu text.
5. The predicted text is displayed to the user.

### Live Demo

**Streamlit Application:**

PASTE YOUR STREAMLIT LINK HERE

---

## Demo Video

**Loom Demonstration:**

PASTE YOUR LOOM LINK HERE

---

## Technologies Used

- Python
- PyTorch
- Hugging Face Transformers
- TrOCR
- OpenCV
- Pandas
- Streamlit
- GitHub
- Google Colab

---

## Project Structure

```text
urdu-ocr-codesaviours-si26-MuhammadHassaan/
│
├── data/
├── models/
├── notebooks/
├── raw/
├── results/
│
├── labels.csv
├── requirements.txt
├── streamlit_app.py
├── README.md
│
└── Week notebooks
