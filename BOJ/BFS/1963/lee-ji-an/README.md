## Info

[1963](https://www.acmicpc.net/problem/1963)

<br>

## ๐ก ํ์ด ๋ฐฉ๋ฒ ์์ฝ

> 4์๋ฆฌ ์์๋ฅผ ๋ชจ๋ ๊ตฌํ๊ณ  ๊ฐ ์๋ฆฌ ์์ ์ซ์๋ฅผ ํ๋์ฉ ๋ฐ๊พธ๋ฉด์ bfs ๋ชฉํ ์ซ์์ ๋๋ฌํ๋ฉด ์ข๋ฃ

1. 4์๋ฆฌ ์์๋ฅผ ๋ชจ๋ ๊ตฌํจ 
2. 4์๋ฆฌ์ ์ซ์ ๋ฅผ 0~9๊น์ง ๋ฐ๊ฟ๋ณด๊ณ  ๊ทธ ์ซ์๊ฐ ํ์ํ ์ ์ด ์๋ ์์ด๋ฉด์ ์์์ด๋ฉด q์ ์ง์ด๋ฃ์
3. ๋ชฉํ ์ซ์์ ๋๋ฌํ๋ฉด ์ข๋ฃ
<br>

## ๐ ๋๋ ์ 
```
def changer(totalNumber, digit, n):  # totalNumber์ digit ์๋ฆฌ ์๋ฅผ n์ผ๋ก ๋ฐ๊พธ๊ฒ ๋ค
    s = list(str(totalNumber))
    s[digit] = chr(n + ord('0'))
    return int(''.join(s))
```
์ซ์์ ํน์  ์๋ฆฌ๋ง ๋ฐ๊พธ๊ณ  ์ถ์ ๋ ์ด๋ ๊ฒ ๋ง๋ค๋ฉด ๊ฐ๋จํ ๊ฒ ๊ฐ๋ค! (๊ฐ์ ์์์ ๋์ค๋ ๋ฐฉ๋ฒ)