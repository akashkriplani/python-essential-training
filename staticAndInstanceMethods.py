# Static and Instance methods

# These can be called by ClassName.staticMethodName
# In this case, WordSet.cleanText(text)
# Alternatively, they can be called by using @staticmethod decorator
# and using self.staticMethodName (in this case, self.cleanText(text))
# or can simply be called as WordSet.cleanText()

# Instance methods are dependent on the instance being called like wordSet below
# addText is an instance method

class WordSet:
    removePuncs = ['!', '.', ',', '\'']
    def __init__(self):
        self.words = set()
    
    # addText is an instance method
    def addText(self, text):
        # Alternatively, we can call WordSet.cleanText(text)
        # We can remove @staticmethod or include it while using WordSet.cleanText
        # But, if we are using self.cleanText, we need to add @staticmethod
        text = self.cleanText(text)
        for word in text.split():
            self.words.add(word)

    # If we do not want to use self as a parameter in the clean text method we can exclude it.
    # If we exclude it, we need to make sure to add the @staticmethod decorator or call the method
    # directly as WordSet.cleanText(text)
    @staticmethod
    def cleanText(text):
        for punc in WordSet.removePuncs:
            text = text.replace(punc, '')
        return text.lower()
    
wordSet = WordSet()
wordSet.addText('Hi, I\'m Akash! Here is a sentence I want to add!')
wordSet.addText('Here is another sentence I want to add.')

print(wordSet.words)
