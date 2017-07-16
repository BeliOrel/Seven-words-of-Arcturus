# import life_happens

class Witch:
    words = {
        1: {
            'Noctu Orfei Aude Fraetor': 'Strive for your ideal place.'
        },
        2: {
            'Phaidoari Afairynghor': 'That which is dreamed cannot be grasped, but work towards it, day after day, and you will find it in your hands.'
        },
        3: {
            'Arae Aryrha': 'Do not compare yourself with others, do what only you can do.'
        },
        4: {
            'Mayenab Dysheebudo': 'To see it through, patience is important.'
        },
        5: {
            'Sybilladura Lelladybura': 'When traditional and modern powers mingle, the gate to an unseen world will open.'
        },
        6: {
            'Lyonne': 'Thank you.'
        },
        7: {
            'Phasansheer Shearylla': 'Connect with other people, and your dream will grow.'
        }
    }

    def __init__(self,name):
        self.name = name
        self.number_of_revived_words = 0
        self.next_word = False
        self.next_word_string = None
        self.know_the_meaning_of_the_next_word = False
        self.revived_words = []

    def __str__(self):
        string = "\n-----\n"
        string += "Name: " + self.name + "\nNumber of revived words: " + str(self.number_of_revived_words) + "\n"
        string += "Know next word: " + str(self.next_word) + "\nNext word: " + str(self.next_word_string) + "\n"
        string += "Know the meaning of the next word: " + str(self.know_the_meaning_of_the_next_word) + "\nRevived words: "
        for word in self.revived_words:
            string += word + ", "
        string += "\n-----\n"
        return string

    def get_witch_name(self):
        return self.name

    def set_witch_name(self, name):
        self.name = name

    def get_number_of_revived_words(self):
        return self.number_of_revived_words

    def increase_number_of_revived_words(self):
        self.number_of_revived_words += 1

    def get_next_word(self):
        return self.next_word

    def switch_next_word(self):
        if self.next_word:
            self.next_word = False
        else:
            self.next_word = True

    def get_next_word_string(self):
        return self.next_word_string

    def set_next_word_string(self, string):
        self.next_word_string = string

    def check_next_word_string(self, string):
        for number,word in self.words.items():
            for key,value in word.items():
                if key.lower() == string.lower():
                    return 1
        return 0

    def reset_next_word_string(self):
        self.next_word_string = None

    def get_know_the_meaning_of_the_next_word(self):
        return self.know_the_meaning_of_the_next_word

    def switch_know_the_meaning_of_the_next_word(self):
        if self.know_the_meaning_of_the_next_word:
            self.know_the_meaning_of_the_next_word = False
        else:
            self.know_the_meaning_of_the_next_word = True

    def get_revived_words(self):
        return self.revived_words

    def set_revived_words(self):
        self.revived_words.append(self.next_word_string)

    def check_revived_words(self, string):
        for word in self.revived_words:
            if word.lower() == string.lower():
                print ("This word has already been revived!")
                return 0
        return 1

    def get_word_meaning(self, word):
        for number,pair in self.words.items():
            for key,value in pair.items():
                if key.lower() == word.lower():
                    return value
        return "No description for a given word!"

def main():
    name = input("Name of the witch: ")
    witch = Witch(name)

    while witch.get_number_of_revived_words() < 7:
        while not witch.get_next_word():
            # life_happens_the_next_word(witch)
            next_word = input("Write the searched word: ")
            while witch.check_next_word_string(next_word) < 1 or witch.check_revived_words(next_word) < 1:
                print("The word you wrote is duplicated or not one of the Seven Words of Arcturus!")
                next_word = input("Once again, write the searched word: ")

            witch.set_next_word_string(next_word)
            # change to True
            witch.switch_next_word()

        while not witch.get_know_the_meaning_of_the_next_word():
            # life_happens_the_meaning_of_the_next_word(witch)
            # This is a simple program, so no fancy logic for guessing the right meaning of the word
            right_meaning = input("Does " + witch.get_witch_name() + " know the right meaning of the next word? [y/n]")
            while not((right_meaning.lower() != "y" and right_meaning.lower() == "n") or (right_meaning.lower() != "n" and right_meaning.lower() == "y")):
                print("ERROR! You have to write y or n! So, once again.")
                right_meaning = input("Does she know the meaning of the next word? [y/n]")

            if right_meaning == "y":
                # change to True
                witch.switch_know_the_meaning_of_the_next_word()
                print("The meaning of the word {0}: {1}".format(witch.get_next_word_string(), witch.get_word_meaning(witch.get_next_word_string())))

        # Now, witch has to put the acquired info to the proper action
        info_used_in_proper_action = False
        while not info_used_in_proper_action:
            # life_happens_put_acquired_info_to_the_proper_action(witch)
            proper_action = input("Did " + witch.get_witch_name() + " use the acquired knowledge in real life situation? [y/n]")
            while not((proper_action.lower() != "y" and proper_action.lower() == "n") or (proper_action.lower() != "n" and proper_action.lower() == "y")):
                print("ERROR! You have to write y or n! So, once again.")
                proper_action = input("Did she use the acquired knowledge in real life situation? [y/n]")

            if proper_action == "y":
                witch.set_revived_words()
                witch.increase_number_of_revived_words()
                # change to False
                witch.switch_next_word()
                witch.switch_know_the_meaning_of_the_next_word()
                witch.reset_next_word_string()
                info_used_in_proper_action = True
                print(str(witch))

    # All the words are revived and thus the seal of Grand Triskellion is broken and ancient magic is released
    print("CONGRATULATIONS!\nYou have broken The Seal of Grand Triskellion and released the ancient magic :)")

if __name__ == '__main__':
    main()