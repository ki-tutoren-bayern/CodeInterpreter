# Liste sicherer Funktionen

safe_builtins = {
    'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 
    'callable', 'chr', 'classmethod', 'complex', 
    'dict', 'dir', 'divmod', 'enumerate', 'filter', 'float', 'format', 
    'frozenset', 'getattr', 'hasattr', 'hash', 'help', 'hex', 
    'id', 'int', 'isinstance', 'issubclass', 'iter', 'len', 
    'list', 'map', 'max', 'memoryview', 'min', 'next', 'object', 
    'oct', 'ord', 'pow', 'print', 'property', 'range', 'repr', 'reversed', 
    'round', 'set', 'slice', 'sorted', 'staticmethod', 
    'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip', 
    'enumerate', 'filter', 'map', 'zip', 'reduce', 'iter', 'next', 
    'getattr', 'hasattr', 
    'callable', 'format', 'dir', 'vars', 
    'repr', 'ascii', 'bin', 'hex', 'id', 'sorted', 'reversed', 
    'enumerate', 'sum', 'min', 'max', 'any', 'all', 'len', 'divmod',
    'complex', 'int', 'float', 'str', 'bool', 'bytes', 'bytearray', 
    'memoryview', 'tuple', 'range', 'frozenset', 'property', 'classmethod', 
    'staticmethod', 'isinstance', 'issubclass', 'iter', 'next', 'slice', 
    'staticmethod', 'super', 'type', 'zip', 'abs', 'round', 'pow', 
    'hex', 'bin', 'dir', 'vars',
}

safe_math = {
        'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil',
    'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'erf', 'erfc',
    'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum',
    'gcd', 'hypot', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt',
    'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'perm',
    'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan',
    'tanh', 'trunc'
}

safe_datetime = {
        'date', 'datetime', 'time', 'timedelta', 'timezone',
    'datetime.combine', 'datetime.strptime', 'datetime.now', 'datetime.utcnow',
    'datetime.fromtimestamp', 'datetime.utcfromtimestamp', 'datetime.fromordinal',
    'datetime.min', 'datetime.max', 'date.today', 'date.fromtimestamp',
    'date.fromordinal', 'date.min', 'date.max', 'time.min', 'time.max',
    'timedelta.min', 'timedelta.max', 'timezone.utc', 'timezone.timedelta'
}

safe_re = {
    'match', 'fullmatch', 'search', 'sub', 'subn', 'split',
    'findall', 'finditer', 'escape', 'compile',
    'Pattern', 'Match'
}

safe_json = {
    'dump', 'dumps', 'load', 'loads',
    'JSONDecoder', 'JSONEncoder'
}

# Kombinierte Liste aller sicherer Funktionen
safe_functions = {
    'builtins': safe_builtins,
    'math': safe_math,
    'datetime': safe_datetime,
    're': safe_re,
    'json': safe_json
}