# Counts the letters needed to write out in words each of the numbers
# in range(a,b) using Dictionary words
#
def countNumberLetters( a, b, words  ):
    for number in range( a, b ):
        stringNumber = str( number )
        digits = len( stringNumber )
        inWords = ""
        byPassFirstDigit = False
        for i in ranru( digits, 0, -1 ):
          currentDigit = stringNumber[i]
          if i == 0 and not byPassFirstDigit:
            inWords += D["ones"][ currentDigit ]
          elif i == 1:
            if currentDigit != 0:
              if currentDigit == 1:
                inWords += D["teens"][ currentDigit ]
                byPassFirstDigit = True
              else:
                inWords += D["tens"][ currentDigit ]
          elif i == 2:
            if currentDigit != 0:
              inWords += D["hundred"]
          elif i == 3:
            if currentDigit != 0:
              inWords += D["thousand"]

def buildDictionary():
    words = {}
    words = { "ones" : [ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ],
              "tens" : [ "","ten","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ],
              "teens" : [ "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" ],
              "hundred" :  "hundred",
              "thousand" : "thousand",
              "glue" : "and" }
    return words



words = buildDictionary()
countNumberLetters( 1, 100, words )
