# Deep Learning for Computer Vision & CNN Architectures: McMaster University

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-FF6F00?style=flat&logo=tensorflow&logoColor=white)](https://tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-D00000?style=flat&logo=keras&logoColor=white)](https://keras.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A curated deep learning suite developed during the **Applied Artificial Intelligence** curriculum at **McMaster University (Ontario, Canada)**. This repository showcases end-to-end convolutional neural network (CNN) architectures applied to autonomous driving perception, foundational CNN theory, and biometric facial expression analysis.

---

## 📌 Repository Overview

This project comprises three major computer vision modules:

```text
McMaster-Computer-Vision-CNN-Suite/
├── README.md                                          # Architectural & experimental documentation
├── Assignment 2.pdf                                   # McMaster University course assignment specification
├── 01_Traffic_Sign_Classification/                    # Autonomous Driving Perception
│   └── Deep_Learning_for_Traffic_Sign_Classification.ipynb # GTSRB multi-class CNN classifier
├── 02_AlexNet_Architecture_Study/                     # Architectural & Generalization Analysis
│   ├── probleme_1.ipynb                              # Empirical study of convolutional feature extraction & regularization
│   └── probleme_1.pdf                                # Formal technical report with curves & mathematical derivations
└── 03_Facial_Smile_Recognition/                       # Biometric Facial Emotion Analysis
    ├── problem_2.ipynb                               # End-to-end CNN smiling classifier on RGB face tensors
    ├── problem_2.pdf                                 # Technical evaluation report with confusion matrix & accuracy
    └── Problem 2/                                    # Dataset tensors
        ├── train_happy.h5                            # 600 training face images (64x64x3)
        └── test_happy.h5                             # 150 test face images (64x64x3)
```

---

## 🚦 Module 1: Autonomous Driving Traffic Sign Recognition (GTSRB)

- **Dataset**: German Traffic Sign Recognition Benchmark (GTSRB) featuring **43 distinct traffic sign classes** under varying illumination, angles, and occlusions.
- **Image Preprocessing Pipeline**:
  1. Grayscale conversion to eliminate chromatic variance and focus on geometric sign topology.
  2. Local Histogram Equalization (`cv2.equalizeHist` / adaptive contrast adjustment) to normalize lighting disparities across daytime and nighttime captures.
  3. Image normalization: $\mathbf{X}_{\text{norm}} = \frac{\mathbf{X} - 128}{128} \in [-1, 1]$.
  4. Real-time data augmentation via affine transformations (random rotation, zooming, spatial shifting).
- **Network Architecture**:
  - Custom deep CNN with alternating $5 \times 5$ convolutions, ReLU activation, spatial Max-Pooling ($2 \times 2$), and Dropout layers ($p=0.4$) to penalize co-adaptation.
  - Fully connected dense layers with Softmax classification over the 43 output classes.
  - Cross-entropy loss minimization via Adam optimizer.

---

## 🧠 Module 2: AlexNet Architecture & Regularization Dynamics

- **Objective**: In-depth theoretical and empirical study of the groundbreaking **AlexNet** architecture ([Krizhevsky et al., 2012](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)).
- **Key Concepts Covered**:
  - Receptive field expansion through cascaded $11 \times 11$, $5 \times 5$, and $3 \times 3$ convolutional kernels.
  - Rectified Linear Units (ReLU) alleviating vanishing gradient problems during deep backpropagation.
  - Overfitting mitigation strategies: Dropout ($0.5$), data augmentation, weight decay ($\ell_2$ regularization), and early stopping.
  - Feature hierarchy: low-level Gabor-like edge filters in early layers transitioning to class-specific semantic detectors in deeper stages.

---

## 😊 Module 3: Facial Expression & Smile Classification

- **Objective**: Binary emotion classification detecting whether a subject is smiling based on $64 \times 64 \times 3$ RGB facial crops.
- **Dataset**: `train_happy.h5` (600 images) and `test_happy.h5` (150 images).
- **Architecture**:
  - `Conv2D` ($32$ filters, $3 \times 3$, `same` padding) $\rightarrow$ `BatchNormalization` $\rightarrow$ `ReLU` $\rightarrow$ `MaxPooling2D` ($2 \times 2$)
  - `Conv2D` ($64$ filters, $3 \times 3$) $\rightarrow$ `BatchNormalization` $\rightarrow$ `ReLU` $\rightarrow$ `MaxPooling2D` ($2 \times 2$)
  - `Flatten` $\rightarrow$ `Dense` ($64$ units, `ReLU`) $\rightarrow$ `Dropout` ($0.5$) $\rightarrow$ `Dense` ($1$ unit, `Sigmoid`).
- **Evaluation**: Binary cross-entropy loss, precision, recall, and ROC-AUC curve analysis.

---

## 🛠️ Quickstart

### Prerequisites
```bash
git clone https://github.com/nourou-dine-cisse/McMaster-Computer-Vision-CNN-Suite.git
cd McMaster-Computer-Vision-CNN-Suite
pip install tensorflow numpy pandas matplotlib seaborn opencv-python h5py jupyter
```

### Running the Notebooks
```bash
jupyter notebook 01_Traffic_Sign_Classification/Deep_Learning_for_Traffic_Sign_Classification.ipynb
jupyter notebook 02_AlexNet_Architecture_Study/probleme_1.ipynb
jupyter notebook 03_Facial_Smile_Recognition/problem_2.ipynb
```

---

## 👤 Author
**Mouhamed Nourou Dine Cisse**  
- **McMaster University** (Hamilton, ON, Canada) — Academic Exchange in Applied AI & Machine Learning  
- **Université Paris-Saclay & ENSIIE** — Master 2 in Artificial Intelligence (M2IA) & Diplôme d'Ingénieur  
- Portfolio: [nourouportfoliowebsite.vercel.app](https://nourouportfoliowebsite.vercel.app)  
- GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)  
- LinkedIn: [mouhamed-nourou-dine-cisse](https://linkedin.com/in/mouhamed-nourou-dine-cisse-094159327)
