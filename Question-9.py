class sol:
    def validity(self,str1):
        accum=[]
        parentheses={"(":")","[":"]","{":"}"}
        for i in str1 :
            if i in parentheses:
                accum.append(i)
            elif len(accum)==0 or parentheses[accum.pop()]!=i:
                return False
        return len(accum)==0
print(sol().validity("((("))