    
letters = ["a", "b", "d", "e", "i", "j", "x", "t"]

def vowels(letter):
    vowels = ["a", "e", "i", "u", "o"]
    
    if (letter in vowels):
        return True
    else:
        return False

filtered_vowels = filter(vowels, letters)

print("the filtered vowels are:")

for vowel in filtered_vowels:
    print(vowel)
    
print(* filtered_vowels)

