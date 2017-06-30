class Node:
    def __init__(self):
        self.eof=False
        self.child=dict()


class Cache:
    def __init__(self,node):
        self.prevstring=""
        self.prevnode=node



class Trie:

    def __init__(self):
        self.head=Node()
        self.results=[]
        self.cache=Cache(self.head)





    def insert(self,word):
        myhead=self.head

        for i in word:
            if i not in myhead.child:
                myhead.child[i]=Node()

            myhead=myhead.child[i]

        myhead.eof=True

    def word_exist(self,word):
        myhead=self.head

        for i in word:
            if i not in myhead.child:
                return False
            myhead=myhead.child[i]

        return myhead.eof==True

    def dfs_prefix(self,prefix):
        self.results=[]
        if prefix[:-1]==self.cache.prevstring and prefix[:-1]!="":
            myhead=self.cache.prevnode
            myprefix=prefix[-1]
            print("cache used")
        else:
            myhead = self.head
            myprefix=prefix

        for i in myprefix:
            if i not in myhead.child:
                return self.results
            myhead=myhead.child[i]

        self.cache.prevstring=prefix
        self.cache.prevnode=myhead

        self.dfs(myhead,prefix)

        return self.results

    def dfs(self,myhead,prefix):
        if myhead.eof==True:
            self.results.append(prefix)
            return

        for i in myhead.child.keys():
            self.dfs(myhead.child[i],prefix+i)
        return


