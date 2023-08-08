dict = {
        'App': "An app, which is short for application, is a type of software that can be installed and run on a computer, tablet, smartphone or other electronic devices",
        'Accessibility': "Accessibility is the concept of whether a product or service can be used by everyone—however they encounter it.",
        'Adapter': "An adapter is a device that allows a specific type of hardware to work with another device that would otherwise be incompatible",
        'Abstraction': "An abstraction is a general concept or idea, rather than something concrete or tangible.",
        'Analog':"Analog is an adjective that describes a continuous measurement or transmission of a signal. It is often contrasted with digital, which is how computers store and process data using ones and zeros.",
        'Antivirus':"Antivirus software is a type of utility used for scanning and removing viruses from your computer.",
        'ASCII':"Stands for `American Standard Code for Information Interchange`. ASCII is a character encoding that uses numeric codes to represent characters. These include upper and lowercase English letters, numbers, and punctuation symbols.",
        'Autofill':"Autofill is a software function that automatically enters data in web forms and spreadsheets.",
        'Autocorrect':"Autocorrect is a software feature that corrects misspellings as you type.",
        'Avatar':"An avatar specifically refers to a character that represents an online user"

}

# sorted_dict_computer = sorted(dict.keys())
for keys in sorted(dict.keys()):
    print(keys)

print(":Options are present below:")
option = input("Write your option: ")
def search_word():
    print("Search")
    word_search = print(dict[str(input("Enter the word:\n"))])
    # word_search_output = print(dict[word_search]) # option ⌥
if option == "search word":
    search_word()
