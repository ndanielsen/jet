"""
An analysis module for JET on gender. 

NLTK to be implemented in future versions.


Author:
Nathan Danielsen
nathan.danielsen@irex.org



Tip of hat for inspiration to : 
Ben Bengfort
https://github.com/bbengfort/gender-words-fatale
"""



import string
import time
import collections

class Gender(object):
    def __init___(self):
        pass

    @staticmethod
    def opentxt(filename):
        """
        Helper function to open a text file and returns data in lists by line
        """
        with open(filename) as f: # this opens the file
            data = f.readlines()

        return data

    @staticmethod
    def cleaner(data):
        """
        Takes lines of uncleaned text, lower cases, removes punctuation, splits and returns cleaned list
        """
        words = []
        for elem in data: #this goes through each elmenent in the list of lists
            elem = elem.lower() #turns all the text in the sublist into lower case
            elem = elem.translate(None, string.punctuation) #removes puncation and replaces it with None
            elem = elem.split() #splits up the sub list into most sub-sub lists --> [[["Sublist"], ["1"]],[["Sublist"], ["2"]]]
            for section in elem: #goes through each of the sub-sub lists
                words.append(section)
        return words
      
    @staticmethod
    def listtodic(data):
        """ 
        Takes a list of words and counts them into a dictionary like object. The key is the word and the value is the count of words in the list.
        """
        count = collections.Counter(data) #uses built in Collections counter tool
        return count


    @staticmethod
    def datatolist(data): ### REFACTOR TO takes sentences and returns a list of words
        """
        Takes a file, removes punctuation and returns a list of sentences.

        """
        pass
 
    @staticmethod
    def genderize(text):
        """
        Takes a list of cleaned words and returns the tuple count (male, female, neuter) of gendered words.
        

        REFACTOR to count lists and dicts

        """
        MALE_WORDS=set(['guy','spokesman','chairman',"men's",'men','him',"he's",'his',
                    'boy','boyfriend','boyfriends','boys','brother','brothers','dad',
                    'dads','dude','father','fathers','fiance','gentleman','gentlemen',
                    'god','grandfather','grandpa','grandson','groom','he','himself',
                    'husband','husbands','king','male','man','mr','nephew','nephews',
                    'priest','prince','son','sons','uncle','uncles','waiter','widower',
                    'widowers'])
        FEMALE_WORDS=set(['heroine','spokeswoman','chairwoman',"women's",'actress','women',
                "she's",'her','aunt','aunts','bride','daughter','daughters','female',
                'fiancee','girl','girlfriend','girlfriends','girls','goddess',
                'granddaughter','grandma','grandmother','herself','ladies','lady',
                'lady','mom','moms','mother','mothers','mrs','ms','niece','nieces',
                'priestess','princess','queens','she','sister','sisters','waitress',
                'widow','widows','wife','wives','woman'])
        MALE = 'male'
        FEMALE = 'female'
        UNKNOWN = 'unknown'
        BOTH = 'both'

        female = 0
        male = 0
        neuter = 0
        for word in text:
            if word in MALE_WORDS:
                #print word, "is a male word."
                male += 1
            elif word in FEMALE_WORDS:
                #print word, "is a female word."
                female += 1    
            else:
            	continue # print word, "is not gendered"
        return male, female, neuter

    def main(self, data):
        """
        Main constructor 
        """  
        pass



    def visual(self):
        """
        A simple gender visual of the most frequent gendered words used. 

        Probably use a simple word map for initial versions

        """
        pass


if __name__ == "__main__":

    test = Gender()
    

    #filename = wget.download("http://gutenberg.net.au/ebooks02/0200161.txt")
    
    filename = "0200161.txt"
    example = test.opentxt(filename)

    opened = test.cleaner(example)

    cleaned = test.listtodic(opened)

    print type(dict(cleaned))

    #print cleaned
    #print test.genderize(opened)