"""You can use this class to represent how classy someone or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase your "classiness".
1) Create a function in "Classy" that takes a string as input and 
2) adds it to the "items" list.
Another method should calculate the "classiness" value based on the items.
The following items have classiness points associated with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""


class Classy(object):
    def __init__(self):
        self.items = []
        self.score = 0
    
    def getClassiness(self):
        return self.score
    
    def addItem(self, newItem):
        if newItem=="tophat":
            self.score +=2
        elif newItem=="bowtie":
            self.score +=4
        elif newItem == "monocle":
            self.score +=5
        else:
            self.score +=0
        self.items.append(newItem)

def main():
    print("Hello World!")
    # Test cases
    me = Classy()

    # Should be 0
    score2 = me.getClassiness()
    print("Score: "+str(score2))

    me.addItem("tophat")
    # Should be 2
    score2 = me.getClassiness()
    print("Score: " + str(score2))

    me.addItem("bowtie")
    me.addItem("jacket")
    me.addItem("monocle")
    # Should be 11
    score2 = me.getClassiness()
    print("Score: " + str(score2))

    me.addItem("bowtie")
    # Should be 15
    score2 = me.getClassiness()
    print("Score: " + str(score2))


if __name__ == "__main__":
    main()