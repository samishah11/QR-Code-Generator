import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image
import base64

def generate_qr(data):
    qr = qrcode.QRCode(
        version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10, border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img

def pil_to_bytes(img):
    """Convert PIL Image to bytes"""
    img_bytes_io = BytesIO()
    img.save(img_bytes_io, format="PNG")
    return img_bytes_io.getvalue()

def main():
    st.title("QR Code Generator WebApp")

    st.subheader("Made by [Shahbaz Mehmood]")
    
    option = st.radio("Select what to convert into QR Code:", ("Text", "Website URL", "Upload Image"))
    
    if option == "Text":
        text = st.text_area("Enter text to generate QR Code:")
        if st.button("Generate QR Code"):
            if text:
                img = generate_qr(text)
                img_bytes = pil_to_bytes(img)
                st.image(img_bytes, caption="Generated QR Code", use_container_width=True)
                st.download_button("Download QR Code", img_bytes, file_name="qrcode.png", mime="image/png")
            else:
                st.warning("Please enter some text!")
    
    elif option == "Website URL":
        url = st.text_input("Enter website URL:")
        if st.button("Generate QR Code"):
            if url:
                img = generate_qr(url)
                img_bytes = pil_to_bytes(img)
                st.image(img_bytes, caption="Generated QR Code", use_container_width=True)
                st.download_button("Download QR Code", img_bytes, file_name="qrcode.png", mime="image/png")
            else:
                st.warning("Please enter a URL!")
    
    elif option == "Upload Image":
        uploaded_file = st.file_uploader("Upload an image to convert into QR Code", type=["jpg", "png", "jpeg"])
        if uploaded_file is not None:
            img_data = uploaded_file.read()
            encoded_img = base64.b64encode(img_data).decode('utf-8')
            img_qr = generate_qr(encoded_img)
            img_qr_bytes = pil_to_bytes(img_qr)
            st.image(img_qr_bytes, caption="Generated QR Code", use_container_width=True)
            st.download_button("Download QR Code", img_qr_bytes, file_name="qrcode.png", mime="image/png")
    
if __name__ == "__main__":
    main()
