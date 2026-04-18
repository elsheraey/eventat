# Practical Deep Learning, Chapters 9–10: Internal Optomatica Talk

**Slides and companion code from an internal Optomatica session covering Chapters 9 and 10 of *Practical Deep Learning for Cloud, Mobile, and Edge* (Anirudh Koul, Siddha Ganju, Meher Kasam), delivered in March 2020. Covers scalable inference serving and deep learning in the browser, with a live pose-estimation demo served via TensorFlow Serving.**

> **Event:** Internal Optomatica session.
> **Date:** March 2020.
> **My role:** Speaker, as an engineer at [Optomatica](https://www.optomatica.com).
> **Talk title:** "Practical Deep Learning — Chapter 9 & 10".

Part of the [eventAt](../) catalog of hackathons, talks, and technical events.

## What's here

| File | What it is |
|---|---|
| [`presentation.pptx`](./presentation.pptx) | The slide deck used during the talk. |
| [`code/server.ipynb`](./code/server.ipynb) | Notebook that stands up an OpenPose model behind [TensorFlow Serving](https://www.tensorflow.org/tfx/serving/architecture) and exposes it via ngrok. |
| [`code/client.py`](./code/client.py) | Minimal client: POSTs an image to the serving endpoint and draws the returned skeleton with OpenCV. |
| [`code/run.bat`](./code/run.bat) | One-liner that invokes the client against the ngrok URL with the sample image. |
| [`code/1.jpeg`](./code/1.jpeg) | Sample input image for the demo. |
| [`code/Links.txt`](./code/Links.txt) | Reference links shown during the talk. |

## What the talk covered

**Chapter 9 — Scalable Inference Serving**

- VMs vs. containers for serving ML models.
- Scaling inference workloads, and the cost vs. QPS trade-off.
- A live demo: [CMU OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) served through TensorFlow Serving, tunneled with ngrok, and consumed from a Python client.

**Chapter 10 — Deep Learning in the Browser**

- Why run models client-side at all.
- A tour of [TensorFlow.js](https://www.tensorflow.org/js) and [ml5.js](https://ml5js.org/), with a nod to [Zaid Alyafeai's interactive demos](https://zaidalyafeai.github.io/) and Google's [semiconductor.withgoogle.com](https://semiconductor.withgoogle.com/).

## Running the demo

The server notebook is intended for a GPU-backed environment (Colab works). It:

1. Loads an OpenPose-style pose estimation model.
2. Wraps it in a Flask endpoint at `/pose`.
3. Exposes the endpoint publicly via ngrok.

Then, from any machine with the client's dependencies installed:

```bash
pip install requests opencv-python numpy pillow
python client.py -u <ngrok-url>/pose -f 1.jpeg
```

The client draws the returned skeleton on top of the input image and opens it in an OpenCV window.
