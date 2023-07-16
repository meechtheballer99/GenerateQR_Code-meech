import qrcode

def generate_qr_code(url, filename):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)

# Example usage
web_link = "https://drive.google.com/drive/folders/1PzjRiPSM1AnqI5Q8ZQG2BTUvQ3ka7oUr?usp=sharing"
output_filename = "qr_code.png"

generate_qr_code(web_link, output_filename)
print("QR code generated successfully.")

