## Info
[17141 ์ฐ๊ตฌ์ 2](https://www.acmicpc.net/problem/17141)

## ๐ก ํ์ด ๋ฐฉ๋ฒ ์์ฝ
์ฐ๊ตฌ์ค ๋งต ์ ๋ณด๋ฅผ ์๋ ฅ๋ฐ์ผ๋ฉด์ ๋ฐ์ด๋ฌ์ค๋ฅผ ๋์ ์ ์๋ ์ขํ๋ค์ ๋ณ๋๋ก ์ ์ฅํด ๋๊ณ , `itertools.combinations`๋ฅผ ์ด์ฉํ์ฌ ๋ฐ์ด๋ฌ์ค๋ฅผ `M`๊ฐ ๋๋ ๋ชจ๋  ์กฐํฉ์ ์ํํ๋ฉฐ `spread()` ํจ์๋ก ์ ๋ฌํ์ฌ ์๋ฎฌ๋ ์ด์ํ ๊ฒฐ๊ณผ๋ฅผ ๋ฐ๋๋ค.  
์๋ฎฌ๋ ์ด์ ํ ๊ฒฐ๊ณผ๋ค ์ค ์ต์๊ฐ์ ์ถ๋ ฅํ๋ฉด ์ ๋ต. ๋ฐ์ด๋ฌ์ค๋ฅผ ํผํธ๋ฆด ๋ ๋ง๋ค ์นด์ดํธ๋ฅผ ์ฆ๊ฐ์ํค๊ณ , ํ์ฌ์ ์นด์ดํธ ๊ฐ๊ณผ ์ ์ฒด ๋งต์ ์๋ ์กด์ฌํ๋ ๋น ๊ณต๊ฐ+๋ฐ์ด๋ฌ์ค๋ฅผ ๋์ ์ ์๋ ๊ณต๊ฐ์ ์๋ฅผ ๋น๊ตํ์ฌ ๊ฐ์ผ์ ์๋ฃ ์ฌ๋ถ๋ฅผ ํ๋จํ๋ฉด ๋๋ค.

## ๐ ๋ง๋ฌด๋ฆฌ
์๋ณธ ์ฐ๊ตฌ์ค ์ ๋ณด๋ฅผ ์ ์งํ๊ธฐ ์ํด `spread()` ํจ์์ ์ธ์๋ก `lab`์ ์ ๋ฌํ  ๋๋ ๋ฆฌ์คํธ ์ปดํ๋ฆฌํจ์์ผ๋ก ๋ณต์ฌํ์ฌ ์ ๋ฌํ๋ค.  
ํจ์ ์์์๋ ๋ณ๋์ `visited` ๋ฐฐ์ด ์์ด๋ `lab` ๋ฐฐ์ด์ ๊ฐ์ ๋ฐ์ด๋ฌ์ค๊ฐ ์๋ค๋ ๊ฐ์ผ๋ก ๋งํน(์ฝ๋์์๋ `9`)ํจ์ผ๋ก์จ ๋ฐฉ๋ฌธ ์ฌ๋ถ๋ฅผ ์ฒดํฌํ  ์ ์๋ค.  
97% ์ฃ์ง ์ผ์ด์ค: ๋ชจ๋  ๋น ๊ณต๊ฐ์ด ๋ฐ์ด๋ฌ์ค๋ฅผ ์ค์ ๋ก ๋์ ์ ์๋ ๊ฒฝ์ฐ
