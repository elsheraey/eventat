# Seq2Seq: Internal Optomatica Talk

**Slide deck from an internal Optomatica session on sequence-to-sequence (Seq2Seq) models, delivered in March 2020. Walks the team through the motivation, architecture, and experiments behind modern encoder-decoder models.**

> **Event:** Internal Optomatica session.
> **Date:** March 2020.
> **My role:** Speaker, as an engineer at [Optomatica](https://www.optomatica.com).
> **Talk title:** "Seq2Seq".

Part of the [eventAt](../) catalog of hackathons, talks, and technical events.

## What's here

| File | What it is |
|---|---|
| [`presentation.pptx`](./presentation.pptx) | The slide deck used during the talk. |

## What the talk covered

The deck walked the team through:

- Why Seq2Seq matters: machine translation, speech recognition, image captioning, video activity recognition.
- RNN types and the role of GRU / LSTM units.
- Practical tricks: reversed inputs and bidirectional RNNs (BIRNN), with a grounded example of why context from both directions matters ("This is Teddy, he's our AI expert." vs. "This is a Teddy bear, would you like to play with it?").
- Neural Machine Translation with attention, and attention as an interpretability tool.
- Evaluation with BLEU.
- Hands-on experiments: Arabic and Swedish translation, and a reverse-words sanity check.
