from tkinter import *
from fuzzywuzzy import process
    
class gui():
     
    def __init__(self,t,all_words,contents):
        #from tkinter import *

        self.t=t
        self.cont=contents
        self.all_words=all_words
        self.choice=0
        self.c=0
        self.root=Tk()

        self.suggestionarr=[]
        self.suggestionarr2=[]
        self.suggestionarr3=[]
        self.suggestionarr4=[]
        self.root.geometry("1200x800")
        self.input_list=[]

        self.frame1=Frame(self.root)

        self.frame2=Frame(self.root)
        self.frame3=Frame(self.frame2)
        #self.frame3=Frame(self.root)
        #self.frame3.pack(side=BOTTOM)
        self.lab1=Label(self.frame2,text="INPUT/OUTPUT",bg="pink",fg="blue")
        self.lab1.pack(fill=X)

        self.inputstr=Text(self.frame2,width=115,bg='gray89',bd='2',cursor="pencil",fg='red',height=18,highlightbackground='blue',highlightcolor='green')
        self.inputstr.pack(side=TOP,fill=X)

        self.choose=Label(self.frame3,text="Choose One",bg="pink",fg="blue")
        self.choose.pack(side=LEFT,padx=20)

        self.entry1=Entry(self.frame3)#,width=15,bg='white',bd='2',cursor="pencil",fg='black',height=1,highlightbackground='blue',highlightcolor='green')
        self.entry1.pack(side=LEFT,padx=20)

        self.go=Button(self.frame3,text="GO",command=self.startit)
        self.go.pack(side=LEFT)



        self.frame21=Frame(self.frame1)
        self.frame22=Frame(self.frame1)
        self.frame23=Frame(self.frame1)
        self.frame24=Frame(self.frame1)

        self.frame21x=Frame(self.frame21)
        self.frame22x=Frame(self.frame22)
        self.frame23x=Frame(self.frame23)
        self.frame24x=Frame(self.frame24)

        #inputstr1=Text(self.frame21x,width=15,bg='white',bd='2',cursor="pencil",fg='black',height=1,highlightbackground='blue',highlightcolor='green')
        #inputstr1.pack(side=LEFT)
        self.submit1=Button(self.frame21x,text="TRIE",command=self.suggest_trie)
        self.submit1.pack(side=LEFT)

        self.suggestions=Text(self.frame21,width=25,bg='gray89',bd='2',cursor="pirate",fg='red',height=18,highlightbackground='blue',highlightcolor='green')
        self.suggestions.pack(side=BOTTOM)

        #inputstr2=Text(self.frame22x,width=15,bg='white',bd='2',cursor="pencil",fg='black',height=1,highlightbackground='blue',highlightcolor='green')
        #inputstr2.pack(side=LEFT)
        self.submit2=Button(self.frame22x,text="KMP",command=self.suggest_kmp)
        self.submit2.pack(side=LEFT)

        self.kmpsuggestions=Text(self.frame22,width=25,bg='gray89',bd='2',cursor="pirate",fg='red',height=18,highlightbackground='blue',highlightcolor='green')
        self.kmpsuggestions.pack(side=BOTTOM)

        #inputstr3=Text(self.frame23x,width=15,bg='white',bd='2',cursor="pencil",fg='black',height=1,highlightbackground='blue',highlightcolor='green')
        #inputstr3.pack(side=LEFT)
        self.submit3=Button(self.frame23x,text="SOUNDEX")
        self.submit3.pack(side=LEFT)

        self.output3=Text(self.frame23,width=25,bg='gray89',bd='2',cursor="pirate",fg='red',height=18,highlightbackground='blue',highlightcolor='green')
        self.output3.pack(side=BOTTOM)

        #inputstr4=Text(self.frame24x,width=15,bg='white',bd='2',cursor="pencil",fg='black',height=1,highlightbackground='blue',highlightcolor='green')
        #inputstr4.pack(side=LEFT)
        self.submit4=Button(self.frame24x,text="FUZZYWUZZY")
        self.submit4.pack(side=LEFT)

        self.output4=Text(self.frame24,width=25,bg='gray89',bd='2',cursor="pirate",fg='red',height=18,highlightbackground='blue',highlightcolor='green')
        self.output4.pack(side=BOTTOM)

        self.frame21.pack(side=LEFT,padx=20)
        self.frame22.pack(side=LEFT,padx=20)
        self.frame23.pack(side=LEFT,padx=20)
        self.frame24.pack(side=LEFT,padx=20)

        self.frame21x.pack(side=TOP,padx=20,pady=10)
        self.frame22x.pack(side=TOP,padx=20,pady=10)
        self.frame23x.pack(side=TOP,padx=20,pady=10)
        self.frame24x.pack(side=TOP,padx=20,pady=10)

        self.frame2.pack(side=TOP)
        self.frame1.pack()#side=BOTTOM)
        self.frame3.pack(pady=30)

        self.root.mainloop()


    def getinput(self):
        return(self.inputstr.get('1.0', END))

    def printsuggestions(self,index,word):
        #self.suggestionarr.append(word)
        self.suggestions.insert(END,str(index)+'  '+word+'\n')

    def printkmpsuggestions(self,index,word):
        self.kmpsuggestions.insert(END,str(index)+'  '+word+'\n')
        
    def printfuzzysuggestions(self,index,word):
        self.output4.insert(END,str(index)+'  '+word+'\n')

    def printoutput(self,word):
        self.input_list[self.c]=word
        input_string=' '.join(self.input_list)+'\n'
        self.inputstr.delete('1.0',END)
        self.inputstr.insert('1.0',input_string)
        self.c+=1
        

    def getchoice(self):
        return(self.entry1.get())

        
    def getsuggestions(self,i):
        self.suggestionarr=[]
        self.suggestionarr=self.t.search(i,self.suggestionarr)
        for p in range(len(self.suggestionarr)):
            self.printsuggestions(p+1,self.suggestionarr[p])

    def getkmpsuggestions(self):
       self.suggestionarr2=[]
       self.KMPSearch()
       if(len(self.suggestionarr2)==0):
            self.suggestionarr2.append('--------')
            #self.printkmpsuggestions(1,self.input_list[self.c])
       for i in range(len(self.suggestionarr2)):
           self.printkmpsuggestions(i+1,self.suggestionarr2[i])
            
            
    def getfuzzy():
        self.suggestionarr4=[]
        self.gate()
        for i in range(len(suggestionarr4())):
            self.printfuzzysuggestions(i+1,self.suggestionarr2[i])
        
       
    


    def startit(self):
        #self.output.delete('1.0',END)
        self.suggestions.delete('1.0',END)
        self.kmpsuggestions.delete('1.0',END)
        self.c=0
        input_string=self.getinput()
        input_string=input_string[:-1]
        self.input_list=input_string.split(' ')
        self.getsuggestions(self.input_list[self.c])
        self.getkmpsuggestions()
        self.getfuzzy()
        


    def again(self):
        #self.printoutput(self.suggestionarr[p-1])
        if(self.c<len(self.input_list)):
            self.getsuggestions(self.input_list[self.c])
            self.getkmpsuggestions()
            self.getfuzzy()

        
        


    def suggest_trie(self):
        p=self.getchoice()
        p=int(p)
        self.printoutput(self.suggestionarr[p-1])
        self.suggestions.delete('1.0',END)
        self.kmpsuggestions.delete('1.0',END)
        self.output3.delete('1.0',END)
        self.entry1.delete(0,END)
        self.again()

    
    def suggest_kmp(self):
        p=self.getchoice()
        p=int(p)
        self.printoutput(self.suggestionarr2[p-1])
        self.kmpsuggestions.delete('1.0',END)
        self.suggestions.delete('1.0',END)
        self.output3.delete('1.0',END)
        self.entry1.delete(0,END)
        self.again()
        
    def suggest_fuzzy(self):
        p=self.getchoice()
        p=int(p)
        self.printoutput(self.suggestionarr4[p-1])
        self.kmpsuggestions.delete('1.0',END)
        self.suggestions.delete('1.0',END)
        self.output3.delete('1.0',END)
        self.entry1.delete(0,END)
        self.again()
        
        

   

    def KMPSearch(self):
        pat=self.input_list[self.c]
        M = len(pat)
        #print(pat)
      
        lps = [0]*M 
        
      
        self.computeLPSArray(pat, M, lps) 
        #print(lps)
        
        for txt in self.all_words:
            #print(self.suggestionarr2)
            #print(txt)
            N = len(txt)
            j = 0
            i = 0
            while i < N :
                #print(i,j)
                if pat[j] == txt[i]: 
                    i += 1
                    j += 1
          
                if j == M: 
                    self.suggestionarr2.append(txt)
                    break
          
                elif i < N and pat[j] != txt[i]:
                    if j != 0: 
                        j = lps[j-1] 
                    else: 
                        i += 1
          
    def computeLPSArray(self,pat, M, lps): 
        len = 0 
      
        lps[0] 
        i = 1
      
        while i < M: 
            if pat[i]== pat[len]: 
                len += 1
                lps[i] = len
                i += 1
            else: 
                if len != 0: 
                    len = lps[len-1]
                    
                else: 
                    lps[i] = 0
                    i += 1
                    
    def gate():
        result=process.extract(self.input_list[self.c],self.cont,limit=20)
        for i in result:
            if(i[1]>75):
                self.suggestionarr4.append(i[0])
      



