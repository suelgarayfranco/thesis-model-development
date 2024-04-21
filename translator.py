import random
import configClass

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
    equations = ' \\\\ \n'.join(terms)
    expression = '\\begin{cases}\n' + equations + '\n\\end{cases}'
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


# ==== Replacement functions for Variable Operands ====
def replaceVariableOperands(expression:str):

    realVariableCount = expression.count('VR')
    complexVariableCount = expression.count('VC')
    naturalVariableCount = expression.count('VN')
    irrationalVariableCount = expression.count('VI')
    decimalVariableCount = expression.count('VD')
    
    for _ in range(naturalVariableCount):
        randomNumber = random.randint(1,)
        #expression.replace('VN',  ,1)