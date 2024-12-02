def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    

    def get_wordcount():
        words = file_contents.split()
        count = 0
        for word in words:
            count += 1
        return print(f"{count} words found in the document")

    get_wordcount()

    def character_count():
        character_dict = {}
        lowered_chars = file_contents.lower()
        for char in lowered_chars:
            if char in character_dict:
                character_dict[char] += 1
            else:
                character_dict[char] = 1
        return character_dict 

    counts_dict = character_count()

    def aggregate():
        for char in counts_dict:
            if char.isalpha():
                print(f"The {char} character was found {counts_dict[char]} times")
        return
    
    aggregate()

main()

    


