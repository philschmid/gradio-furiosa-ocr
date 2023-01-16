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
    print(ocr_lines)

    x = [
        {
            "words": [
                {
                    "data": "Cloud",
                    "location": {
                        "vertices": [
                            {"x": 385.6947937011719, "y": 159.46141052246094},
                            {"x": 531.0, "y": 160.36538696289062},
                            {"x": 531.0, "y": 215.91952514648438},
                            {"x": 385.6947021484375, "y": 213.9243927001953},
                        ]
                    },
                },
                {
                    "data": "Attention",
                    "location": {
                        "vertices": [
                            {"x": 531.0, "y": 160.36538696289062},
                            {"x": 766.1771850585938, "y": 161.39407348632812},
                            {"x": 766.1771850585938, "y": 216.99058532714844},
                            {"x": 531.0, "y": 215.91952514648438},
                        ]
                    },
                },
            ],
            "is_cut": False,
        },
        {
            "words": [
                {
                    "data": "The",
                    "location": {
                        "vertices": [
                            {"x": 388.0808410644531, "y": 217.13206481933594},
                            {"x": 451.0, "y": 217.05905151367188},
                            {"x": 451.0, "y": 252.35037231445312},
                            {"x": 388.0808410644531, "y": 251.5474395751953},
                        ]
                    },
                },
                {
                    "data": "Transformers",
                    "location": {
                        "vertices": [
                            {"x": 451.0, "y": 217.05905151367188},
                            {"x": 640.0, "y": 216.97915649414062},
                            {"x": 640.0, "y": 253.22918701171875},
                            {"x": 451.0, "y": 252.35037231445312},
                        ]
                    },
                },
                {
                    "data": "&",
                    "location": {
                        "vertices": [
                            {"x": 640.0, "y": 216.97915649414062},
                            {"x": 666.0, "y": 216.98016357421875},
                            {"x": 666.0, "y": 253.21826171875},
                            {"x": 640.0, "y": 253.22918701171875},
                        ]
                    },
                },
                {
                    "data": "Cloud",
                    "location": {
                        "vertices": [
                            {"x": 666.0, "y": 216.98016357421875},
                            {"x": 753.0, "y": 216.98703002929688},
                            {"x": 753.0, "y": 253.14259338378906},
                            {"x": 666.0, "y": 253.21826171875},
                        ]
                    },
                },
                {
                    "data": "Newsletter",
                    "location": {
                        "vertices": [
                            {"x": 753.0, "y": 216.98703002929688},
                            {"x": 910.0657958984375, "y": 216.94970703125},
                            {"x": 910.0657958984375, "y": 253.5532684326172},
                            {"x": 753.0, "y": 253.14259338378906},
                        ]
                    },
                },
            ],
            "is_cut": False,
        },
        {
            "words": [
                {
                    "data": "ISSUE",
                    "location": {
                        "vertices": [
                            {"x": 134.49691772460938, "y": 275.4983215332031},
                            {"x": 342.00006103515625, "y": 279.13970947265625},
                            {"x": 342.0, "y": 364.6739501953125},
                            {"x": 134.49693298339844, "y": 361.0396728515625},
                        ]
                    },
                },
                {
                    "data": "#1:",
                    "location": {
                        "vertices": [
                            {"x": 342.00006103515625, "y": 279.13970947265625},
                            {"x": 448.0, "y": 279.21099853515625},
                            {"x": 448.0, "y": 364.741455078125},
                            {"x": 342.0, "y": 364.6739501953125},
                        ]
                    },
                },
                {
                    "data": "How",
                    "location": {
                        "vertices": [
                            {"x": 448.0, "y": 279.21099853515625},
                            {"x": 601.0, "y": 280.2091064453125},
                            {"x": 601.0, "y": 365.74517822265625},
                            {"x": 448.0, "y": 364.741455078125},
                        ]
                    },
                },
                {
                    "data": "far",
                    "location": {
                        "vertices": [
                            {"x": 601.0, "y": 280.2091064453125},
                            {"x": 703.0, "y": 281.8919372558594},
                            {"x": 703.0, "y": 367.4332275390625},
                            {"x": 601.0, "y": 365.74517822265625},
                        ]
                    },
                },
                {
                    "data": "can",
                    "location": {
                        "vertices": [
                            {"x": 703.0, "y": 281.8919372558594},
                            {"x": 817.5032958984375, "y": 284.0867919921875},
                            {"x": 819.8800048828125, "y": 369.63458251953125},
                            {"x": 703.0, "y": 367.4332275390625},
                        ]
                    },
                },
                {
                    "data": "you",
                    "location": {
                        "vertices": [
                            {"x": 817.5032958984375, "y": 284.0867919921875},
                            {"x": 943.4017333984375, "y": 284.6953125},
                            {"x": 948.5821533203125, "y": 370.93035888671875},
                            {"x": 819.8800048828125, "y": 369.63458251953125},
                        ]
                    },
                },
                {
                    "data": "get",
                    "location": {
                        "vertices": [
                            {"x": 943.4017333984375, "y": 284.6953125},
                            {"x": 1063.6422119140625, "y": 280.98114013671875},
                            {"x": 1069.174560546875, "y": 366.2252197265625},
                            {"x": 948.5821533203125, "y": 370.93035888671875},
                        ]
                    },
                },
            ],
            "is_cut": False,
        },
        {
            "words": [
                {
                    "data": "with",
                    "location": {
                        "vertices": [
                            {"x": 156.07260131835938, "y": 349.31524658203125},
                            {"x": 319.9999694824219, "y": 351.7566833496094},
                            {"x": 320.0, "y": 441.1121826171875},
                            {"x": 156.07260131835938, "y": 438.671875},
                        ]
                    },
                },
                {
                    "data": "a",
                    "location": {
                        "vertices": [
                            {"x": 319.9999694824219, "y": 351.7566833496094},
                            {"x": 366.4130859375, "y": 351.54974365234375},
                            {"x": 367.36566162109375, "y": 443.85845947265625},
                            {"x": 320.0, "y": 441.1121826171875},
                        ]
                    },
                },
                {
                    "data": "single",
                    "location": {
                        "vertices": [
                            {"x": 366.4130859375, "y": 351.54974365234375},
                            {"x": 563.6693115234375, "y": 351.00836181640625},
                            {"x": 564.5840454101562, "y": 441.41998291015625},
                            {"x": 367.36566162109375, "y": 443.85845947265625},
                        ]
                    },
                },
                {
                    "data": "GPU",
                    "location": {
                        "vertices": [
                            {"x": 563.6693115234375, "y": 351.00836181640625},
                            {"x": 707.0001220703125, "y": 351.4193115234375},
                            {"x": 707.0, "y": 440.77435302734375},
                            {"x": 564.5840454101562, "y": 441.41998291015625},
                        ]
                    },
                },
                {
                    "data": "in",
                    "location": {
                        "vertices": [
                            {"x": 707.0001220703125, "y": 351.4193115234375},
                            {"x": 779.0, "y": 352.0030212402344},
                            {"x": 779.0, "y": 441.3586120605469},
                            {"x": 707.0, "y": 440.77435302734375},
                        ]
                    },
                },
                {
                    "data": "just",
                    "location": {
                        "vertices": [
                            {"x": 779.0, "y": 352.0030212402344},
                            {"x": 912.9999389648438, "y": 353.2247314453125},
                            {"x": 913.0, "y": 442.5796813964844},
                            {"x": 779.0, "y": 441.3586120605469},
                        ]
                    },
                },
                {
                    "data": "one",
                    "location": {
                        "vertices": [
                            {"x": 912.9999389648438, "y": 353.2247314453125},
                            {"x": 1041.928466796875, "y": 353.29949951171875},
                            {"x": 1041.92822265625, "y": 442.65362548828125},
                            {"x": 913.0, "y": 442.5796813964844},
                        ]
                    },
                },
            ],
            "is_cut": False,
        },
        {
            "words": [
                {
                    "data": "day?",
                    "location": {
                        "vertices": [
                            {"x": 518.030029296875, "y": 425.5204772949219},
                            {"x": 676.0, "y": 425.74786376953125},
                            {"x": 676.0, "y": 515.4774780273438},
                            {"x": 518.030029296875, "y": 515.4981079101562},
                        ]
                    },
                }
            ],
            "is_cut": False,
        },
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
        .gr-button {
            color: white;
            border-color: #9d66e5;
            background: #9d66e5;
        }
        input[type='range'] {
            accent-color: #9d66e5;
        }
        .dark input[type='range'] {
            accent-color: #dfdfdf;
        }
        .container {
            max-width: 730px;
            margin: auto;
            padding-top: 1.5rem;
        }
        #gallery {
            min-height: 22rem;
            margin-bottom: 15px;
            margin-left: auto;
            margin-right: auto;
            border-bottom-right-radius: .5rem !important;
            border-bottom-left-radius: .5rem !important;
        }
        #gallery>div>.h-full {
            min-height: 20rem;
        }
        .details:hover {
            text-decoration: underline;
        }
        .gr-button {
            white-space: nowrap;
        }
        .gr-button:focus {
            border-color: rgb(147 197 253 / var(--tw-border-opacity));
            outline: none;
            box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
            --tw-border-opacity: 1;
            --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
            --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(3px var(--tw-ring-offset-width)) var(--tw-ring-color);
            --tw-ring-color: rgb(191 219 254 / var(--tw-ring-opacity));
            --tw-ring-opacity: .5;
        }
        #advanced-options {
            margin-bottom: 20px;
        }
        .footer {
            margin-bottom: 45px;
            margin-top: 35px;
            text-align: center;
            border-bottom: 1px solid #e5e5e5;
        }
        .footer>p {
            font-size: .8rem;
            display: inline-block;
            padding: 0 10px;
            transform: translateY(10px);
            background: white;
        }
        .dark .logo{ filter: invert(1); }
        .dark .footer {
            border-color: #303030;
        }
        .dark .footer>p {
            background: #0b0f19;
        }
        .acknowledgments h4{
            margin: 1.25em 0 .25em 0;
            font-weight: bold;
            font-size: 115%;
        }
