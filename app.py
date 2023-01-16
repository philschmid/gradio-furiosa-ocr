import gradio as gr
import requests as r
from PIL import Image
from io import BytesIO

WARBOY_API_URL = "https://serving.furiosa.in/ocr/v1/image:annotate"
IMAGE_FORMAT = "JPEG"


def convert_image_to_binary(image: Image):
    buf = BytesIO()
    image.save(buf, format=IMAGE_FORMAT)
    return buf.getvalue()


def predict_with_warboy(image):
    binary_image = convert_image_to_binary(image)
    files = {"image": binary_image}

    response = r.post(WARBOY_API_URL, files=files)
    json_response = response.json()

    ocr_lines = [
        line
        for block in json_response["annotation"]["blocks"]
        for paragraph in block["paragraphs"]
        for line in paragraph["lines"]
    ]
    res = []
    for lines in ocr_lines:
        temp_line = []
        for words in lines["words"]:
            temp_line.append(words["data"])
        res.append(" ".join(temp_line))

    return res


css = """
        a {
            color: inherit;
            text-decoration: underline;
        }
        .gradio-container {
            font-family: 'IBM Plex Sans', sans-serif;
        }
        .container {
            max-width: 730px;
            margin: auto;
            padding-top: 1.5rem;
        }
        .gr-box{
            display:flex;
            gap: 1rem;
            flex-direction: column;
        }
"""

examples = ["examples/example_1.png", "examples/example_2.png", "examples/example_3.png"]

block = gr.Blocks(css=css)

with block:
    gr.HTML(
        """
            <div style="text-align: center; max-width: 850px; margin: 0 auto;">
              <div>
                <img class="logo" src="https://huggingface.co/datasets/philschmid/assets/resolve/main/furiosa_logo.png" alt="Furiosa AI Logo"
                    style="margin: auto; max-width: 14rem;">
                <h1 style="font-weight: 900; font-size: 2rem;">
                  Furiosa AI <span style="color:#620102;">WARBOY</span>: OCR Demo
                </h1>
              </div>
              <p style="margin-bottom: 10px">
              High performance inference chip for the most advanced vision applications, Edge servers to data centers.
              </p>
               <a href="https://www.furiosa.ai/">Learn more</a>
            </div>
        """
    )

    with gr.Box():
        input_image = gr.Image(label="OCR Image", type="pil", elem_id="img_1")
        gr.Examples(examples=examples, inputs=[input_image])
        furiosa_ocr = gr.Button("Extract Text").style(margin=True, full_width=True)
        furiosa_result = gr.Textbox(label="FuriosaAI Result", lines=2, elem_id="furiosa_result")
        # intel_result = gr.Textbox(label="Intel Result", lines=5, elem_id="furiosa_result")

    furiosa_ocr.click(
        fn=predict_with_warboy,
        inputs=[input_image],
        outputs=furiosa_result,
    )

    gr.HTML(
        """
            <div style="margin: 0 auto">
            <h2 style="font-weight: 900; font-size: 2rem;">What is WARBOY?</h2>
                <p>
                  WARBOY is currently deployed in commercial applications, in public datacenter environments (Kakao Enterprise). Applications include Korea's largest online English education provider ePopSoft's dictionary OCR service. With seamless integration from datacenter hardware to real-time application, FuriosaAI's full-stack solution allows customers to optimize development and operation workstreams and costs, while drastically improving service quality and management experience.
                </p>
              <div>
                <img class="logo" src="https://huggingface.co/datasets/philschmid/assets/resolve/main/furiosa_architecture.png" alt="Furiosa OCR Setup"
                    style="margin: auto; max-width:32rem;">
              </div>
            </div>
        """
    )
block.launch(debug=True)
