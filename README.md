# Food AI

Get all pathologies and allergies from the ingredients of a given product


## Setup

## Install dependencies
`$ pip install -r requirements.txt`

## Set environment variables

- FLASK_APP=main.py
- FLASK_ENV=developmentPYTHONUNBUFFERED=1;FLASK_APP=main.py;FLASK_ENV=development
- GOOGLE_APPLICATION_CREDENTIALS=/path/file-credentials.json (check how to obtain credentials below)

## Get credentials
Quickstart: Using client libraries (https://cloud.google.com/vision/docs/quickstart-client-libraries)

## Execute Flask
`$ flask run`

## How to use:
Send a file in a POST request to domain-or-ip/upload_product_images endpoint

### curl example
curl --location --request POST 'localhost:5000/upload_product_images' \
--form 'images=@/home/user/Downloads/photo.jpg'
