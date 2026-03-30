# 🔎 AI Autocomplete Engine

A fast autocomplete system built using Trie (Data Structures) and Python, capable of generating real-time suggestions from a large dataset.

This project demonstrates how efficient data structures and dataset-driven ranking can be combined to build scalable search systems.




## 🚀 Features

- Fast prefix-based search using Trie (DSA)
- Real-time suggestions with interactive Streamlit UI
- Handles large dataset (~300,000+ words)
- Dataset-based ranking of suggestions
- Optimized performance using caching




## ⚙️ How It Works

1. Words from the dataset are inserted into a Trie  
2. User enters a prefix  
3. Trie efficiently retrieves matching words  
4. Results are ranked using dataset information  
5. Suggestions are displayed in real-time via Streamlit  




## 🧠 Tech Stack

- Python  
- Data Structures (Trie)  
- Pandas / NumPy  
- Streamlit  




## 📸 Demo

<img width="1106" height="629" alt="homepage" src="https://github.com/user-attachments/assets/98af151e-9dd9-4460-a4a4-387f7bdd0d53" />
<img width="1099" height="625" alt="output" src="https://github.com/user-attachments/assets/46d481da-89e6-45d7-901b-271486f58251" />




## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```



## 📁 Project Structure
AI-Autocomplete-Engine/
│── app.py
│── src/
│   ├── trie.py
│   ├── preprocess.py
│   ├── autocomplete.py
│── data/
│── requirements.txt




## 👩‍💻 Author
Gaurangi Sonar
