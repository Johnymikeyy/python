def texter(text1, text2, text3):
    print(f"{text2} {text3} {text1}")
text1 = "i"
text2 = "love"
text3 = "you"

texter(text1="you", text2="i", text3="love")

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    
print(parrot(1000))