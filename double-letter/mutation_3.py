def double_letter(word):
    '''
        Change count condition,
        looking at the wrong consonant
    '''
    consonants = "bcdfghjklpmntrqsvwxyzBCDFGHJKLMNPQRSTVWXYZ"  
    consonant_count = 0 
    result = list(word) 

    for i in range(len(result)):
        if result[i] in consonants:
            consonant_count += 1
            if consonant_count == 3: # Mutation looking for the third consonant instead of the second consonant
                result[i] = result[i] * 2 
                break 
    return "".join(result) 