## Info
[16236 ์๊ธฐ ์์ด](https://www.acmicpc.net/problem/16236)

## ๐ก ํ์ด ๋ฐฉ๋ฒ ์์ฝ
๋จผ์  ๋ฌผ๊ณ ๊ธฐ์ ์์ด์ ์์น๋ฅผ ์๋ ฅ ๋ฐ์ผ๋ฉด์ ๋์์ ์์ด์ ์ขํ์ ๋ฌผ๊ณ ๊ธฐ์ ์ด ๊ฐ์๋ฅผ ์ ์ฅํด ๋๋ค.  
์ด ๋, ์์ด์ ์์น(`9`)์ ๊ฐ์ ์ฐจํ BFS๋ฅผ ์ ์ฉํ  ๋, **ํฌ๊ธฐ๊ฐ 9์ธ ๋ฌผ๊ณ ๊ธฐ**๋ก ์ธ์ํ๋ ๊ฒ์ ๋ฐฉ์งํ๊ธฐ ์ํ์ฌ 0์ผ๋ก ๋ฐ๊ฟ ์ค๋ค.  
  
๋ค์์ผ๋ก๋ ํ์ฌ ์์ด์ ์์น ์ขํ๋ฅผ ์ ๋ฌ๋ฐ๊ณ , ๋จน์ ์ ์๋ ๋ฌผ๊ณ ๊ธฐ ์ค ๊ฐ์ฅ ๊ฐ๊น์ด ๋ฌผ๊ณ ๊ธฐ๋ฅผ ์ก์๋จน์ ํ, ์ฒ์ ์์น๋ก๋ถํฐ์ ๊ฑฐ๋ฆฌ์ ๊ทธ ๋ฌผ๊ณ ๊ธฐ๋ฅผ ์ก์๋จน์ ํ ์์ด์ ์ขํ๋ฅผ ๋ฐํํ๋ `bfs(row, col)` ํจ์๋ฅผ ์ ์ํ๋ค.  
BFS ํ์์์๋ ํ์ฌ์ ๊ฒฝ๋ก๊ฐ ํญ์ ์ต์ ์ด๋ผ๋ ์ ์ ์ด์ฉํ๋ค. ๋ค์ ๋งํด, ํ์ ์ค ๋ฌผ๊ณ ๊ธฐ๋ฅผ ํ ๋ฒ์ด๋ผ๋ ๋ง๋๋ฉด ๊ทธ ๊ฒฝ๋ก๋ ๊ทธ ๋ฌผ๊ณ ๊ธฐ๊น์ง์ ์ต๋จ๊ฒฝ๋ก๊ฐ ๋๋ค. ๋ฐ๋ณต ์ค ํ์ฌ์ ๊ฑฐ๋ฆฌ ์ต์๊ฐ๋ณด๋ค ๋ ํฐ ๊ฒฝ์ฐ๋ ์กฐ์ฌํ  ํ์๊ฐ ์๊ณ (ํ์ ์ฝ์ํ  ํ์ X), ์ต๋จ๊ฑฐ๋ฆฌ๊ฐ ๋์ผํ ๋ฌผ๊ณ ๊ธฐ๊ฐ 2๋ง๋ฆฌ ์ด์์ด๋ผ๋ฉด `row`๊ฐ์ด ์์ ๋ฌผ๊ณ ๊ธฐ๋ฅผ, ๊ฑฐ๋ฆฌ์ `row`๊ฐ์ด ๋์ผํ๋ค๋ฉด `col`๊ฐ๋ ๋น๊ตํ์ฌ ์ ์ผ ์์ ๋ฌผ๊ณ ๊ธฐ๋ฅผ ์ ํํ์ฌ ๋จน์ผ๋ฉด ๋๋ค.  
๋ฌผ๊ณ ๊ธฐ ํ๋ณด๊ตฐ ๋ฆฌ์คํธ(`candidate_list`)์ ํ๋ณด๊ตฐ ๋ธ๋๋ฅผ ์ฝ์ํ  ๋, `(๊ฑฐ๋ฆฌ, ํ, ์ด)` ์์ผ๋ก ํํ์ ๋ง๋ค์ด ์ฝ์ํ๋ฉด, `list.sort()`๋ฅผ ์ฌ์ฉํ์ฌ ์ฐ์ ์์๋ฅผ ์ฝ๊ฒ ๋ณด์กดํ  ์ ์๋ค.  
  
`bfs()` ํจ์๊ฐ ์ ์ ๋์๋ค๋ฉด ๋จ์ ์๋ ๋ฌผ๊ณ ๊ธฐ๊ฐ ์กด์ฌํ์ง ์์ ๋ ๊น์ง ๋ฃจํ๋ฅผ ๋๋ฉด์ `bfs()`๋ฅผ ๋ฐ๋ณต ํธ์ถํ์ฌ ๋ฌผ๊ณ ๊ธฐ๋ฅผ ์ก์๋จน์๊ณผ ๋์์ ์์ด์ ์ขํ๋ฅผ ์ด๋์ํค๊ณ , ๋ฌธ์ ์ ์กฐ๊ฑด์ ๋ง๊ฒ ์์ ์ ํฌ๊ธฐ์ ๋์ผํ ์์ ๋ฌผ๊ณ ๊ธฐ๋ฅผ ์ก์๋จน์๋ค๋ฉด ์์ด์ ํฌ๊ธฐ๋ฅผ 1 ์ฑ์ฅ์ํจ๋ค.  
๋ฃจํ ์์์ ํ ๋ฒ ์์ด๊ฐ ์์นํ๋ ๊ณณ์ ์ด๋ฏธ ๋ฌผ๊ณ ๊ธฐ๊ฐ ์ก์๋จนํ์ผ๋ฏ๋ก, ๋ฃจํ๋ฅผ ๋๋ฉด์ ์๋ณธ `matrix` ๋ฐฐ์ด์์ ํด๋น ์ขํ๋ฅผ 0์ผ๋ก ๋ฐ๊ฟ ์ฃผ์ด์ผ ํ๋ค.  
๋ฃจํ๋ `bfs()`๊ฐ `False`๋ฅผ ๋ฐํํ ๊ฒฝ์ฐ(๋จ์์๋ ๋ฌผ๊ณ ๊ธฐ๊ฐ ์์ง๋ง ๋ ์ด์ ์ก์๋จน์ ์ ์๋ ๋ฌผ๊ณ ๊ธฐ๊ฐ ์์ ๊ฒฝ์ฐ) ๋๋ `fish_cnt`๊ฐ 0์ด ๋๋ ๊ฒฝ์ฐ(๋ ์ด์ ๋จ์ ์๋ ๋ฌผ๊ณ ๊ธฐ๊ฐ ์๋ ๊ฒฝ์ฐ) ํ์ถํ๊ณ , ๊ทธ๋ ๋์ ๋ ์๊ฐ์ ์ถ๋ ฅํ๋ฉด ๋๋ค.

## ๐ ๋ง๋ฌด๋ฆฌ
์์ ์ ํ์๋ ๋ฌธ์ ์ธ๋ฐ ๊ตฌํ์์ ๋งํ์ ์์  ์์ค์ฝ๋๋ฅผ ์ฐธ๊ณ ํด์ ํ์๋ค. `bfs()` ํจ์ ๋ด์์ ํ์ ๋ฃ์ ๋, BFS ํ์์์ ํ์ฌ ๊ฒฝ๋ก๊ฐ ์ต์ ์ด๋ ๊ฒฝ๋ก๋ผ๋ ์ ์ ์ด์ฉํ์ฌ "`ํ์ฌ๊น์ง ์ด๋ํ ๊ฑฐ๋ฆฌ + 1` ์ ํด๋ ์ง๊ธ๊น์ง ๊ตฌํ ์ต์๊ฐ๋ณด๋ค ์์ ๊ฒฝ๋ก"๋ง ํ์ ์ฝ์ํ๋ ๊ฒ์ด ๋ถํ์ํ ์ฐ์ฐ์ ๋ง๊ธฐ ์ํ ํฌ์ธํธ.
