def emoji_convertor(txt):
    words = message.split(' ')
    emoji_dict = {
        ':)': "😊",
        ':(': "😒"
    }
    output = ""
    for word in words:
        output = output + " " + emoji_dict.get(word, word)
    return output


message = input("Enter the message = ")
print(emoji_convertor(message))