"""

block = gr.Blocks(css=css)

with block:
    gr.HTML(
        """
            <div style="text-align: center; max-width: 650px; margin: 0 auto;">
              <div>
                <img class="logo" src="https://huggingface.co/datasets/philschmid/assets/resolve/main/furiosa_logo.png" alt="Furiosa AI Logo"
                    style="margin: auto; max-width: 7rem;">
                <h1 style="font-weight: 900; font-size: 3rem;">
                  Furiosa AI WARBOY: OCR Demo
                </h1>
              </div>
              <p style="margin-bottom: 10px; font-size: 94%">
              High performance inference chip for the most advanced vision applications, Edge servers to data centers
                <a href="https://www.furiosa.ai/">Learn more</a>.
              </p>
            </div>
        """
    )

    with gr.Row() as text_to_image:
        with gr.Column():
            input_image = gr.Image(label="OCR Image", type="pil", elem_id="img_1")
            furiosa_ocr = gr.Button("Generate Image")
            example1 = gr.Button("Example 1")

        with gr.Column():
            furiosa_result = gr.Textbox(label="FuriosaAI Result", lines=5, elem_id="furiosa_result")
            intel_result = gr.Textbox(label="Intel Result", lines=5, elem_id="furiosa_result")

    furiosa_ocr.click(
        fn=predict_with_warboy,
        inputs=[input_image],
        outputs=furiosa_result,
    )

    gr.HTML(
        """
            <div style="display:flex; margin: 0 auto; width:100%">
              <div style="width:50%;">
                  <p >
                  WARBOY is currently deployed in commercial applications, in public datacenter environments (Kakao Enterprise). Applications include Korea's largest online English education provider ePopSoft's dictionary OCR service. With seamless integration from datacenter hardware to real-time application, FuriosaAI's full-stack solution allows customers to optimize development and operation workstreams and costs, while drastically improving service quality and management experience.
                </p>
              </div>
              <div style="width:50%;">
                <img class="logo" src="https://huggingface.co/datasets/philschmid/assets/resolve/main/furiosa_architecture.png" alt="Furiosa OCR Setup"
                    style="margin: auto; max-width: 7rem;">
              </div>
            </div>
        """
    )
block.launch(debug=True)
