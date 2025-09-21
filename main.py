from flask import Flask, send_file
from io import BytesIO
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow import keras
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Force CPU
tf.config.set_visible_devices([], "GPU")

# Load model
generator = keras.layers.TFSMLayer("DCGEN_saved_model", call_endpoint="serving_default")
latent_dim = 300

def tensor_to_image(tensor):
    """Convert model output tensor to PNG bytes"""
    # Get the image array
    img_array = tensor["conv2d"][0].numpy()  # shape: (64, 64, 3)
    # Rescale [-1,1] or [0,1] -> [0,255] depending on your preprocessing
    img_array = (img_array * 255).astype(np.uint8)
    # Convert to PIL Image
    img = Image.fromarray(img_array)
    # Save to BytesIO
    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf

@app.route("/generate")
def generate_single():
    noise = tf.random.normal([1, latent_dim])
    output = generator(noise)
    buf = tensor_to_image(output)
    return send_file(buf, mimetype="image/png")

@app.route("/generate_grid/<int:n>")
def generate_grid(n):
    imgs = []
    for _ in range(n):
        noise = tf.random.normal([1, latent_dim])
        output = generator(noise)
        imgs.append(Image.open(tensor_to_image(output)))

    # Make grid
    cols = min(4, n)
    rows = (n + cols - 1) // cols
    w, h = imgs[0].size
    grid_img = Image.new("RGB", (cols*w, rows*h))
    for idx, img in enumerate(imgs):
        x = (idx % cols) * w
        y = (idx // cols) * h
        grid_img.paste(img, (x, y))

    buf = BytesIO()
    grid_img.save(buf, format="PNG")
    buf.seek(0)
    return send_file(buf, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
