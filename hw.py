from textblob import TextBlob
from colorama import Fore, Style, init
import time

init(autoreset=True)

conversation_history = []
sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}


def show_processing_animation():
    print("Analyzing", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print()


def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.25:
        sentiment = "positive"
        color = Fore.GREEN
    elif polarity < -0.25:
        sentiment = "negative"
        color = Fore.RED
    else:
        sentiment = "neutral"
        color = Fore.YELLOW

    sentiment_counts[sentiment] += 1
    conversation_history.append((text, sentiment, polarity))

    print(f"{color}Sentiment: {sentiment.upper()} (Score: {polarity:.2f}){Style.RESET_ALL}")


def execute_command(command):
    if command == "summary":
        print("\n📊 Sentiment Summary:")
        for key in sentiment_counts:
            print(f"{key.capitalize()}: {sentiment_counts[key]}")
    elif command == "reset":
        conversation_history.clear()
        for key in sentiment_counts:
            sentiment_counts[key] = 0
        print("✅ Data has been reset.")
    elif command == "history":
        if not conversation_history:
            print("No messages in history.")
        else:
            print("\n📝 Conversation History:")
            for i, (text, sentiment, score) in enumerate(conversation_history, 1):
                print(f"{i}. \"{text}\" => {sentiment.upper()} ({score:.2f})")
    elif command == "help":
        print("\n🔧 Available Commands:")
        print("summary - Show sentiment statistics")
        print("reset - Reset all data")
        print("history - Show past conversation")
        print("help - List all commands")
        print("exit - Exit the chatbot and save report")
    else:
        print("❓ Unknown command. Type 'help' for options.")


def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if name.isalpha():
            return name
        print("❌ Name must only contain letters. Try again.")


def save_summary(username):
    filename = f"{username}_sentiment_analysis.txt"
    with open(filename, "w") as file:
        file.write(f"Sentiment Analysis Report for {username}\n")
        file.write("-" * 40 + "\n")
        for key in sentiment_counts:
            file.write(f"{key.capitalize()}: {sentiment_counts[key]}\n")
    print(f"\n📁 Summary saved to {filename}")


def main():
    print("🎩 Welcome to Sentiment Spy!")
    username = get_valid_name()
    print(f"\nHello, {username}! I'm your Sentiment Spy chatbot.")
    print("Type a sentence to analyze its sentiment or type 'help' for commands.")

    while True:
        user_input = input("\n🗣️ You: ").strip()
        if not user_input:
            continue
        if user_input.lower() == "exit":
            print("🚪 Exiting Sentiment Spy...")
            save_summary(username)
            break
        elif user_input.lower() in ["summary", "reset", "history", "help"]:
            execute_command(user_input.lower())
        else:
            show_processing_animation()
            analyze_sentiment(user_input)


if __name__ == "__main__":
    main()
