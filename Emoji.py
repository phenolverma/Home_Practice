message = input("Enter the message = ")
words = message.split(' ')
emoji = {
    ':)': "😊",
    ':(': "😒"
}
output = ""
for word in words:
    output = output + " " + emoji.get(word, word)
print(output)
