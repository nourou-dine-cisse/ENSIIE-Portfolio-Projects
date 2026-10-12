import torch

from diffusers import Flux2KleinPipeline
from PIL import Image


pipe = Flux2KleinPipeline.from_pretrained(
    "black-forest-labs/FLUX.2-klein-4B",
    dtype=torch.float32,
)

pipe.enable_model_cpu_offload()


image = Image.open(
    "images/person.jpeg"
).convert("RGB")


prompt = """
Add realistic eyeglasses to the person's face.
Preserve the person's identity, facial features, skin, hair,
clothing, background, lighting, and composition.
Only add the eyeglasses.
"""


result = pipe(
    prompt=prompt,
    image=image,
    num_inference_steps=20,
    guidance_scale=4.0,
).images[0]


result.save("images/person_glasses.jpg")