# urdu-ocr-codesaviours-si26-MuhammadHassaan

## What is OCR?

OCR stands for Optical Character Recognition. It is a technology that converts text from images into machine-readable text. OCR is used to read scanned documents, printed pages, books, and images so that the text can be edited, searched, or stored digitally.

## Why is Urdu OCR harder than English OCR?

Urdu OCR is harder than English OCR because Urdu is written in a cursive style where letters are connected with each other. The shape of Urdu letters changes depending on their position in a word. Urdu also has dots, complex ligatures, and different writing styles, which make recognition more difficult for OCR models.

## Real-world uses of Urdu OCR

Urdu OCR can be used to digitize old Urdu books, newspapers, and historical records. It can help offices, schools, and libraries convert scanned Urdu documents into editable text. It can also be useful for reading Urdu forms, signboards, and printed documents automatically.
# Week 2 Progress

## Image Preprocessing

- Converted images to grayscale.
- Resized images while maintaining aspect ratio.
- Applied Gaussian Blur for noise reduction.
- Applied Adaptive Thresholding for binarization.
- Saved processed images into data/processed.

## Tesseract OCR Testing

Tesseract OCR was tested on preprocessed Urdu images.

## Gap Analysis

Tesseract produced weak results on Urdu text. Some outputs were empty, some characters were incorrect, and connected Urdu letters were difficult to recognize.

Urdu is cursive, letters connect with each other, and many letters differ only by dots. Because of this, Tesseract is not fully reliable for Urdu OCR.

A dedicated Urdu OCR model is required for better accuracy.
