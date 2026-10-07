Here's a professional README.md for your GitHub repository.

# 🐬 Bioacoustic Classification of Striped Dolphin Vocalizations Using Deep Learning Models

## 📌 Project Overview

This project focuses on the automatic classification of striped dolphin vocalizations using Deep Learning techniques. The system processes underwater acoustic recordings, converts them into Mel Spectrogram images, and classifies them into different vocalization categories such as **Whistles**, **Clicks**, and **Noise** using a **ResNet-34 Convolutional Neural Network**.

The project aims to assist marine researchers in analyzing dolphin communication efficiently while reducing manual effort and improving classification accuracy.

---

## 🎯 Objectives

- Automate the classification of striped dolphin vocalizations.
- Reduce manual analysis of underwater acoustic recordings.
- Improve classification accuracy using Deep Learning.
- Support marine biodiversity monitoring and conservation research.

---

## 🛠️ Technologies Used

- Python 3.x
- PyTorch
- Torchvision
- Librosa
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- OpenCV

---

## 📂 Project Structure

```
Bioacoustic-Classification-of-Striped-Dolphin-Vocalizations/
│
├── dataset/
│   ├── whistle/
│   ├── click/
│   └── noise/
│
├── models/
│   └── resnet34_model.pth
│
├── preprocessing.py
├── spectrogram.py
├── dataset.py
├── train.py
├── predict.py
├── evaluate.py
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Methodology

1. Collect dolphin vocalization audio recordings.
2. Perform audio preprocessing.
3. Apply noise reduction and normalization.
4. Generate Mel Spectrograms using STFT.
5. Resize spectrograms for ResNet-34.
6. Train the deep learning model.
7. Evaluate using standard performance metrics.
8. Predict new dolphin vocalizations.

---

## 🧠 Deep Learning Model

The project uses **ResNet-34**, a Residual Convolutional Neural Network.

Why ResNet-34?

- Deep architecture with residual learning
- Better feature extraction
- Reduced vanishing gradient problem
- High classification accuracy
- Efficient transfer learning

---

## 📊 Evaluation Metrics

The model performance is evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 📈 Workflow

```
Audio (.wav)
      │
      ▼
Audio Preprocessing
      │
      ▼
Mel Spectrogram Generation
      │
      ▼
Image Resizing
      │
      ▼
ResNet-34
      │
      ▼
Prediction
      │
      ▼
Whistle / Click / Noise
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Bioacoustic-Classification-of-Striped-Dolphin-Vocalizations.git

cd Bioacoustic-Classification-of-Striped-Dolphin-Vocalizations
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Training

Run:

```bash
python train.py
```

---

## 🔍 Prediction

```bash
python predict.py
```

---

## 🌐 Run Web Application

```bash
streamlit run app.py
```

---

## 📊 Sample Output

Input:

```
111995(1)_segment_3_segment_2.wav
```

Output:

```
Prediction : Whistle

Confidence : 96.48%
```

---

## 📌 Features

- Automatic Dolphin Vocalization Classification
- Audio Noise Reduction
- Mel Spectrogram Generation
- Deep Learning using ResNet-34
- Real-Time Prediction
- User-Friendly Interface
- High Classification Accuracy

---

## 📚 References

1. Hatch et al., *Conservation Biology*, 2012.
2. Tyack & Miller, *Journal of the Acoustical Society of America*, 2015.
3. Gillespie et al., *Journal of the Acoustical Society of America*, 2010.
4. Roch et al., *Journal of the Acoustical Society of America*, 2018.
5. He et al., *Deep Residual Learning for Image Recognition*, CVPR, 2016.

---

## 👨‍💻 Authors

- Haribabu S
- Gurubaran D
- Abhinav Bharathi D

Department of Computer Science and Engineering

Final Year Project

---

## 📜 License

This project is developed for academic and educational purposes. Feel free to use it for learning and research.

---

⭐ If you find this project useful, consider giving it a star on GitHub!

This README is suitable for a final-year project repository and includes the standard sections expected on GitHub.
