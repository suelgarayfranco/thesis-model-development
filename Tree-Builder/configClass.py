from typing import Optional
from enum import Enum
from dataclasses import dataclass
import json

class ExpressionType(Enum):
    POLYNOMIAL = 'polynomial'
    SYSTEM_OF_EQ = 'system_of_esq'

@dataclass
class TreeSystemsConfig:
    variables: list[str]    
    is_complete: bool
    sign: str
    both_sides: bool
    is_ordered: bool
    num_unknowns: int
    num_equations: int         
    homogeneous: bool

@dataclass
class TreePolynomialsConfig:
    variables: list[str]
    degree: Optional[int]      
    max_degree: int       
    is_complete: Optional[bool]
    order: Optional[str]
    sign: str

@dataclass
class TreeCoefficientsConfig:
    real: bool
    complex: bool
    natural: bool
    irrational: bool
    fractional:bool
    decimal:bool


@dataclass
class Configuration():
    expression_type: ExpressionType
    num_expressions: int
    coefficients: TreeCoefficientsConfig
    polynomials: Optional[TreePolynomialsConfig]
    systems: Optional[TreeSystemsConfig]


configJson = json.load(open('config.json'))

config = Configuration(
    expression_type=ExpressionType[configJson['expression_type']],
    num_expressions=configJson['num_expressions'],
    coefficients=TreeCoefficientsConfig(
        real=configJson['coefficients']['real'],
        complex=configJson['coefficients']['complex'],
        irrational=configJson['coefficients']['irrational'],
        fractional=configJson['coefficients']['fractional'],
        decimal=configJson['coefficients']['decimal'],
        natural=configJson['coefficients']['natural'],
    ),
    polynomials=None,
    systems=None
)

if (config.expression_type == ExpressionType.POLYNOMIAL):
    config.polynomials = TreePolynomialsConfig(
        variables=configJson['polynomials']['variables'],
        max_degree=configJson['polynomials']['max_degree'],
        degree=configJson['polynomials']['degree'],
        is_complete=configJson['polynomials']['is_complete'],
        sign=configJson['polynomials']['sign'],
        order=configJson['polynomials']['order'],
    )
elif (config.expression_type == ExpressionType.SYSTEM_OF_EQ):
    config.systems = TreeSystemsConfig(
        variables = configJson['systems']['variables'],    
        is_complete = configJson['systems']['is_complete'], 
        sign = configJson['systems']['sign'], 
        both_sides = configJson['systems']['both_sides'], 
        is_ordered = configJson['systems']['is_ordered'],
        num_unknowns = configJson['systems']['num_unknowns'],
        num_equations = configJson['systems']['num_equations'],        
        homogeneous = configJson['systems']['homogeneous'],
    )


