## Info
[16929 Two Dots](https://www.acmicpc.net/problem/16929)

## ๐ก ํ์ด ๋ฐฉ๋ฒ ์์ฝ
DFS๋ฅผ ํ์ฉํ์ฌ ์ฌ์ดํด์ด ์์ฑ๋๋์ง ๊ฒ์ฆํ๋ค. `dfs()` ํจ์์ ์ธ์๋ก ๋ฐฉ๋ฌธํ  ์ขํ์ ์์น์ ์ต์ด ์์ ์ขํ์ ์์น, `cnt`(ํธ์ถ depth)๋ฅผ ์ ๋ฌ๋ฐ๋๋ค.  

`dfs()` ๋ด๋ถ์์๋ ์ํ์ข์ฐ 4๋ฐฉํฅ์ ์ธ์ ํ ์ขํ์ ๋ํด ๋ฐฉ๋ฌธ ์ฌ๋ถ, ์ฌ์ดํด ์์ฑ ์ฌ๋ถ(์ด๊ธฐ์ขํ๋ ๋์ผํ ์ขํ), `board` ๋ฒ์ ๋ฒ์ด๋จ ์ฌ๋ถ๋ฅผ ํ์ธํ์ฌ ์ ์งํ  ์ ์๋ค๋ฉด ์ฌ๊ทํธ์ถํ๊ณ , ์ฌ์ดํด์ ์์ฑํ  ์ ์๋ค๋ฉด ์ ์ญ๋ณ์ `ans`๋ฅผ `True`๋ก ์ค์ ํ๊ณ  ๋ฆฌํดํ๋ค. ์ฌ๊ทํธ์ถ ์ ์๋ ํด๋น ์ขํ๋ฅผ ๋ฐฉ๋ฌธ์ฒ๋ฆฌํ๊ณ , ๋ค์ ๋ฐฉํฅ์ ํธ์ถ์์๋ ๊ทธ ์ขํ๊ฐ ์ํฅ์ ๋ฐ์ผ๋ฉด ์ ๋๋ฏ๋ก ํ ๋ฒ ์ฌ๊ทํธ์ถ์ด ๋๋๋ฉด ๋ค์ ๊ทธ ์ขํ๋ฅผ ๋ฏธ ๋ฐฉ๋ฌธ ์ฒ๋ฆฌํด ์ฃผ์ด์ผ ํ๋ค.  
  
**๋ํ, ํจ์๊ฐ ํธ์ถ๋์์ ๋ ์ ์ญ๋ณ์ `ans`๊ฐ `True`์ธ์ง๋ฅผ ์ฒดํฌํ์ฌ `True`๋ผ๋ฉด ๋ค๋ฅธ ๊ฒฝ๋ก์ ์ฌ๊ทํธ์ถ์์ ์ด๋ฏธ ์ฌ์ดํด์ ์ฐพ์๋ค๋ ์๋ฏธ์ด๋ฏ๋ก ๋ฐ๋ก ๋ฆฌํดํด ์ฃผ์ด์ผ ํ๋ค!**

## ๐ ๋ง๋ฌด๋ฆฌ
1. `dfs()` ํธ์ถ ์ด๊ธฐ์ ์ฌ์ดํด ๋ฐ๊ฒฌ ์ฌ๋ถ๋ฅผ ์ฒดํฌํ์ฌ ์ฐพ์๋ค๋ฉด ๋ฐ๋ก ๋ฐํ
2. ์ฌ๊ทํธ์ถ ์ ํ๋ก ๋ฐฉ๋ฌธ์ฒ๋ฆฌ/๋ฐฉ๋ฌธ์ฒ๋ฆฌ ํด์ 

์ด ๋ ๊ฐ์ง๊ฐ ํต์ฌ ํฌ์ธํธ์ธ๊ฒ ๊ฐ๋ค. ํนํ 2๋ฒ์ ๊ฒฝ์ฐ, ๊ฐ ์ฝ์คํ๋ง๋ค 4๋ฐฉํฅ์ผ๋ก ์ด 4๋ฒ์ ์ฌ๊ทํธ์ถ์ด ์ผ์ด๋๋๋ฐ, ์์ ๋ณด๋ค ๋จผ์  ํธ์ถ๋ ํจ์๊ฐ ๊ฒฝ๋ก๋ฅผ ์ฐพ์๋ค๋ฉด ํ๋๊ทธ ๋ณ์์ ํํ๋ก ๋๋จธ์ง ํจ์๋ค์ ์ค์ง์ํค๋ ์์์ด ํ์ํ๋ค. ์ฒ์์ ์ด๊ฑฐ ์๊ฐ ๋ชป ํด์ TLE ๋ด์..  
1๋ฒ์ ์ฒ๋ฆฌํ๊ณ  ๋ ์ดํ์ ์๊ฐ ์ด๊ณผ๋ ๋ฉดํ์ง๋ง ๋งค ํธ์ถ๋ง๋ค `hist`๋ผ๋ ์งํฉ์ ๊ณ์ ์ ์งํ๊ณ  ์์๊ธฐ์ ๋งค์ฐ ๋๋ ธ๋ค(์ฝ 1900ms). ํ์ง๋ง ์ด๋ฅผ ๋จ์ `visited` ๋ฐฐ์ด๋ก ์ฒ๋ฆฌํ์ฌ ์คํ์๊ฐ์ ๋ํญ ์ค์ผ ์ ์์๋ค(์ฝ 56ms).
