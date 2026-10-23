# Crypto Chatbot

A command-line chatbot that answers questions about crypto prices with live
data from the free [CoinGecko API](https://www.coingecko.com/en/api). You
type a command such as `price bitcoin` and it replies with the current
figures. No API key is needed.

It works from fixed commands, not free text: the first word picks the
command and the rest are its arguments.

## Commands

| Command | What it shows |
|---|---|
| `price <coin>` | Price in USD, 24-hour change and market cap |
| `top [n]` | The top n coins by market cap (default 10, at most 50) |
| `trending` | Coins trending on CoinGecko right now |
| `market <coin>` | Rank, price, market cap, 24-hour volume and circulating supply |
| `compare <coin1> <coin2>` | Price, 24-hour change and market cap side by side |
| `news` | Global market overview: total market cap, volume, Bitcoin dominance |
| `help` | The list of commands |
| `quit` | Exit |

Coins use CoinGecko ids, which are usually the full lower-case name:
`bitcoin`, `ethereum`, `dogecoin`.

## Example

A real session, run on 23 October 2026:

```
💬 You: price bitcoin

🤖 Bot: 💰 Bitcoin Price Info:
• Price: $81,535.00
• 24h Change: 📉 -0.16%
• Market Cap: $1,639,583,982,029
• Updated: 17:05:27

💬 You: top 3

🤖 Bot: 🏆 Top 3 Cryptocurrencies:

 1. Bitcoin (BTC) - $81,535.00 📉 -0.16%
 2. Ethereum (ETH) - $2,400.47 📉 -0.23%
 3. Tether (USDT) - $1.00 📉 -0.03%

💬 You: price notacoin

🤖 Bot: ❌ Coin 'notacoin' not found. Please check the spelling.
```

## How to run it

```bash
git clone https://github.com/Letsapatiiso07/crypto-chatbot.git
cd crypto-chatbot
pip install -r requirements.txt
python crypto_chatbot.py
```

It needs Python 3.6 or later, the `requests` library and an internet
connection.

## How it works

`crypto_chatbot.py` holds one class, `CryptoChatbot`. A dictionary maps each
command word to a method, and each method calls one CoinGecko endpoint
(`/simple/price`, `/coins/markets`, `/search/trending`, `/coins/{id}` or
`/global`), formats the reply and returns it as text. Network errors and
unknown coins come back as a short message instead of a crash.

## Limits

- **Fixed commands only.** It does not understand free text such as "how
  is bitcoin doing?".
- **Rate limits.** CoinGecko's free API limits how often you can call it.
  Several commands in quick succession can return `429 Too Many Requests`;
  wait a minute and try again.
- **Coin names must be CoinGecko ids.** Ticker symbols such as `btc` do not
  work.
- **No tests yet.**

For learning only; this is not investment advice.

## Author

Tiiso Letsapa, Letsapamyron07@gmail.com

MIT License, see [LICENSE](LICENSE).
