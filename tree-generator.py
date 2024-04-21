from configClass import config, ExpressionType
from dictionaries import isNaryOperator, NaryOperators, getRandomNaryOperator, getRandomVariableOperand
import random
import numpy as np
import csv
import pandas as pd

def removeRandomTerm(terms, degree, order):
    if order == "desc":
        to_delete = random.randint(1,len(terms)-1)
    elif order == "asc":
        to_delete = random.randint(0,len(terms)-2)
    else:
        to_delete = random.randint(0,len(terms)-1)
        while terms[to_delete] == degree:
            to_delete = random.randint(0,len(terms)-1)

    terms.pop(to_delete)


def generate_polynomial_term(variable, degree, coefficients,isNegative):

    coef = getRandomVariableOperand(coefficients=coefficients)
    
    term = []
    if degree == 0:
        term = [coef.name]
    elif degree == 1:
        term = ['MUL', coef.name, variable, 'E']
    else:
        term = ['MUL', coef.name, 'POW', variable, f'{degree}','E']
    
    if (isNegative):
        term.insert(0,'NEG')

    return term


def generate_polynomial(variable, degree, is_complete, order, coefficients, sign):

    pol = ["SUM"]

    terms:list = np.arange(start=0, stop=degree+1).tolist()
    
    if order == 'desc':
        terms = terms[::-1]
    elif order == None:
        np.random.shuffle(terms)
    
    if not is_complete:
        if degree == 1:
            terms = [1]
        else:
            count_to_delete = random.randint(1,len(terms)-1)
            for _ in range(count_to_delete):
                removeRandomTerm(terms, degree, order) 
    
    for x in terms:
        if sign == 'mixed':
            isNegative = random.choice([True,False])
        elif sign == 'negative':
            isNegative = True
        else:
            isNegative = False

        term = generate_polynomial_term(variable=variable ,degree=x, coefficients=coefficients, isNegative=isNegative)
        pol.extend(term)
            
    pol.append('E')

    return pol


def generate_equation_term(variable, coefficients, is_negative):

    coef = getRandomVariableOperand(coefficients=coefficients)
    
    term = ["MUL", coef.name, variable, "E"]
    
    if (is_negative):
        term.insert(0,'NEG')

    return term

def generate_linear_expresion(variables, coefficients, sign):
    expression = []
    for var in variables:
        if sign == 'mixed':
            isNegative = random.choice([True,False])
        elif sign == 'negative':
            isNegative = True
        else:
            isNegative = False
    
        term = generate_equation_term(variable=var, coefficients=coefficients, is_negative=isNegative)
        expression.extend(term)
    if len(variables) > 0:
        expression.insert(0,"SUM")
        expression.append("E")
    return expression

def generate_sys_of_eq(variables:list, coefficients, num_unkn, num_eq, homogeneous, sign, is_complete, is_ordered, both_sides):

    system = ["CASES"]
    
    np.random.shuffle(variables)

    for _ in range(num_eq):
        available_vars = variables.copy()
        equation = ["EQ"]

        if not is_ordered:
            np.random.shuffle(available_vars)

        if not is_complete:
            for _ in range(random.randint(0,len(available_vars) - 1)):
                available_vars.pop(random.randint(0,len(available_vars) - 1))

        if not both_sides:
            if homogeneous:
                right_side = ["0"]
            else:
                right_side = [getRandomVariableOperand(coefficients=coefficients).name]
            
            left_side = generate_linear_expresion(variables=available_vars, coefficients=coefficients, sign=sign)

        else:
            random_split_pt = random.randint(0,len(available_vars) - 1)
            left_side_vars = available_vars[:random_split_pt]
            right_side_vars = available_vars[random_split_pt:]

            left_side = generate_linear_expresion(variables=left_side_vars, coefficients=coefficients, sign=sign)
            right_side = generate_linear_expresion(variables=right_side_vars, coefficients=coefficients, sign=sign)

            independent_term = getRandomVariableOperand(coefficients=coefficients).name

            if len(left_side_vars) == 0:
                left_side.insert(-1,independent_term)
            else:
                right_side.insert(-1,independent_term)

        equation.extend(left_side)
        equation.extend(right_side)

        system.extend(equation)    

    system.append("E")

    return system

def generate_trees():
    trees = []

    if config.expression_type == ExpressionType.POLYNOMIAL:
        params = config.polynomials

    elif config.expression_type == ExpressionType.SYSTEM_OF_EQ:
        params = config.systems
        
    for _ in range(config.num_expressions):
        tree = []
        if config.expression_type == ExpressionType.POLYNOMIAL:
            tree = generate_polynomial(
                variable=params.variables[0],
                degree= params.degree if params.degree else random.randint(1, params.max_degree), 
                is_complete= params.is_complete,
                order=params.order,
                coefficients=config.coefficients,
                sign=params.sign
            )
        elif config.expression_type == ExpressionType.SYSTEM_OF_EQ:
            tree = generate_sys_of_eq(
                variables=params.variables,
                num_unkn=params.num_unknowns,
                num_eq=params.num_equations,
                homogeneous=params.homogeneous,
                sign=params.sign,
                is_complete=params.is_complete,
                is_ordered=params.is_ordered,
                both_sides=params.both_sides,
                coefficients=config.coefficients
            )

        trees.append(tree)

    return trees

# UNCOMMENT to generate trees and insert in file

trees = [[','.join(tree)] for tree in generate_trees()]

with open('expressions/sys_9/expressions_sys_9.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerows(trees)


#print(generate_trees())
