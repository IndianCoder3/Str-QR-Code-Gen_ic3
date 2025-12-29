# 🔳 QR Code Generator (Streamlit)

A simple and interactive **QR Code Generator** built with **Python** and **Streamlit**.
Create QR codes from text or URLs, customize colors and size, and download them directly to your device.

Built by **IndianCoder3** 🚀

---

## ✨ Features

* 📝 Generate QR codes from **text or URLs**
* 🔍 Automatic **URL detection & normalization**
* 🎨 Customize:

  * Fill color
  * Background color
  * Box size
  * Border size
* 📥 **Download QR code as PNG**
* 🌐 Works locally and on **Streamlit Cloud**
* 🧼 Clean, simple UI

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **qrcode** (`qrcode[pil]`)
* **Pillow (PIL)**

---

## 📂 Project Structure

```
.
├── app.py
├── requirements.txt
└── README.md
```

---

## ▶️ Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/IndianCoder3/Str-QR-Code-Gen_ic3.git
cd qr-streamlit-app
```

### 2️⃣ Create & activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
# venv\Scripts\activate    # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app

```bash
streamlit run app.py
```

Open your browser at:

```
http://localhost:8501
```

---

## ☁️ Deploy on Streamlit Cloud

1. Push this repo to **GitHub**
2. Go to 👉 [https://share.streamlit.io](https://share.streamlit.io)
3. Click **New app**
4. Select:

   * Repository: `IndianCoder3/qr-streamlit-app`
   * Branch: `main`
   * File: `app.py`
5. Click **Deploy**

---

## ⚠️ Notes

* File downloads use Streamlit’s `download_button`
* No files are saved on the server (cloud-safe)
* Tested with **Python 3.11+**

---

## 👤 Author

**IndianCoder3**

* 🌐 Portfolio: [https://indiancoder3.netlify.app](https://indiancoder3.netlify.app)
* 🐙 GitHub: [https://github.com/IndianCoder3](https://github.com/IndianCoder3)
* 🐱 Scratch: [https://scratch.mit.edu/users/IndianCoder3/](https://scratch.mit.edu/users/IndianCoder3/)

---

## 📜 License

This project is open-source and free to use for learning and personal projects.