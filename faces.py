def main():
    text=input("Write a sentence: ")
    text = change(text)
    print(text, end=" ")

def change(text):
    text=text.replace(":)", "🙂").replace(":(","🙁")
    return text;


main()
