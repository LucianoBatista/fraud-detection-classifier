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

Today, to ensure the survival of your business, the great challenge is to reduce operating costs: fraud, especially those related to commercial and financial operations, which impact, in practice, all types of industries and sectors of the economy. From the government, to the bank, from the retailer to the micro-entrepreneur, everyone needs to know and face this challenge.

The **ACFE** [report](https://www.acfe.com/rtm2019/index.html#Learn) (*Association of Certified Fraud Examiners*) corroborates this perception by pointing to a forecast of 60% growth in the next two years in investments in anti-fraud, a clear example of the challenge organizations are facing. However, the same report points out that 58% of companies declare that they do not have sufficient levels, resources and professionals to act in anti-fraud actions (see table below:)

Considering that the goal of fraudsters in general is to have monetary benefits, it makes it evident that the financial sector is one of their main targets. Even the growing investment in preventive and monitoring actions has not been enough to stop or stop the escalation of criminals. According to [**Psafe**](https://www.psafe.com/), from January to August of last year there were 920 thousand cases in Brazil alone and every minute, **3.6 frauds happen in the country**. For example, more than **11 million bank fishing** attempts were detected.

The financial industry has great representation in Brazil and in the world. To get an idea, the assets of banks in Brazil total R$ 7.4 trillion, exceeding the country's own GDP [Infomoney](https://www.infomoney.com.br/economia/ativos-de-bancos-somam-r-74-trilhoes-e-superam-pib-brasileiro/).

 According to [ABECS](https://www.abecs.org.br/) (*Brazilian Association of Credit Card Companies and Services*), BRL 558 billion was handled in the first quarter of 2021 and credit cards represented **BRL $335 billion** of that total. There were **6.5 billion transactions**, an increase of 11.8%, with emphasis on the debit card, which showed an increase of 163% (see tables below). Despite the opulence of these numbers, the impact of fraud is equally glaring. Cybercrime, considering only credit card transactions, already projected in 2018 an **impact of 6 trillion dollars** of lost revenue by 2021 around the world.

No wonder, in the [November 2020 report](https://api.abecs.org.br/wp-content/uploads/2020/11/Apresentacao-Balanco-3T20.pdf) is listed among the financial sector's priorities to fraud reduction and the use of an artificial intelligence system to monitor it. According to [Febraban](https://portal.febraban.org.br/) (*Brazilian Federation of Banks*) to mitigate this risk, an annual expenditure of around BRL 2 billion on IT per year is expected in Brazil. However, the risk is heightened not only by the sophistication of cyber criminals, but also by consumer dissatisfaction that not only abandons the customer base, but also uses the consumer code itself, which guarantees double compensation of the amounts charged. All this, without considering the lawsuits for moral and material damages that can be filed by the consumer. According to the **National Council of Justice (CNJ)**, the projection is that 28% of the lawsuits in progress have financial institutions as defendants.

In this scenario, artificial intelligence emerges as a tool that gives more robustness, agility and flexibility to combat fraud, working 24 hours a day, 7 days a week, making it a more than possible way, necessary for financial institutions to can effectively combat fraudsters. An example of this is American Express, with more than **115 million** active credit cards, which fights fraud using inference and Deep Learning, reducing fraud-related expenses by **US$ 1.2 trillion**, in detection processes that happen in milliseconds . This fact guarantees the company the lowest fraud rate in the world for 13 consecutive years.

### The Mission

**You**, as a manager, have the mission in this challenge to dethrone American Express as the best institution in the fight against fraud. To do so, you need to propose a solution for fraud detection and analysis that can reduce the company's risks and ensure healthy margins. Remember, the result of your work will give you and your area even more visibility. Be judicious, use good arguments, facts and justifications for your proposal, as well as, of course, make a good execution of your project.

The mission is not easy, as the large volume of information and technological legacy are the reality of most corporations in the sector, even among leading companies. In addition, artificial intelligence initiatives demand great capacity


## Models

All models are serialized as pickle files to reproducibility. All the models can be find on `models` directory, accessing the [github of the project](https://github.com/LucianoBatista/fraud-detection-classifier).

I'm using the following convention for name the pickle files:

- `{date_start_training}{model}v_{ordinal_number_qtt_trained_that_date}.sav`