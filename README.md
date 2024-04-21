## Configuration JSON for Tree Generation

```json
{
    "expression_type": "polynomial"|"system-of-eq", 
    "coefficients": [            
        "real": true|false,
        "complex": true|false,
        "decimal": true|false,
        "irrational": true|false,
        "rational": true|false,
    ],
    "polynomials": {        //is used if expression_type = polynomial
        "variables": str[],
        "degree": int,              
        "max_degree": int,           
        "is_complete": true|false,
        "order": "asc"|"desc"|"none",
        "sign": "positive"|"negative"|"mixed"
    },
    "systems-of-eq": {      //is used if expression_type = system-of-eq
        "variables": str[],
        "num_unknowns": int,
        "num_equations": int,       
        "linearity": true|false,    
        "homogeneous": true|false,
        "sign": "positive"|"negative"|"mixed",
        "both_sides": true|false,
        "is_ordered": true|false
    },    
}
```
- `expression_type` The class of algebraic expression to be generated

- `coefficients` List with the possible number sets from which to generate the expression's coefficients. For every set there is a boolean value that enables or disables the corresponding set.

- `polynomials` Configuration parameters that apply when the equation type is set to *polynomial*.

    - `polynomials.variables` The list of variables form which to generate the unknowns of the polynomials. Each variable is defined with a string.

    - `polynomials.degree` Degree of the generated polynomials.

    - `polynomials.max_degree` Maximum possible degree of the generated polynomials.

    - `polynomials.is_complete` Determines if the generated polynomial should be complete or can skip some terms.

    - `polynomials.order` Determines the order of the terms inside the polynomial. If set to *asc* the exponents go in ascending order, if it is set to *desc* they go in descending order, and if set to *none*, no particular order is applied. 

## Configuration JSON for Latex Generation

```json
{
    "coeficients": [            //use if expression_type = polynomial
        "real": CoefficientType,
        "complex": CoefficientType,
        "irrational": CoefficientType,
        "rational": CoefficientType,
        "decimal": CoefficientType,
    ]
}

CoefficientType: {    
    "min": int,
    "max": int,
    "num_decimals": int
}
```
