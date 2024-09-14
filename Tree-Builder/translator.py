import random
import json

# ==== Translation functions for NaryOperators ====
def translateSUM(terms:list):
    if len(terms) > 1:
        expression = ' + '.join(terms)
        expression = expression.replace('+ -','-')
    else:
        expression = terms[0]
    return expression

def translateMUL(terms:list):
    expression = '.'.join(terms)
    return expression

def translateCASES(terms:list):
    equations = ' \\\\ '.join(terms)
    expression = '\\begin{cases} ' + equations + ' \\end{cases}'
    return expression

# ==== Translation functions for BinaryOperators ====
def translatePOW(terms:list):
    expression = terms[0] + '^{' + terms[1] + '}'
    return expression

def translateSUB(terms:list):
    expression = terms[0] + '_{' + terms[1] + '}'
    return expression

def translateEQ(terms:list):
    expression = terms[0] + ' = ' + terms[1] 
    return expression

def translateSQRT(terms:list[str]):
    expression = ''

    if terms[1].isdecimal: 
        if int(terms[1]) != 2:
            expression = f'\sqrt[{terms[1]}]' + '{' + terms[0] + '}'
        else:
            expression = '\sqrt{' + terms[0] + '}'
        
    return expression


# ==== Translation functions for UnaryOperators ====
def translateNEG(term:str):
    expression = ''
    containsSumOp = term.find('+') != -1

    if containsSumOp:
        expression = f'- ({term})'
    else:
        expression = f'- {term}'

    return expression



def getRandomNatural(min, max):
    return str(random.randint(min, max))

def getRandomDecimal(min, max, decimals):
    return str(round(random.uniform(min, max), decimals))

def getRandomNaturalOrDecimal(min, max, decimals):
    is_decimal = random.choice([True,False])

    if is_decimal:
        return getRandomDecimal(min, max, decimals)
    
    return str(getRandomNatural(min, max))

def getRandomFractional(min, max):
    numerator = getRandomNatural(min,max)
    denominator = getRandomNatural(min,max)

    if denominator == 1: 
        denominator += 1

    return r'\frac{' + str(numerator) + r'}{' + str(denominator) + r'}'

def getRandomReal(min, max, minFrac, maxFrac, decimals):
    is_fractional = random.choice([True,False])

    if is_fractional:
        return getRandomFractional(minFrac, maxFrac)
    
    return str(getRandomNaturalOrDecimal(min,max,decimals))

def getRandomComplex(min, max):
    is_pure = random.choice([True,False])

    if is_pure:
        return f'{getRandomNatural(min, max)}i'
    
    return f'({getRandomNatural(min, max)}+{getRandomNatural(min, max)}i)'


# ==== Replacement functions for Variable Operands ====
def replaceVariableOperands(expression:str, config:dict):

    replacedExpression = expression

    realVariableCount = expression.count('VR')
    complexVariableCount = expression.count('VC')
    naturalVariableCount = expression.count('VN')
    irrationalVariableCount = expression.count('VI')
    decimalVariableCount = expression.count('VD')
    fractionalVariableCount = expression.count('VF')

    minNatural = config['natural']['min']
    maxNatural = config['natural']['max']
    minFrac = config['fractional']['min']
    maxFrac = config['fractional']['max']
    decimals = config['decimals']
    
    for _ in range(naturalVariableCount):
        randomNumber = getRandomNatural(minNatural, maxNatural)
        replacedExpression = replacedExpression.replace('VN',randomNumber,1)

    for _ in range(realVariableCount):
        randomNumber = getRandomReal(minNatural, maxNatural, minFrac, maxFrac, decimals)
        replacedExpression = replacedExpression.replace('VR',randomNumber,1)

    for _ in range(fractionalVariableCount):
        randomNumber = getRandomFractional(minFrac, maxFrac)
        replacedExpression = replacedExpression.replace('VF',randomNumber,1)
    
    for _ in range(decimalVariableCount):
        randomNumber = getRandomDecimal(minNatural, maxNatural, decimals)
        replacedExpression = replacedExpression.replace('VD',randomNumber,1)

    for _ in range(complexVariableCount):
        randomNumber = getRandomComplex(minNatural, maxNatural)
        replacedExpression = replacedExpression.replace('VC',randomNumber,1)

    return replacedExpression
