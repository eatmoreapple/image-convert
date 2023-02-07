from flask import Flask, render_template, request, Response
from PIL import Image
import io

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/jpgtopng", methods=["GET"])
def jpgtopng():
    return render_template("jpgtopng.html")


@app.route("/pngtojpg", methods=["GET"])
def pngtojpg():
    return render_template("pngtojpg.html")


@app.route("/webptopng", methods=["GET"])
def webptopng():
    return render_template("webptopng.html")


@app.route("/bmptopng", methods=["GET"])
def bmptopng():
    return render_template("bmptopng.html")


@app.route("/pngtopdf", methods=["GET"])
def pngtopdf():
    return render_template("pngtopdf.html")


@app.route("/pngtobmp", methods=["GET"])
def pngtobmp():
    return render_template("pngtobmp.html")


@app.route('/api/jpgtopng', methods=['POST'])
def jpg_to_png():
    image = request.files.get('image')
    if not image:
        return Response("No image found", status=400)
    image_data = Image.open(io.BytesIO(image.read()))
    if image_data.format != 'JPEG':
        return {'error': 'Invalid image format. Only JPEG is allowed.'}
    image_data = image_data.convert('RGB')
    image_buffer = io.BytesIO()
    image_data.save(image_buffer, format='PNG')
    image_buffer.seek(0)
    response = Response(image_buffer, content_type='image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='converted.png')
    return response


@app.route("/api/pngtojpg", methods=["POST"])
def png_to_jpg():
    image = request.files.get('image')
    if not image:
        return {'error': 'No image found.'}
    image_data = Image.open(io.BytesIO(image.read()))
    if image_data.format != 'PNG':
        return {'error': 'Invalid image format. Only PNG is allowed.'}
    image_data = image_data.convert('RGB')
    image_stream = io.BytesIO()
    image_data.save(image_stream, format='JPEG')
    image_stream.seek(0)
    response = Response(image_stream.read(), content_type='image/jpeg')
    response.headers.set('Content-Disposition', 'attachment', filename='converted.jpg')
    return response


@app.route("/api/webptopng", methods=["POST"])
def webp_to_png():
    image = request.files.get('image')
    if not image:
        return {'error': 'No image found.'}
    image = Image.open(io.BytesIO(image.read()))
    pdf_buffer = io.BytesIO()
    image.save(pdf_buffer, 'PNG', resolution=100.0)
    pdf_buffer.seek(0)
    response = Response(pdf_buffer, content_type="application/png")
    response.headers["Content-Disposition"] = "attachment; filename=converted_file.png"
    return response


@app.route("/api/bmptopng", methods=["POST"])
def bmp_to_png():
    image = request.files.get('image')
    if not image:
        return {'error': 'No image found.'}
    image = Image.open(io.BytesIO(image.read()))
    pdf_buffer = io.BytesIO()
    image.save(pdf_buffer, 'PNG', resolution=100.0)
    pdf_buffer.seek(0)
    response = Response(pdf_buffer, content_type="application/png")
    response.headers["Content-Disposition"] = "attachment; filename=converted_file.png"
    return response


@app.route("/api/pngtopdf", methods=["POST"])
def png_to_pdf():
    image = request.files.get('image')
    if not image:
        return {'error': 'No image found.'}
    image = Image.open(io.BytesIO(image.read()))
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    pdf_buffer = io.BytesIO()
    image.save(pdf_buffer, 'PDF', resolution=100.0)
    pdf_buffer.seek(0)
    response = Response(pdf_buffer, content_type="application/pdf")
    response.headers["Content-Disposition"] = "attachment; filename=converted_file.pdf"
    return response


@app.route("/api/pngtobmp", methods=["POST"])
def png_to_bmp():
    image = request.files.get('image')
    if not image:
        return {'error': 'No image found.'}
    image = Image.open(io.BytesIO(image.read()))
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    pdf_buffer = io.BytesIO()
    image.save(pdf_buffer, 'BMP', resolution=100.0)
    pdf_buffer.seek(0)
    response = Response(pdf_buffer, content_type="application/bmp")
    response.headers["Content-Disposition"] = "attachment; filename=converted_file.bmp"
    return response


if __name__ == "__main__":
    app.run(port=5000)
