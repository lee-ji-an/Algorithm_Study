## Info

[1963 ์์ ๊ฒฝ๋ก](https://www.acmicpc.net/problem/1963)

<br>

## ๐ก ํ์ด ๋ฐฉ๋ฒ ์์ฝ

> bfs๋ก A์์ B๊ฐ ๋  ๋๊น์ง ํ์ํ๊ธฐ

### isPrime
* ์์์ธ์ง ํ๋ณ

### intToArray
* ์ ์๋ฅผ ๋ฐฐ์ด ํํ๋ก ๋ณํ
* ์) 1000 -> { 1, 0, 0, 0 }
* ๊ฐ ์๋ฆฌ์๋ฅผ ๋น๊ตํ๊ณ  ๋ฐ๊ฟ ๋ ์ฌ์ฉ

### arrayToInt
* ๋ฐฐ์ด ํํ์ ์๋ฅผ ์ ์๋ก ๋ณํ
* ์) { 1, 0, 0, 0 } -> 1000
* ์ ์๋ก ์ ์ฅํ๊ณ  ๊ด๋ฆฌ

### bfs
* ๋ฐฉ๋ฌธํ ์ง ์ฌ๋ถ๋ Set\<Integer\>์ผ๋ก ๊ด๋ฆฌ
* ๊ฐ ๋ค ์๋ฆฌ์ ๋ํ์ฌ 0~9๋ฅผ ๋ฃ์ด์ ์์์ด๊ณ  ํ์ํ ์ง ์์ผ๋ฉด ํ์

<br>

## ๐ ๋๋ ์ 
visited๋ฅผ Set์ผ๋ก ์ฌ์ฉํด๋ณธ ๊ฒ์ด ํฅ๋ฏธ๋กญ๋ค. ์ค์๋ฅผ ์กฐ์ฌํ์.