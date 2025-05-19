# 🏥 Emergency Medical Service Coverage Analysis using Haversine Distance

This project analyzes emergency **hospital service coverage** using **Haversine distance** to determine which hospitals are within a specified radius (10 km) of accident locations. It also visualizes the spatial relationships between accident spots and nearby hospitals.

---

## 📌 Problem Statement

Given a list of hospitals and accident locations, determine:

> **Which hospitals lie within 10 km of each accident site?**  
> Use the **Haversine formula** to compute great-circle distances on Earth's surface.

---

## 🧮 Haversine Formula

To compute distance between two geographic points (lat/lon):

\[
d = 2r \cdot \arcsin\left( \sqrt{ \sin^2\left( \frac{\Delta \phi}{2} \right) + \cos(\phi_1) \cdot \cos(\phi_2) \cdot \sin^2\left( \frac{\Delta \lambda}{2} \right)} \right)
\]

Where:

- \( r \) is the Earth’s radius (≈ 6371 km)
- \( \phi \): latitude in radians
- \( \lambda \): longitude in radians

---

## 📁 Sample Data

### 🚑 Hospitals (`hospitals.csv`)

| hospital_id | name                | latitude | longitude |
| ----------- | ------------------- | -------- | --------- |
| 1           | General Hospital    | 23.8103  | 90.4125   |
| 2           | City Care           | 23.7500  | 90.3600   |
| 3           | North Health Center | 23.8500  | 90.4200   |

### 💥 Accidents (`accidents.csv`)

| accident_id | latitude | longitude |
| ----------- | -------- | --------- |
| 101         | 23.7900  | 90.4000   |
| 102         | 23.7600  | 90.3700   |
| 103         | 23.8400  | 90.4600   |

---

## ⚙️ Required Libraries

Install the necessary libraries using:

```bash
pip install pandas numpy matplotlib
```
