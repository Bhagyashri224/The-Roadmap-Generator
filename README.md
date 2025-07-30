https://drive.google.com/drive/folders/1lO02NMU30bc4C5BFqVBaIrUp4MyZKpAd

# Roadmapper: Your Personalized Learning Path

This is a Streamlit web application that uses the LLaMA 2 model (via `ctransformers`) to generate personalized learning roadmaps for any skill.

## How It Works

1. User enters a skill they want to learn.
2. The app uses a local LLaMA 2 `.gguf` model to generate a step-by-step roadmap with recommended resources.
3. The result is displayed on the web page.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/roadmapper.git
cd roadmapper
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Download LLaMA 2 Model
- Visit: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF
- Download the file: `llama-2-7b-chat.Q3_K_M.gguf`
- Place it in the `model/` folder

### 4. Run the App
```bash
streamlit run app.py
```

---

## Folder Structure

```
roadmapper/
├── app.py
├── requirements.txt
├── README.md
├── utils/
│   └── model_loader.py
└── model/
    └── llama-2-7b-chat.Q3_K_M.gguf  # (You download & place this here)
```

## Notes

- Requires Python 3.8+.
- Ensure your machine has enough RAM to load the 7B model.
