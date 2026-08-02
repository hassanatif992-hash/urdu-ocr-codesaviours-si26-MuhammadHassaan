import html
import numpy as np
import streamlit as st
import torch

from PIL import Image, ImageOps
from transformers import (
    TrOCRProcessor,
    VisionEncoderDecoderModel
)


# --------------------------------------------------
# Page settings
# --------------------------------------------------

st.set_page_config(
    page_title="Urdu OCR — Code Saviours SI-26",
    page_icon="📖",
    layout="centered"
)


MODEL_NAME = "mohammadalihumayun/trocr-ur-v2"

device = torch.device("cpu")


# --------------------------------------------------
# Load model only once
# --------------------------------------------------

@st.cache_resource(
    show_spinner="Loading the Urdu OCR model..."
)
def load_urdu_ocr_model():

    processor = TrOCRProcessor.from_pretrained(
        MODEL_NAME
    )

    model = VisionEncoderDecoderModel.from_pretrained(
        MODEL_NAME
    )

    model.to(device)
    model.eval()

    return processor, model


processor, model = load_urdu_ocr_model()


# --------------------------------------------------
# Image preprocessing
# --------------------------------------------------

def prepare_urdu_image(image):

    gray_image = ImageOps.grayscale(
        image.convert("RGB")
    )

    image_array = np.array(gray_image)

    # Convert white text on a dark background
    # into black text on a white background
    if image_array.mean() < 127:

        gray_image = ImageOps.invert(
            gray_image
        )

    # Improve contrast
    gray_image = ImageOps.autocontrast(
        gray_image,
        cutoff=1
    )

    image_array = np.array(gray_image)

    # Remove unnecessary blank space
    text_pixels = image_array < 245

    if text_pixels.any():

        rows, columns = np.where(
            text_pixels
        )

        gray_image = gray_image.crop(
            (
                columns.min(),
                rows.min(),
                columns.max() + 1,
                rows.max() + 1
            )
        )

    # Add white margin
    gray_image = ImageOps.expand(
        gray_image,
        border=20,
        fill=255
    )

    return gray_image.convert("RGB")


# --------------------------------------------------
# Urdu OCR prediction
# --------------------------------------------------

def extract_urdu_text(image):

    processed_image = prepare_urdu_image(
        image
    )

    pixel_values = processor(
        images=processed_image,
        return_tensors="pt"
    ).pixel_values.to(device)

    with torch.inference_mode():

        generated_ids = model.generate(
            pixel_values,
            max_new_tokens=100,
            num_beams=4,
            do_sample=False,
            early_stopping=True
        )

    predicted_text = processor.batch_decode(
        generated_ids,
        skip_special_tokens=True
    )[0].strip()

    return predicted_text, processed_image


# --------------------------------------------------
# Application interface
# --------------------------------------------------

st.title("Urdu OCR — Code Saviours SI-26")

st.write(
    "Upload a clear, cropped, single-line Urdu image. "
    "The application will extract the Urdu text."
)

st.info(
    "Best results are obtained with clear, straight and "
    "closely cropped single-line Urdu images."
)

uploaded_file = st.file_uploader(
    "Upload an Urdu text image",
    type=["png", "jpg", "jpeg", "webp"]
)

if uploaded_file is not None:

    uploaded_image = Image.open(
        uploaded_file
    ).convert("RGB")

    st.subheader("Uploaded Image")

    st.image(
        uploaded_image,
        use_container_width=True
    )

    if st.button(
        "Extract Urdu Text",
        type="primary",
        use_container_width=True
    ):

        try:

            with st.spinner(
                "Reading the Urdu text..."
            ):

                predicted_text, processed_image = (
                    extract_urdu_text(
                        uploaded_image
                    )
                )

            if predicted_text:

                st.subheader("Extracted Urdu Text")

                safe_text = html.escape(
                    predicted_text
                )

                st.markdown(
                    f"""
                    <div dir="rtl"
                         style="
                         text-align:right;
                         font-size:24px;
                         padding:18px;
                         border:1px solid #cccccc;
                         border-radius:8px;
                         background-color:#f7f7f7;
                         color:#111111;
                         line-height:1.8;">
                        {safe_text}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                with st.expander(
                    "View processed image"
                ):

                    st.image(
                        processed_image,
                        use_container_width=True
                    )

            else:

                st.warning(
                    "No Urdu text was detected."
                )

        except Exception as error:

            st.error(
                "The image could not be processed."
            )

            st.code(str(error))


st.divider()

st.caption(
    "Code Saviours ML/AI Internship — Batch SI-26 | "
    "Muhammad Hassaan"
)
