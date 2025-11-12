# Anatomy-Wordlist-Dataset
A structured, open-source dataset of anatomy-related medical terms — categorized, decomposed, and connected by prefix–suffix relationships.

---

## 📚 Overview

This project provides a structured wordlist of **anatomy-related medical terms**, decomposed into their **prefix**, **root**, and **suffix** components.  
It is designed for:

- 🧩 **Medical education tools** 
- 🤖 **NLP or ML research** on medical terminology
- 📖 **Linguistic analysis** of biomedical language

---

## 🧬 Example Data

### `data/anatomy_terms.json`

```json
[
  {
    "term": "hepatocyte",
    "prefix": "hepato-",
    "root": "cyte",
    "suffix": null,
    "meaning": "liver cell",
    "category": "Anatomy",
    "related_terms": ["hepatitis", "hepatic", "hepatology"]
  },
  {
    "term": "osteoblast",
    "prefix": "osteo-",
    "root": "blast",
    "suffix": null,
    "meaning": "bone-forming cell",
    "category": "Anatomy",
    "related_terms": ["osteocyte", "osteoclast", "osteology"]
  },
  {
    "term": "dermatology",
    "prefix": "dermato-",
    "root": "logy",
    "suffix": null,
    "meaning": "study of the skin",
    "category": "Anatomy",
    "related_terms": ["dermis", "epidermis", "dermatitis"]
  }
]


## 📚 Data Source & License

This repository contains medical terminology data derived from:

> "Glossary – Fundamentals of Anatomy and Physiology"  
> by University of Southern Queensland  
> https://usq.pressbooks.pub/anatomy/back-matter/glossary/  
> Licensed under **CC BY-SA 4.0**

The dataset (`data/anatomy_terms.*`) is redistributed and extended under the same
**Creative Commons Attribution-ShareAlike 4.0 International License**.

All scripts and utilities in the `/scripts` directory are released under the **MIT License**.  
See `LICENSE` and `DATA_LICENSE` for details.
