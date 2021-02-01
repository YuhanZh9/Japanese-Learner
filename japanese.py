class Character:
    """
    Information about a Japanese character.
    
    Attributes:

    __hiragrana:
        a string

    __katakana:
        a string

    __romaji:
        a string

    __timewrong:
        an integer
    """
    def __init__(self, hiragana, katakana, romaji):
        """Creates a character with given hiragana, katakana, and romaji

        Character, str, str, str -> None"""
        self.__hiragana = hiragana
        self.__katakana = katakana
        self.__romaji = romaji
        self.__timewrong = 0

    def __repr__(self):
        """returns a string in the form of Character(hiragana, katakana, romaji)

        Character -> str"""
        return "Character('" + self.__hiragana + "', '" +\
               self.__katakana + "', '" + self.__romaji +\
               "')"
    def __str__(self):
        """returns a strng in the format of 'hiragana, katakana, romaji'

        Character -> str"""
        return self.__hiragana + ', ' +\
               self.__katakana + ', ' +\
               self.__romaji
    def getHiragana(self):
        """returns the hiragana for the character

        Character -> str"""
        return self.__hiragana
    
    def getKatakana(self):
        """returns the katakana for the character

        Character -> str"""
        return self.__katakana

    def getRomaji(self):
        """returns the romaji for the character

        Character -> str"""
        return self.__romaji

    def getTimewrong(self):
        """returns the romaji for the character

        Character -> num"""
        return self.__timewrong
    
    def addTimewrong(self):
        """increases the timewrong by 1

        Character -> None"""
        self.__timewrong += 1

    def __gt__(self, other):
        """returns True if self has a larger time wrong than other

        Character, Character -> bool"""
        return self.__timewrong > other.__timewrong
    
    def __cmp__(self, other):
        """returns True if self has same time wrong than other

        Character, Character -> bool"""
        return self.__timewrong == other.__timewrong
    
    def __lt__(self, other):
        """returns True if self has a smaller time wrong than other

        Character, Character -> bool"""
        return self.__timewrong < other.__timewrong
    
        
class Set:
    """
    Information about a set that contains Japanese chracters.

    Attributes:

    __characters:
        a list of Character

    __userid (the user the set is for):
        a string
    """

    def __init__(self, userid, characters = None):
        """creates a set with the given list of Characters and userid

        Set, str, list -> None"""
        hiragana = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん']
        katakana = ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス', 'セ', 'ソ', 'タ', 'チ', 'ツ', 'テ', 'ト', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ', 'マ', 'ミ', 'ム', 'メ', 'モ', 'ヤ', 'ユ', 'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン']
        romaji = ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko', 'sa', 'si/shi', 'su', 'se', 'so', 'ta', 'ti/chi', 'tu/tsu', 'te', 'to', 'na', 'ni', 'nu', 'ne', 'no', 'ha', 'hi', 'hu/fu', 'he', 'ho', 'ma', 'mi', 'mu', 'me', 'mo', 'ya', 'yu', 'yo', 'ra', 'ri', 'ru', 're', 'ro', 'wa', 'wo','n']
        if characters == None:
            characters = []
            for i in range(46):
                characters.append(Character(hiragana[i], katakana[i], romaji[i]))
                self.__characters = characters
        
        self.__characters = characters
        self.__userid = userid

    def __repr__(self):
        """returns a string in the form Set(userid, characters)

        Set -> str"""
        string = '['
        for char in self.__characters:
            string += repr(char)
            string += ', '
        string += ']'
        return "Set('" + self.__userid + "', " + string + ")"
        
    def getCharacters(self):
        """returns the list of Characters the Set has

        Set -> list"""
        return self.__characters

    def addCharacters(self, char):
        """adds a Character to the list of Characters

        Set, Character -> None"""
        self.__characters.append(char)

    def removeCharacters(self, char):
        """removes a Character to the list of Characters

        Set, Character -> None"""
        self.__character.remove(char)
        
class User:
    """
    Information about a user that takes the Japanese characters test.

    Attributes:
    __userid:
        a string

    __testedcharacters:
        a list of Character
    """
    def __init__(self, userid, testedcharacters = None):
        """creates a user witht the given userid and tested Characters

        User, str, list -> None"""
        self.__userid = userid
        if testedcharacters == None:
            self.__testedcharacters = []
        else:
            self.__testedcharacters = testedcharacters
        
    def __repr__(self):
        """returns a string in the form of User(userid, testedcharacters)

        User -> str"""
        string = '['
        for char in self.__testedcharacters:
            string += repr(char)
            string += ', '
        string += ']'
        return "User('" + userid + "', " + string + ')'

    def getTestedcharacters(self):
        """returns the list of tested Characters the user has

        User -> str"""
        return self.__testedcharacters

    def addTestedcharacters(self, char):
        """adds the given Character into the testedcharacters

        User, Character -> None"""
        self.__testedcharacters.append(char)

    def getUserid(self):
        """returns the user id of the user

        User -> str"""
        return self.__userid
