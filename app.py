from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse

import io
from io import BytesIO

from fastapi import FastAPI, Form

import funciones

app = FastAPI()

@app.post("/echo-image/")
async def echo_image(image: UploadFile = File(...)):
    if not image.content_type.startswith("image/"):
        return {"error": "El archivo no es una imagen"}

    contents = await image.read()
    return StreamingResponse(BytesIO(contents), media_type=image.content_type)

@app.post("/get-platillo/")
async def get_platillo_image(prompt: str = Form(...)):
    
    imagen_pil = funciones.genera_platillo(prompt)

    img_io = io.BytesIO()
    imagen_pil.save(img_io, "PNG")
    img_io.seek(0)
    
    #Ver cual es el mejor resultado para backend, si forzar la disposición de archivo o permitir que el navegador decida (puede que sea irrelevante para un consumo de la api directo)
    #return StreamingResponse(content=img_io, media_type="image/png", headers={"Content-Disposition": "attachment; filename=platillo.png"})
    return StreamingResponse(content=img_io, media_type="image/png")