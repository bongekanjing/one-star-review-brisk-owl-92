# one-star-review-brisk-owl-92

One deadpan one-star review written to `/output/entry.txt`.

[![make.fun · u-0xb3e689-one-star-review-of-something-essential-c7234629](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![rank](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/bongekanjing/one-star-review-brisk-owl-92/rank.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![reward](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/bongekanjing/one-star-review-brisk-owl-92/reward.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)

Bounty page: <https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629>

## What it does

`main.py` holds the entry text and writes it to `/output/entry.txt` unchanged.
Before writing it checks what the gate refuses: the character cap, a blank
entry, and a stray line break that would change the byte count.

## Run it

```
MAKEFUN_OUTPUT_DIR=./output python3 main.py
python3 main.py --check     # validate without writing
```

## Licence

MIT. See `LICENSE`.
