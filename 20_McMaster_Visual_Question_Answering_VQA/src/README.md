# Visual Question Answering (VQA) Project
---

## 📘 Project Overview
Visual Question Answering (VQA) is a multimodal AI task that combines **computer vision** and **natural language processing** to answer natural‑language questions about images. Given an image and a question, the system must produce a correct answer such as:

- “What color is the traffic light?”
- “How many people are sitting?”
- “Is the dog jumping?”

This requires the model to jointly understand **visual content**, **linguistic structure**, and **semantic relationships** between them. VQA has applications in accessibility tools, intelligent assistants, robotics, and automated image analysis.

---

## 🧠 Methodology

### 1. Dataset
The project uses a standard VQA dataset.

Each sample contains:
- An image  
- A natural‑language question  
- A ground‑truth answer  

---

## 🖼️ 2. Image Encoder

Two image encoders are implemented:

### **a) Pretrained ResNet‑50 Encoder**
- Loaded with **ImageNet** weights  
- Final classification layer removed  
- Outputs a **2048‑dimensional feature vector**  
- Used as a strong, frozen feature extractor  

### **b) Custom CNN Encoder (Baseline)**
- Three convolutional blocks with BatchNorm, ReLU, and MaxPool  
- Global Average Pooling  
- Linear projection to a **512‑dimensional vector**  
- Trained from scratch on the VQA dataset  
---

## ✍️ 3. Question Encoder
Questions are converted into numerical embeddings using:

- Tokenization  
- **Word embeddings** (e.g., GloVe)  
- An **LSTM encoder** to capture sequential context  
---

## 🔗 4. Multimodal Fusion
The image and question embeddings are combined using simple but effective fusion strategies such as:

- Concatenation  
- Element‑wise multiplication  
- Linear projection layers  

The fused representation is passed to a classifier.

---

## 🧩 5. Answer Prediction
The model predicts an answer from a restricted vocabulary (yes and no answers).  
A fully connected classifier outputs a probability distribution over possible answers.

---

## 📊 6. Evaluation
Performance is measured using:

- Accuracy  
- Precision  
- Recall  
- F1‑score  

These metrics evaluate how well the system answers the questions.
