def valueDictFunc():
    global values, numOfValues
    values = {
            'PPG':[],
            'REB':[],
            'AST':[],
            'STL':[],
              
        }
    numOfValues = len(values)

valueDictFunc()

# REMOVE AFTER RELEASE TEST ONLY
givenNumber = 22.3
givenNumber2 = 5.2
givenNumber3 = 1.4
givenNumber4 = 0.4

def valueDictUpdate():
    values.update({'PPG':givenNumber})
    values.update({'REB':givenNumber2})
    values.update({'AST':givenNumber3})
    values.update({'STL':givenNumber4})