class TrieNode: 
      
    
    def __init__(self): 
        self.children = [None]*26
  
        
        self.isEndOfWord = False
  
class Trie: 
      
    
    def __init__(self): 
        self.root = self.getNode() 
  
    def getNode(self): 
      
        
        return TrieNode() 
  
    def _charToIndex(self,ch): 
          
          
        return ord(ch)-ord('a') 
  
  
    def insert(self,key): 
          
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
  
            if not pCrawl.children[index]: 
                pCrawl.children[index] = self.getNode() 
            pCrawl = pCrawl.children[index] 
  
        pCrawl.isEndOfWord = True
  
    def search(self, key,arr): 
          
        pCrawl = self.root 
        length = len(key)
        for level in range(length): 
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]: 
                arr.append(key)
                return (arr)
            pCrawl = pCrawl.children[index] 
  
        if(pCrawl.isEndOfWord):
            arr.append(key)
            return([key])
        
        elif(not pCrawl.isEndOfWord):
            for i in range(26):
                if(pCrawl.children[i]):
                    ch=chr(ord('a')+i)
                    s=self.search(key+ch,arr)
            return(arr)

            
                
                




  
def main():
    
    with open('dict.txt','r') as f:
        f_contents= f.read().split('\n')
        all_words=[i.lower() for i in f_contents]
  
    t = Trie() 

    for word in all_words: 
        t.insert(word)

    root=gui(t,all_words,f_contents)


if __name__ == '__main__': 
    main()
    
    

