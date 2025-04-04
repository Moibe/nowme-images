from fastapi import FastAPI, Form
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse, FileResponse
from io import BytesIO
import funciones, globales

app = FastAPI()

@app.post("/echo-image/")
async def echo_image(image: UploadFile = File(...)):
    if not image.content_type.startswith("image/"):
        return {"error": "El archivo no es una imagen"}

    contents = await image.read()
    return StreamingResponse(BytesIO(contents), media_type=image.content_type)

@app.post("/genera-imagen/")
async def genera_imagen(platillo: str = Form(...)):

    if globales.seconds_available > 25:
        print("GPU...")
        resultado = funciones.genera_platillo_gpu(platillo)
        return FileResponse(resultado, media_type="image/png", filename="imagen.png")
    else: 
        print("Inference...")
        resultado = funciones.genera_platillo_inference(platillo)
        return StreamingResponse(content=resultado, media_type="image/png")
