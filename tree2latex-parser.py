from dictionaries import isBinaryOperator, isNaryOperator, isUnaryOperator, isFinishOperand, isOperand, isOperator, NaryOperators, BinaryOperators, UnaryOperators,computeString
import pandas as pd

def parse_and_complete_tree(treeString:str):
    tree = treeString.split(',')
    expression:str = ''
    while (len(tree) != 0):
        node = tree.pop(0)
        if isOperator(node):
            expression += solveOperator(tree, node)
        elif isOperand(node):
            expression += node
        else:
            raise Exception('ERROR: Expression parsing failure')
        
    return expression


def solveOperator(tree, operator):
    if isNaryOperator(operator):
        return solveNaryOperator(tree, NaryOperators[operator])
    elif isBinaryOperator(operator):
        return solveBinaryOperator(tree, BinaryOperators[operator])
    elif isUnaryOperator(operator):
        return solveUnaryOperator(tree, UnaryOperators[operator])
    else:
        raise Exception('ERROR: NOT an Operator')


def solveNaryOperator(tree:list, operator):
    terms = []
    foundEnd = False

    while (len(tree) != 0 and (not foundEnd)):
        node = tree.pop(0)

        if isFinishOperand(node):
            foundEnd = True
        elif isOperand(node):
            terms.append(node)
        elif isOperator(node):
            terms.append(solveOperator(tree,node))
        else:
            raise Exception('ERROR: solving n-ary Operator')      
    return computeString(operator,terms)


def solveBinaryOperator(tree, operator):
    terms = []
   
    while (len(tree) != 0 and len(terms) < 2):
        node = tree.pop(0)

        if isOperand(node):
            terms.append(node)
        elif isOperator(node):
            terms.append(solveOperator(tree,node))
        else:
            raise Exception('ERROR: solving binary Operator')      
    return computeString(operator,terms)


def solveUnaryOperator(tree, operator):

    term = ''

    node = tree.pop(0)

    if isOperand(node):
        term = node
    elif isOperator(node):
        term = solveOperator(tree,node)
    else:
        raise Exception('ERROR: solving unary Operator')      
    
    return computeString(operator,term)


expression = ','.join(['CASES', 'EQ', 'SUM', 'MUL', 'VC', 'y', 'E', 'E', '0', 'EQ', 'SUM', 'MUL', 'VF', 'z', 'E', 'MUL', 'VN', 'y', 'E', 'NEG', 'MUL', 'VF', 'x', 'E', 'E', '0', 'EQ', 'SUM', 'NEG', 'MUL', 'VN', 'x', 'E', 'NEG', 'MUL', 'VC', 'y', 'E', 'E', '0', 'E'])

print(parse_and_complete_tree("CASES,EQ,SUM,NEG,MUL,VN,y,E,NEG,MUL,VN,x,E,E,VN,EQ,SUM,MUL,VF,x,E,NEG,MUL,VF,y,E,E,VN,E"))

# UNCOMMENT to translate trees to pseudolatex and insert in file
'''
df = pd.read_csv("tree-expressions.csv", header=None, sep=';')
df.columns = ['tree']
df.drop_duplicates()
df['pseudolatex'] = df['tree'].apply(parse_and_complete_tree)

df.to_csv('polynomials-pseudolatex.csv', sep=';')


df = pd.read_csv("polynomials-pseudolatex.csv", sep=';')

n = 30
list_df = [df['pseudolatex'][i:i+n] for i in range(0,len(df), n)]

for idx, x in enumerate(list_df):
    x.to_csv(f'polynomials-pseudolatex-{idx}.csv', sep=';')
'''