import streamlit as st
from PIL import Image
import qrcode
from io import BytesIO
import re


def make_qr(
    data: str,
    fill_color: str = "black",
    back_color: str = "white",
    box_size: int = 10,
    border: int = 4,
):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color=fill_color,
        back_color=back_color
    ).convert("RGB")

    return img

def sanitize_filename(name: str) -> str:
    name = re.sub(r'[\\/*?:"<>|]', "_", name).strip()
    return name or "QR_Code"


def is_likely_url(text: str) -> bool:
    text = text.strip()
    if not text:
        return False
    if re.match(r"https?://", text, re.IGNORECASE):
        return True
    if re.match(r"^[\w.-]+\.[a-zA-Z]{2,}(/.*)?$", text):
        return True
    return False


def normalize_url(text: str) -> str:
    text = text.strip()
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", text):
        return text
    return "https://" + text


def main() -> None:
    st.set_page_config(
        page_title="IndianCoder3's QR Code Generator",
        layout="centered",
    )

    st.title("IndianCoder3's QR Code Generator")
    st.write("Enter text or a URL to generate a QR code.")

    data = st.text_area("Text / URL", height=150)

    col1, col2 = st.columns(2)
    with col1:
        box_size = st.slider("Box size", 1, 20, 10)
    with col2:
        border = st.slider("Border", 1, 10, 4)

    col3, col4 = st.columns(2)
    with col3:
        fill_color = st.color_picker("Fill color", "#000000")
    with col4:
        back_color = st.color_picker("Background color", "#ffffff")

    filename_input = st.text_input("Filename (optional, without extension)")

    treat_as_url = False
    if is_likely_url(data):
        treat_as_url = st.checkbox("Treat input as URL", value=True)

    if st.button("Generate QR"):
        if not data.strip():
            st.warning("Please enter some text or a URL.")
            return

        payload = data
        if treat_as_url:
            payload = normalize_url(data)
            st.markdown(f"**Detected URL:** [{payload}]({payload})")

        img = make_qr(
            payload,
            fill_color=fill_color,
            back_color=back_color,
            box_size=box_size,
            border=border,
        )

        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        st.image(buffer, caption="Generated QR Code")

        if filename_input.strip():
            filename = sanitize_filename(filename_input)
        else:
            short = sanitize_filename(data)[:40]
            filename = f"QR_{short}"

        st.download_button(
            label="Download QR Code (PNG)",
            data=buffer.getvalue(),
            file_name=f"{filename}.png",
            mime="image/png",
        )
    else:
        st.info("Waiting for input…")


if __name__ == "__main__":
    main()
