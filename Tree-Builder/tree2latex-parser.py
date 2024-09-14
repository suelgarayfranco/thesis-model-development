from dictionaries import isBinaryOperator, isNaryOperator, isUnaryOperator, isFinishOperand, isOperand, isOperator, NaryOperators, BinaryOperators, UnaryOperators,computeString
import pandas as pd
import glob
import json
from translator import replaceVariableOperands

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


# UNCOMMENT to translate trees to pseudolatex and insert in file
'''
df = pd.read_csv("tree-expressions.csv", header=None, sep=';')
df.columns = ['tree']
df.drop_duplicates()
df['pseudolatex'] = df['tree'].apply(parse_and_complete_tree)

df.to_csv('polynomials-pseudolatex.csv', sep=';')

'''

'''
files = glob.glob('./expressions/**/expressions_sys_*.csv', recursive=True)

for x in files:
    tree_df = pd.read_csv(x, header=None, names=['tree'])
    group = x.split('/')[2].split('_')[1]

    pseudolatex_df = tree_df['tree'].apply(parse_and_complete_tree)

    pseudolatex_df.to_csv(f'./expressions/psudolatex_{group}.csv', header=None, index=None)
'''

'''
configJson = json.load(open('replacer-config.json'))

df = pd.read_csv('./expressions/sys_11/psudolatex_11.csv', names=['pseudolatex'])

df['latex'] = df['pseudolatex'].apply(lambda x: replaceVariableOperands(x, configJson.get('coefficients')))

df['latex'].to_csv('./expressions/sys_11/latex_11.csv', index=None, header=None)
'''

