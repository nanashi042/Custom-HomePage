from flask import Flask, render_template
import random
import os

app = Flask(__name__)

# Define the directory path for your images
IMAGE_DIR = "D:/Code/Web_Dev/Chrome_Home_Page/static/img/"

# Function to get a random image from the directory
def get_random_image():
    image_files = [f for f in os.listdir(IMAGE_DIR) if f.endswith(('.jpg', '.png', '.jpeg'))]
    if image_files:
        return random.choice(image_files)
    else:
        return None

@app.route('/')
def index():
    # Get a random image from the directory
    random_img = get_random_image()

    # Pass the image filename to the template
    return render_template('index.html', img=random_img)

if __name__ == '__main__':
    app.run(debug=True)
