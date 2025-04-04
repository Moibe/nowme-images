import bridges
from huggingface_hub import InferenceClient
from PIL import Image

def genera_platillo(prompt): 
    enlace = "black-forest-labs/FLUX.1-dev"
    proveedor =  "hf-inference"

    client = InferenceClient(
            provider= proveedor,
            api_key=bridges.hug
        ) 
    
    #Testing change,

    try: 
        image = client.text_to_image(
        prompt,
        model=enlace,
        #seed=42, #default varía pero el default es que siempre sea la misma.
        #guidance_scale=7.5,
        #num_inference_steps=50,
        #width=1024, #El default es 1024 x 1024 y quizá 1024*768, el max es 1536. 
        #height=1024 #El límite de replicate es 1024.
        )

        return image        
        
    except Exception as e:
        print("Excepción es: ", e)