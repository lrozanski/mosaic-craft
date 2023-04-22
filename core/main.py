from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from image import process_image

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Params(BaseModel):
    posterize_levels: int
    num_clusters: int
    blur_ksize: int
    min_area_threshold: int
    font_scale: float
    font_thickness: float


class Image(BaseModel):
    data: str
    params: Params


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/process")
async def say_hello(image: Image):
    output_path = "."

    (output_path, posterize_levels, num_clusters, blur_ksize, min_area_threshold,
     font_scale, font_thickness) = image.params

    process_image(image.data, output_path, posterize_levels, num_clusters, blur_ksize, min_area_threshold,
                  font_scale, font_thickness)
