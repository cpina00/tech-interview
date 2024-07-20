"""
Teniendo una lista de palabras, se debe crear un programa que
devuelva verdadero o falso, verdadero cuando la palabra sea primera
vez que se encuentra en la lista, y falso cuando ya se encuentre
repetida. 
"""

def unique_word(words: list[str]) -> list[bool]:
    result = []
    for i in range(len(words)):
        value = True
        for j in range(i):
            if words[i] == words[j]:
                value = False
        result.append(value)
    return result
    """
    Aquí recorremos la lista y para cada elemento, contrastamos con los elementos
    anteriores si existe o no la palabra. de forma que si   
    esta forma de resolverlo, siendo la más intuitiva, es también muy costosa. su 
    complejidad es del orden O(n^2), por tanto, es posible cambiar la solución,
    utilizando un tipoi de datos más apropiado para esta tarea, una tabla hash o en
    python, un diccionario, que tiene coste de busqueda constante.
    """


def unique_word(words: list[str]) -> list[bool]:
    """
    con esta estructura, creamos un diccionario vacio, luego recorremos la lista.
    Por cada elemento, consultamos si existe en el diccionario, si existe, se marca
    Falso, y continuamos con la siguiente palabra. si no existe, marcamos Verdadero
    y lo agregamos al diccionario.
    
    De esta forma, solo hay que recorrer la lsta 1 vez para verificar lo solicitado,
    teniendo una complejidad O(n), mucho mejor que la solución anterior.
    """
    result = []
    unique_works = {}
    for word in words:
        if unique_works.get(word, False):
            result.append(False)
        else:
            unique_works[word] = 1
            result.append(True)
        
    return result



import unittest
class TestUniqueWord(unittest.TestCase):
    
    dataset = [
        ["a","b","c","d"],
        ["a","a","b","c"],
        ["a","b","b","c"],
        ["a","b","c","c"]
    ]
    expectations = [
        [True, True, True, True],
        [True, False, True, True],
        [True, True, False, True],
        [True, True, True, False]
    ]
    
    def test_input_void(self):
        data = []
        expected = []
        value = unique_word(data)
        self.assertEqual(value, expected)
    
    def test_dataset(self):
        for data, expectation in zip(self.dataset, self.expectations):
            with self.subTest():
                self.assertEqual(unique_word(data), expectation)
    
        
        
if __name__=="__main__":
    unittest.main()