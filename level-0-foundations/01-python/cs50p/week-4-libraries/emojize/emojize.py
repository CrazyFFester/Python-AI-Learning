import emoji

emoji_text = input("Input: ")
emoji = emoji.emojize(emoji_text, language='alias')

print(f"Output: {emoji}")
