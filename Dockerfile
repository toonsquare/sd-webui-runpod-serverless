FROM runpod/stable-diffusion:web-automatic-base-4.0.0

SHELL ["/bin/bash", "-c"]

ENV PATH="${PATH}:/workspace/stable-diffusion-webui/venv/bin"

WORKDIR /workspace/stable-diffusion-webui/models/Stable-diffusion
RUN wget https://huggingface.co/toonsquare/test/resolve/main/test.ckpt --content-disposition

WORKDIR /workspace/stable-diffusion-webui/extensions
RUN git clone https://github.com/Mikubill/sd-webui-controlnet.git

WORKDIR /workspace/stable-diffusion-webui
CMD ["python", "extensions/sd-webui-controlnet/install.py"]

WORKDIR /workspace/stable-diffusion-webui/extensions/sd-webui-controlnet/models
RUN wget https://huggingface.co/lllyasviel/ControlNet/resolve/main/models/control_sd15_depth.pth --content-disposition

WORKDIR /
RUN pip install -U xformers
RUN pip install runpod

ADD handler.py .
ADD start.sh /start.sh
RUN chmod +x /start.sh

CMD [ "/start.sh" ]
