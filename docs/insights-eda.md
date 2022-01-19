# Desbalanceamento

- [x] O dado é 99.88% desbalanceado
- [x] A variável type: algumas classes não possuem variabilidade na variável target, mas segundo Patrícia isso não é um problema. **Precisamos calcular a correlação!**
- [x] A variável is_flagged_fraud **possui apenas 16 registros do tipo fraude**, o que não explica muita coisa.
  - Precisaríamos tirar essa dúvida sobre a variável
- [x] Amount analysis


- Gráfico pela hora do dia:
  - Hora do dia me parece ter uma correlação bem bosta: -0.037
  - em média a mesma quantidade de frauds por hora


- Se dividir o dado no meio, vamos ver que nos primeiros 15 dias temos uma média de fraude bem menor que depois desses 15 dias. Adicionar categoria before_400, after_400.
- A média de valor transacionado também possui relação com se é fraude ou não.
