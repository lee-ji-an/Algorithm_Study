## Info
[16933](https://www.acmicpc.net/problem/16933)

## ๐ก ํ์ด ๋ฐฉ๋ฒ ์์ฝ
visited : bfs ํ์ํ๋ฉด์ ํ์ฌ๊น์ง ๋์ฐฉํ ์ ๋ค ์ค์ ๋จ์ ๋ฒฝ๋ค ์๊ฐ ๊ฐ์ฅ ์์ ๊ฐ์ ์ ์ฅ

1. bfs๋ก ๋งต์ ํ์ํ๋ค๊ฐ ๋ถ์  ์ ์๋ ๋ฒฝ ๊ฐฏ์๊ฐ ๋จ์์์ ๋ ๋ฒฝ์ด ์์ผ๋ฉด ๋ฌด์กฐ๊ฑด ๋ถ์จ
2. visited์ ์ ์ฅ๋ ๊ฐ๊ณผ ํ์์ ๊บผ๋ธ ์์ด์ ๋จ์ ๋ฒฝ์ ๊ฐฏ์๋ฅผ ๋น๊ตํ์ ๋ ํ์์ ๊บผ๋ธ ์์ด์ ๋ฒฝ์ ๊ฐฏ์๊ฐ ๋ ํด ๋๋ง ํ์ ๋ฃ์
- ๋ฒฝ์ด ์์ ๋
   1. ๋ฒฝ์ ๋ถ์  ๋ ๋ฎ์ด๋ฉด -> ๊ทธ๋ฅ ๋ถ์๋ฉด ๋จ
   2. ๋ฒฝ์ ๋ถ์  ๋ ๋ฐค์ด๋ฉด -> cnt๋ง ์ฆ๊ฐ์์ผ์ ๋ค์ ํ์ ๋ฃ์
- ๋น๊ณต๊ฐ์ผ ๋ 
   1. ํ์ ๋ฃ์
## ๐ ๋ง๋ฌด๋ฆฌ

๋ฎ์ธ์ง ๋ฐค์ธ์ง ํ์ธํ๋ ๋ฐฉ๋ฒ
1. ํ์ ๋ฎ์ธ์ง ๋ฐค์ธ์ง๋ฅผ ๊ฐ์ด ๋ฃ์ด๋๋ ๋ฐฉ๋ฒ (์ฝ๋์์ bfs ํจ์)
2. cnt % 2 == 1 -> ๋ฎ / cnt % 2 == 0 -> ๋ฐค ์ผ๋ก ๊ณ์ฐํ๋ ๋ฐฉ๋ฒ (์ฝ๋์์ bfs2 ํจ์)

2๋ฒ ๋ฐฉ๋ฒ์ด ์ฝ๊ฐ ๋ ๋นจ๋์!
