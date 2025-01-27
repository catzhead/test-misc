from diffusers import DiffusionPipeline
import torch

pipeline = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16,
    use_safetensors=True,
    variant="fp16"
)
pipeline.to("mps")

prompt = "a cat wearing a Sherlock Holmes deerstalker hat, detailed fur, " \
         "portrait style"
negative_prompt = "low quality, blurry, distorted"

image = pipeline(
    prompt=prompt,
    negative_prompt=negative_prompt,
    num_inference_steps=30,
    guidance_scale=7.5
).images[0]

image.save("sherlock_cat.png")
