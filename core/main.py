import os
from pathlib import Path

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
    font_thickness: int


class Image(BaseModel):
    data: str
    params: Params


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/process")
async def process(image: Image):
    downloads_path = os.path.join(Path.home(), "Downloads")
    output_path = os.path.join(downloads_path, "output.png")

    process_image(image.data, output_path, image.params.posterize_levels, image.params.num_clusters,
                  image.params.blur_ksize, image.params.min_area_threshold,
                  image.params.font_scale, image.params.font_thickness)
