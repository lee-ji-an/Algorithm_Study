## Info

[6087](https://www.acmicpc.net/problem/6087)

<br>

## π‘ νμ΄ λ°©λ² μμ½

> μμ μμΉμμ bfs νμ (λμλ¨λΆμΌλ‘ ν μΉΈμ© νμνλ κ²μ΄ μλλΌ κ° μ μλ κ±°λ¦¬ λκΉμ§ νμ)  
  μλ? λ°©ν₯μ μΌλ§λ λ°κΏ¨λμ§λ§ μ€μνλκΉ!

1. μμμμΉμμ bfs νμ
2. λ€ λ°©ν₯μΌλ‘ νμ, λ€ λ°©ν₯ λͺ¨λ λ²½μ΄λ λ§΅μ λμ λ§λ  λκΉμ§ κ³μ νμνλ©° νμ λ£μ
3. λͺ©ν μ§μ μ λλ¬νλ©΄ μ’λ£
<br>

## π λλ μ 
λ°©ν₯μ λ°κΎΌ νμλ§ κ΄μ¬μλ μμΉ!
λ°λΌμ νμ¬ μμΉμμ λ°©ν₯μ ν λ²λ§ λ°κΏμ κ° μ μλ λͺ¨λ  μμΉλ₯Ό νμ λ£μΌλ©΄ λλ€!
visited μ λ°©ν₯μ λ°κΎΌ νμλ₯Ό μ μ₯νλλ° 
λ΄κ° νμμΉμμ visitedλ₯Ό κ²μ¬νμ λ λλ κ°μ μκ° μ μ₯λμ΄μμ΄λ κ³μ νμμ ν΄λ΄μΌν¨.  
μλ..  
κ·Έ μμΉμ λμ°©νμ λμ λ°©ν₯μ ν νμλ κ°μμ§λΌλ  
μ²μμ λμ°©ν μμ΄λ κ·Έ μμΉμμ λμμ λκ°κ³ ,  
λμ€μ λμ°©ν μμ΄λ κ·Έ μμΉμμ μ λμμ λκ° μλ μκΈ° λλ¬Έ  

```
while True:
  ...
    if board[movey][movex] == '*' or visited[movey][movex] < corner+1:
        break
```