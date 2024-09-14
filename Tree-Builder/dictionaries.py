from enum import Enum
from configClass import TreeCoefficientsConfig
import random
from translator import translateSUM, translateMUL, translatePOW, translateNEG, translateCASES, translateSUB, translateEQ, translateSQRT


class NaryOperators(Enum):
    SUM = {"toString":translateSUM}
    MUL = {"toString":translateMUL}
    CASES = {"toString":translateCASES}

class BinaryOperators(Enum):
    POW = {"toString":translatePOW}
    EQ = {"toString":translateEQ}
    SUB = {"toString":translateSUB}
    SQRT = {"toString":translateSQRT}

class UnaryOperators(Enum):
    NEG = {"toString": translateNEG}

class ControlOperands(Enum):
    E = {"name":"E"}

class VariableOperands(Enum):
    VR = {"name":"VR"}
    VD = {"name":"VD"}
    VN = {"name":"VN"}
    VI = {"name":"VI"}
    VC = {"name":"VC"}
    VF = {"name":"VF"}

class LiteralOperands(Enum):
    DOTS = {"name":"DOTS"}


# ====== BOOLEAN FUNCTIONS FOR TYPE CHECKING ======
def isNaryOperator(operator):
    return operator in NaryOperators._member_names_

def isBinaryOperator(operator):
    return operator in BinaryOperators._member_names_

def isUnaryOperator(operator):
    return operator in UnaryOperators._member_names_

def isOperator(arg):
    return isUnaryOperator(arg) or isBinaryOperator(arg) or isNaryOperator(arg)

def isOperand(arg):
    return not isOperator(arg)

def isFinishOperand(arg):
    return arg == ControlOperands.E.name




def computeString(operator, *args):
    return operator.value.get('toString')(*args)




# ====== FUNCTIONS FOR RANDOM VALUES ======

def getRandomOperator():
    match random.randint(1,3):
        case 1: return getRandomNaryOperator()    
        case 2: return getRandomBinaryOperator()
        case 3: return getRandomUnaryOperator()
        
def getRandomNaryOperator():
    nary_operators = NaryOperators._member_names_

    return NaryOperators[random.choice(nary_operators)]

def getRandomBinaryOperator():
    binary_operators = BinaryOperators._member_names_
    
    return BinaryOperators[random.choice(binary_operators)] 

def getRandomUnaryOperator():
    unary_operators = UnaryOperators._member_names_

    return UnaryOperators[random.choice(unary_operators)]

def getRandomVariableOperand(coefficients:TreeCoefficientsConfig):

    available = [attr for attr, value in coefficients.__dict__.items() if value]
    choice = random.choice(available)

    match choice:
        case 'natural': return VariableOperands.VN
        case 'real': return VariableOperands.VR
        case 'complex': return VariableOperands.VC
        case 'irrational': return VariableOperands.VI
        case 'decimal': return VariableOperands.VD
        case 'fractional': return VariableOperands.VF
