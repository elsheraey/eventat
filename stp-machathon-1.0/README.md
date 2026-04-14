# STP Machathon 1.0: Face Recognition Talk

**Slides and live demo from my talk "Face Recognition: Tech. that knows you", delivered at STP Machathon 1.0 in February 2020 as a representative of Optomatica. Covers the basics of face recognition technology and its potential applications.**

> **Event:** STP Machathon 1.0, the first iteration of STP's machine learning event in collaboration with several leading Egyptian companies in the ML field.
> **Date:** February 2020.
> **My role:** Speaker, representing [Optomatica](https://www.optomatica.com).
> **Talk title:** "Face Recognition: Tech. that knows you".

Part of the [eventAt](../) catalog of hackathons, talks, and technical events.

## What's here

| File | What it is |
|---|---|
| [`presentation.pdf`](./presentation.pdf) | The slide deck used during the talk. |
| [`demo.ipynb`](./demo.ipynb) | Jupyter notebook live-demo of a simple face recognition pipeline, run during the talk. |
| [`mourad.jpg`](./mourad.jpg) | Training image used by the demo. |
| [`unknowns.jpg`](./unknowns.jpg) | Test image set used by the demo for inference. |

## What the talk covered

The presentation walked an ML-curious audience through:

- The basic concepts behind modern face recognition (face detection, embeddings, distance metrics).
- What the technology can and can't reliably do at scale.
- A live-coded demo using the `face_recognition` Python library, trained on a single reference image and tested against a small gallery of unknowns.
- Potential applications, and some of the ethical considerations that come with them.

## Running the demo

```bash
pip install face_recognition numpy matplotlib jupyter
jupyter notebook demo.ipynb
```

The demo reads `mourad.jpg` as the known face and classifies each face in `unknowns.jpg` as a match or non-match.
