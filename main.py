import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()
print(f'{Fore.CYAN} Hi!, welcome to Sentiment Spy')
user_name = input(f"{Fore.RED} Please enter your name.")
if not user_name:
    user_name="Mystery Agent"
convo_hist=[]
print(f'\n{Fore.CYAN}Hello, {user_name}!')
print("\nType a sentence and i will analyze your mood with my AI!")
print("\nType 'reset', 'history', or 'exit' to quit")

running=True
while running==True:
    user_input=input(f'{Fore.GREEN} >> {Style.RESET_ALL}').strip()
    if not user_input:
        print("Enter some text for the conversation to continue")
        continue
    if user_input.lower()=='exit':
        print(f"Good bye, {user_name}.")
    elif user_input.lower()=='reset':
        print(f"All conversations have been deleted.")
        continue
    elif user_input.lower()=='history':
        if not convo_hist:
            print("There hasn't been any conversation yet.")
        else:
            print("Conversation history")
            for idx, (text, polarity, sentiment_type) in enumerate(convo_hist, start=1):
                if sentiment_type=='Positive':
                    color=Fore.GREEN
                    emoji="😀"
                if sentiment_type=='Negative':
                    color=Fore.RED
                    emoji="😔"
                else:
                    color=Fore.YELLOW
                    emoji='😐'
                print(f'{idx}.{color}{emoji} {text}'
                f'(Polarity: {polarity: 2f}, {sentiment_type}){Style.RESET_ALL}')
        continue

    polarity=TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type='Positive'
        color=Fore.GREEN
        emoji='😀'
    elif polarity < -0.25:
        sentiment_type='Negative'
        color=Fore.RED
        emoji='😔'
    else:
        sentiment_type='Neutral'
        color=Fore.YELLOW
        emoji='😐'

    convo_hist.append((user_input,polarity,sentiment_type))

    print(f'{color}{emoji} {sentiment_type} sentiment detected!')


