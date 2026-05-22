from diffusers import StableDiffusionPipeline
import torch
import matplotlib.pyplot as plt

prompt = input("Enter your prompt: ")

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16).to("cuda")

with torch.autocast("cuda"):
    image = pipe(prompt).images[0]

image.save("result_image/generated_image.png")

plt.imshow(image)
plt.axis("off")
plt.title("Generated Image")
plt.show()