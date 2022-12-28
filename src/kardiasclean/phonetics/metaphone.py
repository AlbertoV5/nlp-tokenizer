"""
Phonetic Algorithms

Paper:
    https://iopscience.iop.org/article/10.1088/1757-899X/508/1/012106/pdf
"""

D_METAPHONE_EN = {
    r'(^[KGP])(N)': lambda x: x.group(2),
    r'(^A)(E)': lambda x: x.group(2),
    r'(^W)(R)': lambda x: x.group(2),
    r'(M)(B)$': lambda x: x.group(1),
    r'(SCH)': 'K',
    r'(C)(IA|H)': lambda x: f"X{x.group(2)}",
    r'(C)([IEY])': lambda x: f"S{x.group(2)}",
    r'(C)': 'K',
    r'(D)(GE|GY|GI)': lambda x: f"J{x.group(2)}",
    r'(D)': 'T',
    r'(G)(H[^AEIOU](?<!H)$)': lambda x: x.group(2),
    r'(G)(N|NED)$': lambda x: x.group(2),
    r'(GG)': 'KK',
    r'(G)([IEY])': lambda x: f"J{x.group(2)}",
    r'(G)': 'K',
    r'([AEIOU])(H)([^AEIOU])': lambda x: f"{x.group(1)}{x.group(3)}",
    r'(CK)': 'K',
    r'(PH)': 'F',
    r'(Q)': 'K',
    r'(S)(H|IO|IA)': lambda x: f"X{x.group(2)}",
    r'(T)(IA|IO)': lambda x: f"X{x.group(2)}",
    r'(TH)': '0',
    r'(T)(CH)': 'CH',
    r'(V)': 'F',
    r'^(WH)': 'W',
    r'(W)([^AEIOU])': lambda x: x.group(2),
    r'^(X)': 'S',
    r'(X)': 'KS',
    r'(Y)([^AEIOU])': lambda x: x.group(2),
    r'(Z)': 'S',
    r'([AEIOU])(?<!^[AEIOU])': ''
}


def metaphone_en(word: str):
    word = word.upper()

    return word


def metasoundex_en(w: str):
    return w