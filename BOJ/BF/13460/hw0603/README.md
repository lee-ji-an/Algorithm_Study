## Info
<a href="https://www.acmicpc.net/problem/13460">
    13460 ๊ตฌ์ฌ ํ์ถ 2
</a>

## ๐ก ํ์ด ๋ฐฉ๋ฒ ์์ฝ
`board`์ ์ ๋ณด๋ฅผ ์๋ ฅ๋ฐ์ผ๋ฉด์ ๋นจ๊ฐ ๊ตฌ์ฌ, ํ๋ ๊ตฌ์ฌ, ๊ตฌ๋ฉ์ ์ขํ๋ฅผ ๋ณ๋๋ก ์ ์ฅํด ๋๊ณ , ์ค์  `board` ๋ฐฐ์ด์๋ ๋ฒฝ๊ณผ ๋น ๊ณต๊ฐ, ๊ตฌ๋ฉ๋ง ์กด์ฌํ๋๋ก ์ ์ฅํ๋ค(๋ ๊ตฌ์ฌ์ ์์น๋ ์ฐ์  ๋น ๊ณต๊ฐ ์ฒ๋ฆฌ)  
  
๋ฌธ์ ์ ์กฐ๊ฑด์ ๋ง๊ฒ ํ์ฌ ๊ฐ ๊ตฌ์ฌ์ ์ขํ์ ๊ธฐ์ธ์ด๋ ๋ฐฉํฅ์ ์ ๋ฌ๋ฐ์ ํด๋น ๋ฐฉํฅ์ผ๋ก ๊ธฐ์ธ์์ ๋ ์ต์ข ๊ตฌ์ฌ์ ์ขํ๋ฅผ ๋ฐํํ๋ `tilt()` ํจ์๋ฅผ ์ ์ํ๋ค.  
๋ฌดํ๋ฃจํ ์์์ ๊ฐ ๊ตฌ์ฌ์ด ๋ฒฝ์ ๋ฟ๊ฑฐ๋ ๊ตฌ๋ฉ์ ๋น ์ ธ ๋ ์ด์ ์งํํ  ์ ์์ ๋ ๊น์ง Red์ Blue์ ์ขํ๋ฅผ ์ ๋ฌ๋ฐ์ ๋ฐฉํฅ์ผ๋ก ํ ์นธ์ฉ ์ด๋์ํค๋ฉฐ ์ต์ข ์์น๋ฅผ ๊ตฌํด์ผ ํ๋ค.  
  
1. ์๋ก์ด ๊ตฌ์ฌ์ ์ขํ(ํ ์นธ ์ด๋ํ ์ขํ)๊ฐ ๋ฒฝ ์์น๋ผ๋ฉด ๊ทธ ๋ฐฉํฅ๊ณผ ๋ฐ๋ ๋ฐฉํฅ์ผ๋ก ํ ์นธ ์ด๋์์ผ ์ด๋์ ์ทจ์ํ๋ ํจ๊ณผ๋ฅผ ๊ตฌํํ๋ค.
2. ๋ก์ง ์ํ ํ ๋นจ๊ฐ ๊ตฌ์ฌ๊ณผ ํ๋ ๊ตฌ์ฌ์ ์ต์ข ์ขํ๊ฐ ๋์ผํ ๊ฒฝ์ฐ(๋ ๊ตฌ์ฌ์ด ๊ฒน์น๋ ๊ฒฝ์ฐ)๊ฐ ์๋ค๋ฉด, ์ ์ ํ ์ฒ๋ฆฌํด ์ฃผ์ด์ผ ํ๋ค.
    - ์ฐ์  ๋ ๊ตฌ์ฌ์ ์ขํ๊ฐ ๊ฒน์ณค๋ค๋ ๊ฒ์ ํด๋น ๋ฐฉํฅ์ผ๋ก ๊ธฐ์ธ์์ ๋ ๋ ์ด์ ์์ง์ผ ์ ์๋ ์์น๊น์ง ์๋ค๋ ๊ฒ์ด๋ฏ๋ก ๋ ๊ตฌ์ฌ ๋ชจ๋ ์ด๋์ ์ค์ง์ํจ๋ค.
    - ๊ทธ ์ดํ ๋ ๊ตฌ์ฌ ์ค ํ๋๋ฅผ `victim`์ผ๋ก ์ค์ ํ์ฌ ํด๋น ๊ตฌ์ฌ์ ์ด๋์ ํ ๋จ๊ณ ์คํ์ทจ์ํ๋ค.
    - ๊ธฐ์ธ์ด๋ ๋ฐฉํฅ์ ๊ณ ๋ คํด ๋ณด๋ฉด ๋ค์๊ณผ ๊ฐ์ ์กฐ๊ฑด์ด ๋ง๋ค์ด์ง๋ค.
      - ์: row๊ฐ ๋ ํฐ ๊ฒ์ ์คํ์ทจ์
      - ํ: row๊ฐ ๋ ์์ ๊ฒ์ ์คํ์ทจ์
      - ์ข: col์ด ๋ ํฐ ๊ฒ์ ์คํ์ทจ์
      - ์ฐ: col์ด ๋ ์์ ๊ฒ์ ์คํ์ทจ์
