import requests
from datetime import datetime

class CryptoChatbot:
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"
        self.commands = {
            'help': self.show_help,
            'price': self.get_price,
            'top': self.get_top_coins,
            'trending': self.get_trending,
            'market': self.get_market_cap,
            'compare': self.compare_coins,
            'news': self.get_news_sentiment,
            'quit': self.quit_bot
        }
        
    def show_help(self, args=None):
        """Display available commands"""
        help_text = """
🚀 Crypto Chatbot Commands:
        
• help - Show this help message
• price <coin> - Get current price (e.g., 'price bitcoin')
• top [number] - Show top cryptocurrencies (default: 10)
• trending - Show trending coins
• market <coin> - Get market cap info
• compare <coin1> <coin2> - Compare two cryptocurrencies
• news - Global market overview
• quit - Exit the chatbot

Examples:
- price ethereum
- top 5
- compare bitcoin ethereum
- market dogecoin
        """
        return help_text
    
    def get_price(self, coin_name):
        """Get current price of a cryptocurrency"""
        try:
            if not coin_name:
                return "❌ Please specify a coin name. Example: 'price bitcoin'"
            
            # Convert to lowercase and replace spaces with hyphens
            coin_id = coin_name.lower().replace(' ', '-')
            
            url = f"{self.base_url}/simple/price"
            params = {
                'ids': coin_id,
                'vs_currencies': 'usd,btc',
                'include_24hr_change': 'true',
                'include_market_cap': 'true'
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if not data:
                return f"❌ Coin '{coin_name}' not found. Please check the spelling."
            
            coin_data = data[coin_id]
            price_usd = coin_data['usd']
            change_24h = coin_data.get('usd_24h_change', 0)
            market_cap = coin_data.get('usd_market_cap', 0)
            
            # Format the response
            change_emoji = "📈" if change_24h >= 0 else "📉"
            change_color = "+" if change_24h >= 0 else ""
            
            result = f"""
💰 {coin_name.title()} Price Info:
• Price: ${price_usd:,.2f}
• 24h Change: {change_emoji} {change_color}{change_24h:.2f}%
• Market Cap: ${market_cap:,.0f}
• Updated: {datetime.now().strftime('%H:%M:%S')}
            """
            return result.strip()
            
        except requests.exceptions.RequestException as e:
            return f"❌ Network error: {str(e)}"
        except Exception as e:
            return f"❌ Error fetching price: {str(e)}"
    
    def get_top_coins(self, limit=None):
        """Get top cryptocurrencies by market cap"""
        try:
            limit = int(limit) if limit else 10
            limit = min(limit, 50)  # Cap at 50
            
            url = f"{self.base_url}/coins/markets"
            params = {
                'vs_currency': 'usd',
                'order': 'market_cap_desc',
                'per_page': limit,
                'page': 1,
                'sparkline': 'false'
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            result = f"🏆 Top {limit} Cryptocurrencies:\n\n"
            
            for i, coin in enumerate(data, 1):
                name = coin['name']
                symbol = coin['symbol'].upper()
                price = coin['current_price']
                change = coin['price_change_percentage_24h'] or 0
                change_emoji = "📈" if change >= 0 else "📉"
                change_sign = "+" if change >= 0 else ""
                
                result += f"{i:2d}. {name} ({symbol}) - ${price:,.2f} {change_emoji} {change_sign}{change:.2f}%\n"
            
            return result
            
        except ValueError:
            return "❌ Please enter a valid number. Example: 'top 5'"
        except Exception as e:
            return f"❌ Error fetching top coins: {str(e)}"
    
    def get_trending(self, args=None):
        """Get trending cryptocurrencies"""
        try:
            url = f"{self.base_url}/search/trending"
            
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            result = "🔥 Trending Cryptocurrencies:\n\n"
            
            for i, coin in enumerate(data['coins'], 1):
                coin_data = coin['item']
                name = coin_data['name']
                symbol = coin_data['symbol']
                rank = coin_data['market_cap_rank']
                
                result += f"{i}. {name} ({symbol}) - Rank #{rank}\n"
            
            return result
            
        except Exception as e:
            return f"❌ Error fetching trending coins: {str(e)}"
    
    def get_market_cap(self, coin_name):
        """Get detailed market information for a coin"""
        try:
            if not coin_name:
                return "❌ Please specify a coin name. Example: 'market bitcoin'"
            
            coin_id = coin_name.lower().replace(' ', '-')
            url = f"{self.base_url}/coins/{coin_id}"
            
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            name = data['name']
            symbol = data['symbol'].upper()
            price = data['market_data']['current_price']['usd']
            market_cap = data['market_data']['market_cap']['usd']
            volume = data['market_data']['total_volume']['usd']
            supply = data['market_data']['circulating_supply']
            rank = data['market_cap_rank']
            
            result = f"""
📊 {name} ({symbol}) Market Info:
• Rank: #{rank}
• Price: ${price:,.2f}
• Market Cap: ${market_cap:,.0f}
• 24h Volume: ${volume:,.0f}
• Circulating Supply: {supply:,.0f} {symbol}
            """
            return result.strip()
            
        except requests.exceptions.HTTPError:
            return f"❌ Coin '{coin_name}' not found. Please check the spelling."
        except Exception as e:
            return f"❌ Error fetching market data: {str(e)}"
    
    def compare_coins(self, args):
        """Compare two cryptocurrencies"""
        try:
            if not args or len(args.split()) < 2:
                return "❌ Please specify two coins. Example: 'compare bitcoin ethereum'"
            
            coins = args.split()
            coin1, coin2 = coins[0], coins[1]
            
            coin1_id = coin1.lower().replace(' ', '-')
            coin2_id = coin2.lower().replace(' ', '-')
            
            url = f"{self.base_url}/simple/price"
            params = {
                'ids': f"{coin1_id},{coin2_id}",
                'vs_currencies': 'usd',
                'include_24hr_change': 'true',
                'include_market_cap': 'true'
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if len(data) < 2:
                return f"❌ Could not find both coins. Please check the spelling."
            
            coin1_data = data[coin1_id]
            coin2_data = data[coin2_id]
            
            result = f"""
⚖️  {coin1.title()} vs {coin2.title()}:

{coin1.title()}:
• Price: ${coin1_data['usd']:,.2f}
• 24h Change: {coin1_data.get('usd_24h_change', 0):.2f}%
• Market Cap: ${coin1_data.get('usd_market_cap', 0):,.0f}

{coin2.title()}:
• Price: ${coin2_data['usd']:,.2f}
• 24h Change: {coin2_data.get('usd_24h_change', 0):.2f}%
• Market Cap: ${coin2_data.get('usd_market_cap', 0):,.0f}
            """
            return result.strip()
            
        except Exception as e:
            return f"❌ Error comparing coins: {str(e)}"
    
    def get_news_sentiment(self, args=None):
        """Get a global market overview from CoinGecko"""
        try:
            # Get global market data
            url = f"{self.base_url}/global"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            global_data = data['data']
            total_market_cap = global_data['total_market_cap']['usd']
            total_volume = global_data['total_volume']['usd']
            btc_dominance = global_data['market_cap_percentage']['btc']
            
            result = f"""
📰 Crypto Market Overview:
• Total Market Cap: ${total_market_cap:,.0f}
• 24h Volume: ${total_volume:,.0f}
• Bitcoin Dominance: {btc_dominance:.1f}%
• Active Cryptocurrencies: {global_data['active_cryptocurrencies']:,}
• Markets: {global_data['markets']:,}
            """
            return result.strip()
            
        except Exception as e:
            return f"❌ Error fetching market data: {str(e)}"
    
    def quit_bot(self, args=None):
        """Exit the chatbot"""
        return "👋 Thanks for using Crypto Chatbot! Goodbye!"
    
    def process_command(self, user_input):
        """Process user input and execute commands"""
        if not user_input.strip():
            return "❓ Please enter a command. Type 'help' for available commands."
        
        parts = user_input.strip().split()
        command = parts[0].lower()
        args = ' '.join(parts[1:]) if len(parts) > 1 else None
        
        if command in self.commands:
            return self.commands[command](args)
        else:
            return f"❓ Command '{command}' not recognized. Type 'help' for available commands."
    
    def run(self):
        """Main chatbot loop"""
        print("🚀 Welcome to Crypto Chatbot!")
        print("Type 'help' for available commands or 'quit' to exit.")
        print("-" * 50)
        
        while True:
            try:
                user_input = input("\n💬 You: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() == 'quit':
                    print("\n🤖 Bot:", self.quit_bot())
                    break
                
                response = self.process_command(user_input)
                print(f"\n🤖 Bot: {response}")
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ An error occurred: {str(e)}")

if __name__ == "__main__":
    bot = CryptoChatbot()
    bot.run()