# Canadian Retail Time Series: Econometric Decomposition & SARIMA Forecasting

[![R](https://img.shields.io/badge/R-4.2+-276DC3?style=flat&logo=r&logoColor=white)](https://www.r-project.org/)
[![Forecast](https://img.shields.io/badge/R%20Package-Forecast%20%2F%20Tseries-blue)](https://cran.r-project.org/web/packages/forecast/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: McMaster University (Ontario, Canada) — Time Series Modeling (STATS 4A03)  
> **Author**: Mohamed Nourou Dine CISSE  
> **Core Stack**: `R`, `SARIMA`, `Holt-Winters`, `STL Decomposition`, `Box-Cox`, `Ljung-Box`  
> **Key Deliverables**: 12-page Econometric Forecasting Monograph, Reproducible R Analysis Code

---

## 🇫🇷 Résumé Rapide en Français

Projet d'économétrie et de modélisation statistique avancée réalisé à l'**Université McMaster (Canada)** sur la série temporelle officielle des **ventes au détail au Canada** (Données Statistique Canada). 

Le jeu de données présente à la fois une tendance haussière de long terme et une saisonnalité annuelle prononcée avec pic majeur en décembre. J'ai conduit une méthodologie rigoureuse de **Box-Jenkins** :
- Transformation stabilisatrice de variance (**Box-Cox**).
- Différenciations régulière ($d=1$) et saisonnière ($D=1$) pour atteindre la stationnarité stricte (tests KPSS et ADF).
- Identification et estimation d'un modèle **$	ext{SARIMA}(p,d,q) 	imes (P,D,Q)_{12}$**.
- Diagnostic résiduel exhaustif vérifiant l'hypothèse de bruit blanc (absence d'autocorrélation résiduelle via le test de Ljung-Box).

Le rapport de **12 pages** synthétise les projections à 24 mois et les intervalles de confiance associés.

---

## 📌 Mathematical Model & Formulation

The Canadian retail volume $Y_t$ follows a seasonal multiplicative ARIMA process:

$$\Phi_P(B^{12}) \phi_p(B) (1 - B^{12})^D (1 - B)^d 	ilde{Y}_t = \Theta_Q(B^{12}) 	heta_q(B) \epsilon_t, \quad \epsilon_t \overset{iid}{\sim} \mathcal{N}(0, \sigma^2)$$

Residual diagnostics confirmed zero serial autocorrelation with Ljung-Box $p$-value $> 0.05$.

---

## 📂 Repository Layout

```text
11_McMaster_Canadian_Retail_Time_Series/
├── src/
│   ├── time_series_analysis.R       # Complete Box-Jenkins pipeline & forecasting script
│   └── stl_decomposition.R         # Seasonal and Trend decomposition with LOESS
├── reports/
│   └── Canadian_Retail_Time_Series_Report.pdf # 12-page formal forecasting monograph
└── README.md
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)\n