# Anatomy-Wordlist-Dataset
A structured, open-source dataset of anatomy-related medical terms — categorized, decomposed, and connected by prefix–suffix relationships.

---

## 📚 Overview

This project provides a structured wordlist of **anatomy-related medical terms**, decomposed into their **prefix**, **root**, and **suffix** components.  
It is designed for:

- 🧩 **Medical education tools** (e.g., Quizlet/Anki-style learning apps)
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
