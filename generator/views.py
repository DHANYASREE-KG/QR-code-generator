import qrcode
from django.shortcuts import render
from io import BytesIO
import base64

def generate_qr(request):
    qr_image_base64 = None

    if request.method == "POST":
        data = request.POST.get("data")

        # Create QR Code with settings
        qr = qrcode.QRCode(
            version=1,  # controls size, 1 = 21x21
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction
            box_size=10,  # size of each box in pixels
            border=4,  # thickness of border
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Save image to memory
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # Encode to base64 for display
        qr_image_base64 = base64.b64encode(buffer.getvalue()).decode()

    return render(request, "generator/index.html", {"qr_image": qr_image_base64})