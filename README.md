# ⚽ Arsenal Set-Piece Analysis Dashboard

## 📊 Overview

This project is an interactive football analytics dashboard that evaluates Arsenal’s corner-kick performance using event data and expected goals (xG).

The goal is to simulate a **real-world football innovation workflow**, where data is transformed into actionable tactical insights.

---

## 🚀 Key Features

* 📍 Player-based shot mapping from corners
* 🎯 xG-based shot quality visualization (bubble size)
* 🧠 Zone-based analysis (Near Post, Central, Far Post, Edge)
* 📊 Interactive filters (players, zones)
* 📈 Summary metrics (Total Shots, Total xG, Avg xG)

---

## 🧩 Data Source

* Event data collected using `understatapi`
* Matches: 10 Arsenal matches (2025 season)
* Focus: Corner situations leading to shots

---

## 🧠 Methodology

### 1. Data Processing

* Extracted shot-level event data
* Engineered team labels and filtered Arsenal events
* Isolated corner situations

### 2. Feature Engineering

* Converted coordinates to pitch dimensions
* Created spatial zones:

  * Near Post
  * Central
  * Far Post
  * Edge/Outside

### 3. Analysis

* Shot distribution by zone
* xG per shot by zone
* Player involvement in set-piece situations

---

## 📊 Key Insights

* Corner shots are heavily concentrated in **central zones**, generating the highest total xG
* **Defenders dominate shot involvement**, indicating reliance on aerial threats
* **Far-post zones are underutilized**, suggesting limited attacking variation
* Edge-of-box shots show **low xG efficiency**, highlighting second-phase inefficiencies

---

## ⚽ Tactical Implications

* Maintain central attacking strength while introducing variation
* Increase far-post targeting to reduce predictability
* Improve second-ball structure for higher-quality edge shots
* Introduce more diverse player involvement in attacking phases

---

## 🖥️ Demo

Run locally:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
arsenal-setpiece-analysis/
├── app11.py
├── requirements.txt
├── data/
│   └── corners_data.csv
└── README.md
```

---

## 🛠️ Tech Stack

* Python (pandas, matplotlib)
* mplsoccer (pitch visualization)
* Streamlit (dashboard)
* understatapi (data collection)

---

## 🎯 Project Objective

This project demonstrates the ability to:

* Build end-to-end football analytics workflows
* Translate data into tactical insights
* Communicate findings through interactive visualization
* Simulate real-world performance analysis environments

---

## 📌 Note

This analysis focuses only on corner situations that resulted in shots due to event data limitations.

---

## 👤 Author

**AYAMAH YAW STEPHEN**
📍 Accra, Ghana
📧 [ayamahstephen90@gmail.com](mailto:ayamahstephen90@gmail.com)
🔗 LinkedIn: linkedin.com/in/ayamah-stephen
🔗 GitHub: github.com/stephen1-hub

