#Given a non-empty string like "Code" return a string like "CCoCodCode".

#string_splosion('Code') -> 'CCoCodCode'
#string_splosion('abc') -> 'aababc'
#string_splosion('ab') -> 'aab'

def string_splosion(str):
    x = 0
    result = ""
    while x != len(str)+1:
        result += str[:x]
        x += 1

    return result

print string_splosion('Code')
print string_splosion('abc')
print string_splosion('ab')
