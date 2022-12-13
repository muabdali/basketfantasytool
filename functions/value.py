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

def valueDictUpdate(givenNumber,givenNumber2,givenNumber3,givenNumber4):
    values.update({'PPG':givenNumber})
    values.update({'REB':givenNumber2})
    values.update({'AST':givenNumber3})
    values.update({'STL':givenNumber4})



