# 🚀 Crypto Chatbot

A Python-based cryptocurrency chatbot that provides real-time crypto market data using the CoinGecko API.

## Features

- 💰 **Price Lookup**: Get current prices for any cryptocurrency
- 🏆 **Top Coins**: View top cryptocurrencies by market cap
- 🔥 **Trending**: See what's trending in the crypto space
- 📊 **Market Data**: Detailed market information including market cap, volume, and supply
- ⚖️ **Compare**: Compare two cryptocurrencies side by side
- 📰 **Market Overview**: Global crypto market statistics
- 🤖 **Interactive Chat**: Easy-to-use command-based interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/crypto-chatbot.git
cd crypto-chatbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the chatbot:
```bash
python crypto_chatbot.py
```

## Usage

Once the chatbot is running, you can use these commands:

### Basic Commands
- `help` - Show all available commands
- `quit` - Exit the chatbot

### Price & Market Data
- `price bitcoin` - Get current Bitcoin price
- `price ethereum` - Get current Ethereum price
- `market dogecoin` - Get detailed market info for Dogecoin

### Rankings & Trends
- `top` - Show top 10 cryptocurrencies
- `top 5` - Show top 5 cryptocurrencies
- `trending` - Show trending coins

### Comparisons & Analysis
- `compare bitcoin ethereum` - Compare Bitcoin and Ethereum
- `news` - Get global market overview

## Example Session

```
🚀 Welcome to Crypto Chatbot!
Type 'help' for available commands or 'quit' to exit.
--------------------------------------------------

💬 You: price bitcoin

🤖 Bot: 💰 Bitcoin Price Info:
• Price: $43,250.00
• 24h Change: 📈 +2.45%
• Market Cap: $847,123,456,789
• Updated: 14:30:25

💬 You: top 3

🤖 Bot: 🏆 Top 3 Cryptocurrencies:

 1. Bitcoin (BTC) - $43,250.00 📈 +2.45%
 2. Ethereum (ETH) - $2,580.50 📉 -1.23%
 3. Tether (USDT) - $1.00 📈 +0.01%

💬 You: quit

🤖 Bot: 👋 Thanks for using Crypto Chatbot! Goodbye!
```

## API

This chatbot uses the [CoinGecko API](https://www.coingecko.com/en/api) to fetch cryptocurrency data. No API key is required for basic usage.

## Requirements

- Python 3.6 or higher
- `requests` library
- Internet connection

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This chatbot is for educational and informational purposes only. Cryptocurrency investments carry risk, and you should do your own research before making any investment decisions.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

Made with ❤️ by Tiiso