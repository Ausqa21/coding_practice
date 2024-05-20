"""
def x(rn):
    db = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    cache = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    output = 0

    if rn in cache:
        return cache[rn]

    for i in rn:
        output += db[i]
    
    return output
"""

def x(rn: str):
    db = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    cache = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    output = 0

    if rn in cache:
        return cache[rn]
    
    for key in cache:
        if key in rn:
            output += cache[key] * rn.count(key)
            rn = rn.replace(key, "")

    for i in rn:
        output += db[i]
    
    return output


if __name__ == "__main__":
    print(x("MCMXCIV"))