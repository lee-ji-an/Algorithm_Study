## Info

[11058 ν¬λ¦¬λ³΄λ](https://www.acmicpc.net/problem/11058)

<br>

## π‘ νμ΄ λ°©λ² μμ½

> μ΄λ€ μΉΈμ λ²νΌλ‘ μ¬μ©νμ¬ `Ctrl+V`λ₯Ό μ¬λ¬ λ² νλ κ²μ΄ κ°μ₯ ν¨κ³Όμ μΈμ§
- `dp[i]`λ₯Ό `ν€λ³΄λλ₯Ό iλ² λλ¬ λνλΌ μ μλ λ¬Έμμ μ΅λ κ°―μ` λ‘ μ μ
- `dp[7]`μ λ€μ κ°λ€ μ€ νλμ΄λ€
  - `Ctrl+A` `Ctrl+C` `Ctrl+V`μ μ΅μ 3λ²μ΄ μμλλ―λ‘ 3μΉΈ μ΄λ΄λ‘ λ¨μ΄μ§ μΉΈμ μ°Έμ‘° λΆκ°λ₯
  - `dp[4]`μμ `Ctrl+A` `Ctrl+C` `Ctrl+V` λ₯Ό μΆκ°νμ¬ `dp[4] * 2`
  - `dp[3]`μμ `Ctrl+A` `Ctrl+C` `Ctrl+V` `Ctrl+V`λ₯Ό μΆκ°νμ¬ `dp[3] * 3`
  - `dp[2]`λ λ²νΌλ₯Ό λ§λ€ μκ° μμΌλ―λ‘ (`A` + `Ctrl+A` `Ctrl+C`μ μ΅μ 3λ² μμ) μ λ¨
- `dp[11]`μ λ€μ κ°λ€ μ€ νλμ΄λ€
  - `dp[8]`μμ `Ctrl+A` `Ctrl+C` `Ctrl+V`
  - `dp[7]`μμ `Ctrl+A` `Ctrl+C` `Ctrl+V` `Ctrl+V`
  - `dp[6]`μμ `Ctrl+A` `Ctrl+C` `Ctrl+V` `Ctrl+V` `Ctrl+V`
  - `dp[5]`μμ `Ctrl+A` `Ctrl+C` `Ctrl+V` `Ctrl+V` `Ctrl+V` `Ctrl+V`
  - `dp[4]`μμ `Ctrl+A` `Ctrl+C` `Ctrl+V` `Ctrl+V` `Ctrl+V` `Ctrl+V` `Ctrl+V`
  - `dp[3]`μμ `Ctrl+A` `Ctrl+C` `Ctrl+V` `Ctrl+V` `Ctrl+V` `Ctrl+V` `Ctrl+V` `Ctrl+V`
---
μκΈ°λ³΄λ€ jμΉΈ λ¨μ΄μ§ μ§μ μ `dp[i-j]` κ°μ `j-1`λ² κ³±ν κ°λ€ μ€ μ΅λκ°μ΄ `dp[i]
<br>

## π λλ μ 
λΈκ°λ€μ μ°λ¬Όμ΄λ€
