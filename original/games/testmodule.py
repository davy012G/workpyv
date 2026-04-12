import random as r

#Glory be to God
def subject_of_formula(relation, formula):# Update.DPJE_soft
    """This function changes different series of
    formulas by making an object in that expression or formula
    the subject through some mathemactical procedures.
    """
    #follow BODMAS
    pass

class English:

    def __init__(self) -> None:
        """This class is designed to reduce the stress of dealing with
        English in computer..."""
        pass

    def singular_plural(self, sentence: str, singular: str, plural: str) -> str:
        if sentence.find("1") != -1 or sentence.find("one") != -1 or sentence.find("0") != -1 or sentence.find("Zero") != -1:
            #Then replace the plural word in the sentence for the singular word
            newsentence = sentence.replace(f"{plural}",f"{singular}")
            new_sentence = newsentence.replace("are","is")
            return new_sentence
        else:
            return sentence

#Test area
diary = ["cow", "milk","farm","goat","sheep","milking_machine"]
extracts = ["carrot","cucumber","apple","olive","banana","orange","vanilla"]
def test_function():
    for w in diary:
        for i in diary:
            print(w,":",i)
    for s in extracts:
        print(s,":",s)

test_function()