3. ํ๋ ๊ตฌ์ฌ์ด ๊ตฌ๋ฉ์ ๋น ์ง ๊ฒฝ์ฐ๋ ์คํจ์์ด ์๋ชํจ์ผ๋ก ์ผํฐ๋ ๊ฐ์ ๋ฐํํ๋ฉด ๋์ง๋ง, ๋นจ๊ฐ ๊ตฌ์ฌ์ด ๊ตฌ๋ฉ์ ๋ค์ด๊ฐ๋ค๊ณ  ํด์ ๋ฐ๋ก ์ฑ๊ณต์ ํ๋จํ๋ฉด ์ ๋๋ค. ๋ฌธ์ ์ ์กฐ๊ฑด์์ ๋นจ๊ฐ ๊ตฌ์ฌ๊ณผ ํ๋ ๊ตฌ์ฌ์ด ๊ฐ์ด ๋น ์ ธ๋ ์คํจ๋ก ๊ฐ์ฃผํ๋ค๊ณ  ํ๊ธฐ ๋๋ฌธ.
  
`tilt()` ํจ์์ ์ ์๊ฐ ์๋ฃ๋๋ค๋ฉด ๋ฌธ์ ์์ ์ต๋ ์ด๋ ํ์์ธ 10ํ ์ด๋ด์์ ๋์ฌ ์ ์๋ ๋ชจ๋  ๊ฒฝ์ฐ๋ฅผ ํ์คํธํ๋ฉด ๋๋ค. ์ค๋ณต์์ด์ด๋ฏ๋ก `PI(4, 10)` ์ด๊ณ , `itertools.product`๋ก ์๋ง์ `iterator`๋ฅผ ํ์ฉํ  ์ ์๋ค.  
๋ฃจํ ์์์ `tilt()`๋ฅผ ํธ์ถํ์ฌ ๊ธฐ์ธ์ด๋ ๋์์ ์๋ฎฌ๋ ์ด์ํ๊ณ , ๊ฐ ํธ์ถ ๊ฒฐ๊ณผ์ ๋ํด ์ด๋ค ๊ตฌ์ฌ์ด ๋น ์ก๋์ง ์ฌ๋ถ๋ฅผ ์ฒดํฌํ์ฌ ์กฐ๊ฑด์ ๋ง๋ ์ด๋์ ์ต์ ํ์๋ฅผ ๊ตฌํ  ์ ์๋ค.  
**์ด ๋, ์ฐ์ํด์ ๊ฐ์ ๋ฐฉํฅ์ผ๋ก ๊ธฐ์ธ์ด๋ ๊ฒฝ์ฐ๋ ์๋ฏธ๊ฐ ์์ผ๋ฏ๋ก ์ ์ธํด ์ฃผ์ด์ผ ํ๋ค.**

```
for dirlist in product(("์", "ํ", "์ข", "์ฐ"), repeat=10):
    # ์ฐ์ํด์ ๊ฐ์ ๋ฐฉํฅ์ผ๋ก ๊ธฐ์ธ์ด๋ ๊ฒฝ์ฐ skip
    if (any(i == j for i, j in zip(dirlist, dirlist[1:]))):
        continue

    # ์์์์ ๋ง๊ฒ ์๋ฎฌ๋ ์ด์
    for dir in dirlist:
        r, b = tilt(dir, r, b)

        ... # ์ด๋ค ๊ตฌ์ฌ์ด ๋น ์ก๋์ง ์ฒดํฌ
```

## ๐ ๋ง๋ฌด๋ฆฌ
`tilt()` ํจ์์ ์กฐ๊ฑด์ ๋ง๊ฒ ๊ตฌํํ๋๋ผ ์ ๋ฅผ ๊ฝค ๋จน์๋ค. ํจ์๋ฅผ ๊ตฌํํ๊ณ  ๋๋ ๋จ์ํ ๊ฐ์ง์น๊ธฐ ํ ๋ธ๋ฃจํธํฌ์ค๋ก ์ฝ๊ฒ ํ ์ ์์๋ค.
