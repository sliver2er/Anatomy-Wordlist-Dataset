# Anatomy-Wordlist-Dataset
A structured, open-source dataset of anatomy-related and affix-based medical terms — categorized, decomposed, and connected by prefix–suffix relationships.

---

## 📚 Overview

This project provides a structured wordlist of **medical terminology**, decomposed into their **prefix**, **root**, and **suffix** components.  
It includes two major datasets:

1. 🧠 **Anatomy Glossary Dataset** — general medical and anatomy-related terms  
2. 🔤 **Medical Affixes Dataset** — medical prefixes and suffixes extracted from Wikipedia  

These datasets are designed for:

- 🧩 **Medical education tools**  
- 🤖 **NLP or ML research** on biomedical terminology  
- 📖 **Linguistic analysis** of medical word formation  

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
  }
]
