## Info

[12946 ์ก๊ฐ ๋ณด๋](https://www.acmicpc.net/problem/12946)

<br>

## ๐ก ํ์ด ๋ฐฉ๋ฒ ์์ฝ

> dfs๋ก ์ด๋ถ ๊ทธ๋ํ๋ก ์์น ํ๊ณ  ์์น ํ์ผ๋ฉด ์ ์ด๋ 1, ์ธ์ ํ ์์ ๋ฐ๋ผ 2 ๋๋ 3 ๋ถ์ฌํ๊ธฐ

1. color ๋ฐฐ์ด : 0์ด๋ฉด ๋ฐฉ๋ฌธx, 1์ด๋ฉด ์๊น1, 2์ด๋ฉด ์๊น2๋ก ์น ํด์ง ๊ฒ
2. ์์น ํด์ผ ํ๋๋ฐ ์๋ ๊ณณ์ dfs๋ก ์์น ํ๊ธฐ

### dfs
1. ์ด ํจ์์ ๋ค์ด์์ผ๋ฉด ์ผ๋จ ์์น ์ ํด์ผํ๊ธฐ ๋๋ฌธ์ ๋ต์ ์ต์ 1
2. ํ์ฌ ์ขํ์ ๋ํด์ ๋ง๋ฟ์์๋ 6๊ฐ์ ์นธ์ ๋ํ์ฌ
   1. ์์น ํด์ผ ํ๋๋ฐ ์๋ผ์์ผ๋ฉด ๋ค๋ฅธ ์๊น๋ก ์์น  ๋ณด๋ด๊ธฐ(dfs)
   2. ์๋ก ๋ง๋ฟ์์๋ (i,j), (ni,nj)์ด ๋ ๋ค ์์น ๋์ด์ผ ํ๋ฏ๋ก ๋ต์ ์ต์ 2
   3. (ni,nj)๋ฅผ ์์น ํ๊ณ  ์๋๋ฐ (i,j)์ ๊ฐ์ ์์ผ๋ก ๋์์์ผ๋ฉด ์๊น ์ถ๊ฐํด์ผ ํ๋ฏ๋ก ๋ต์ 3

<br>

## ๐ ๋๋ ์ 
๋ต์ด ์ต๋ 3์ด๊ณ  ํ์ฌ ์นธ์ ๋๋ฌ์ผ 6๊ฐ์ ์นธ๊ณผ ๋น๊ตํ๋ ๊ฒ๊น์ง๋ ๊ฐ๋๋ฐ ๋ง๋ฌด๋ฆฌ๊ฐ ์๋ผ์ ๊ฒฐ๊ตญ ๊ฐ์ ์์ฒญ ..<br>
์ธ์์ ์ด๋ ๊ฒ๋ ๊ฐ๋จํ๊ณ  ๊น๋ํ ๋ก์ง ๊ทผ๋ฐ ์ด์  ๋ด๊ฐ ์งค ์๋ ์๋ ...
