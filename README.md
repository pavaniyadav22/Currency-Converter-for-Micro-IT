
# 💱 Currency Converter (Python)

A **real-time currency converter** built using Python. This application allows users to convert an amount from one currency to another using up-to-date exchange rates fetched from an open API.

---

## 👨‍💻 Developed By

**Guggulla Pavani**  
📧 guggullapavani@gmail.com

---

## 📌 Project Overview

The Currency Converter helps users convert values from one currency to another using real-time exchange rates. It is built as a command-line interface (CLI) application and is perfect for students, developers, or anyone needing a simple yet effective currency conversion tool.

---

## 🚀 Features

- ✅ Real-time exchange rates
- 🌐 Supports over 160+ currencies
- 🧑‍💻 User-friendly command-line interface
- 🔧 Simple and lightweight
- 📡 Uses the free [Exchangerate.host API](https://exchangerate.host)

---

## 🧱 Project Structure

```
currency_converter/
├── converter.py         # Main CLI program
├── utils.py             # Conversion logic and API calls
├── requirements.txt     # Required Python packages
└── README.md            # Project documentation
```

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/currency_converter.git
cd currency_converter
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

- Python 3.6 or higher
- Internet connection (for fetching exchange rates)
- `requests` library (installed via requirements.txt)

---

## 🧪 How to Use

### Run the converter:
```bash
python converter.py
```

### Example:
```
💱 Currency Converter - Real-time
Enter base currency (e.g. USD): USD
Enter target currency (e.g. INR): INR
Enter amount in USD: 50
✅ 50.00 USD = 4162.35 INR
```

---

## 🌍 API Used

This project uses the free and open [Exchangerate.host API](https://exchangerate.host) for live exchange rate data.

- Endpoint: `https://api.exchangerate.host/convert`
- No API key or registration required

---

## 🔒 Limitations

- Requires internet access
- No historical exchange rate support (real-time only)
- Command-line only (GUI not included, but can be added)

---

## 🛠 Future Improvements

- [ ] Add graphical user interface (GUI) using Tkinter or Streamlit
- [ ] Offline mode with locally cached rates
- [ ] Add currency list and search options
- [ ] Export conversion history to a file

---

## 🙏 Acknowledgements

- [Exchangerate.host API](https://exchangerate.host) – For real-time exchange rates
- Python `requests` module – For HTTP requests

---

> 💡 Tip: You can integrate this converter into a web app, mobile app, or finance dashboard with minor modifications.
