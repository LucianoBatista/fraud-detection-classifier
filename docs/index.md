---
title: Home
authors:
    - Luciano
---

![tera_nvidia](imgs/1633367202129-desafio%20classificação.png)

The objective of this documentation is to provide an overview about the project. Here, you'll find all the steps of a Data Science Project:

- **Exploratory Data Analysis**
- **Iterative Modeling**
- **Metrics Analysis**
- **API Development**
- **Deploy on Heroku**


The motivation of this project came from the Fraud Detection Challenge offer by the Tera and NVidia.

## The Challenge

Fraud is a problem that impact a lot of different fields, like: government, bank, ratailer, micro-entrepreneur. So, is very important to everyone to know how to face this challenge.



The **ACFE** [report](https://www.acfe.com/rtm2019/index.html#Learn) (*Association of Certified Fraud Examiners*) corroborates this perception by pointing to a forecast of 60% growth in the next two years in **investments in anti-fraud**.

In the same report, **58% of companies** declare that:

> ... we do not have sufficient levels, resources and professionals to act in anti-fraud actions.

According to [**Psafe**](https://www.psafe.com/), from January to August of last year there were 920 thousand cases in only in Brazil, meaning that **3.6 frauds happen in the country** per minute. For example, more than **11 million [bank phishing](https://canaltech.com.br/seguranca/O-que-e-Phishing/)** attempts were detected.

In the [November 2020 report](https://api.abecs.org.br/wp-content/uploads/2020/11/Apresentacao-Balanco-3T20.pdf) is listed among the financial sector's priorities to fraud reduction and the **use of an artificial intelligence system to monitor it**. According to [Febraban](https://portal.febraban.org.br/) (*Brazilian Federation of Banks*) to mitigate this risk, an annual expenditure of around BRL 2 billion on IT per year is expected in Brazil. 

However, the risk is heightened not only by the sophistication of cyber criminals, but also by consumer dissatisfaction that not only abandons the customer base, but also uses the consumer code itself, which guarantees double compensation of the amounts charged.

In this scenario, **artificial intelligence emerges as a tool that gives more robustness, agility and flexibility to combat fraud**, working 24 hours a day, 7 days a week, making it a more than possible way, necessary for financial institutions to can effectively combat fraudsters. 

An example of this is American Express, with more than **115 million** active credit cards, which fights fraud using inference and Deep Learning, reducing fraud-related expenses by **US$ 1.2 trillion**, in detection processes that happen in milliseconds . **This fact guarantees the company the lowest fraud rate in the world for 13 consecutive years.**

### The Mission

**You**, as a manager, have the mission in this challenge to **dethrone American Express** as the best institution in the fight against fraud. To do so, you need to propose a solution for fraud detection and analysis that can reduce the company's risks and ensure healthy margins.

The mission is not easy, as the large volume of information and technological legacy are the reality of most corporations in the sector, even among leading companies. In addition, artificial intelligence initiatives demand great capacity


## Models

All models are serialized as pickle files to reproducibility. All the models can be find on `models` directory, accessing the [github of the project](https://github.com/LucianoBatista/fraud-detection-classifier).

I'm using the following convention for name the pickle files:

- `{date_start_training}{model}v_{ordinal_number_qtt_trained_that_date}.sav`