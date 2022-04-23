class NodoArbol:
    def __init__(self, value, left=None, right=None):
        self.data = value
        self.left = left
        self.right = right

def preorder(elem):
    if elem != None:
        print(elem.data , " ", end="")
        preorder(elem.left)
        preorder(elem.right)

def postorden(elem):
    if elem != None:
        postorden(elem.left)
        postorden(elem.right)
        print(elem.data, " ", end="")

def inorden(elem):
    if elem != None:
        inorden(elem.left)
        print(elem.data, " ", end="")
        inorden(elem.right)

def main():
    print("\t\tArbol #1")
    arbolT1=NodoArbol("+",NodoArbol("-",NodoArbol(5),NodoArbol(4)),NodoArbol("*",NodoArbol(3),NodoArbol(2)))
    print("Infija o Inorden")
    inorden(arbolT1)
    print("\nPrefija o Preorden")
    preorder(arbolT1)
    print("\nPosfija o Postorden")
    postorden(arbolT1)
    print("\n\t\tArbol #2")
    arbolT2=NodoArbol(40,NodoArbol(30,NodoArbol(25),NodoArbol(35)),NodoArbol(50,NodoArbol(45),NodoArbol(60)))
    print("Infija o Inorden")
    inorden(arbolT2)
    print("\nPrefija o Preorden")
    preorder(arbolT2)
    print("\nPosfija o Postorden")
    postorden(arbolT2)

main()