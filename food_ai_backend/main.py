import os
from flask import Flask, request, jsonify
from google.cloud import vision

client = vision.ImageAnnotatorClient()
api = Flask(__name__)


def detect_text(file):
    """Detects text in the file."""

    content = file.read()
    image = vision.types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return [text.description for text in texts]


@api.route("/upload_product_images", methods=["POST"])
def post_file():
    """Upload a file."""

    res = []
    for image in request.files.getlist('images'):
        res.append(detect_text(image))

    # Return the texts found on all uploaded images
    return jsonify({'response': res}), 200
