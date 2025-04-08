import bridges
from huggingface_hub import InferenceClient
import gradio_client
import io
import globales


previo = "Una fotografía de un plato blanco con "

def genera_platillo_gpu(platillo):

    client = gradio_client.Client(globales.espacio, hf_token=bridges.hug)

    prompt = previo + platillo

    print("Eso es el prompt final:", prompt)

    kwargs = {
            "prompt": prompt,
            "api_name": "/infer"
        }
    

    try:
        result = client.predict(**kwargs
        # prompt=prompt,
        # negative_prompt="",
        # seed=42,
        # randomize_seed=True,
        # width=1024,
        # height=1024,
        # guidance_scale=3.5,
        # num_inference_steps=28,
        # api_name="/infer"
        )
        
        return result[0]

    except Exception as e:
        print("Excepción es: ", e)


def genera_platillo_inference(platillo):

    client = InferenceClient(
            provider= globales.proveedor,
            api_key=bridges.hug
        )

    prompt = previo + platillo

    try: 
        image = client.text_to_image(
        prompt,
        model=globales.inferencia,
        #seed=42, #default varía pero el default es que siempre sea la misma.
        #guidance_scale=7.5,
        #num_inference_steps=50,
        #width=1024, #El default es 1024 x 1024 y quizá 1024*768, el max es 1536. 
        #height=1024 #El límite de replicate es 1024.
        )

        img_io = io.BytesIO()
        image.save(img_io, "PNG")
        img_io.seek(0)

        return img_io         
        
    except Exception as e:
        print("Excepción es: ", e)