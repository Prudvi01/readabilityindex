# coding=UTF8
from helper import syllable_count, sentence_count

#print(syllable_count('Bureaucratic'))  # prints "2"

def ARI(text):
    """Automated Readability Index
    Designed to gauge the understandability of a text. 
    The output is an approximate representation of the 
    U.S grade level needed to comprehend a text."""
    words = len(text.split())
    characters = len(text)
    sentences = sentence_count(text)
    
    ARI = 4.71 * (characters/words) + 0.5 * (words/sentences) -21.43
    return ARI

def FRE(text):
    """Flesch Reading Ease
    Designed to indicate how difficult a reading passage is to understand. 
    Higher scores indicate material that is easier to read; 
    lower numbers mark harder-to-read passages."""
    words = len(text.split())
    syllables = syllable_count(text)
    sentences = sentence_count(text)
    FRE = (206.835 - (1.015*(words/ sentences))) - 84.6 * (syllables/ words)
    return FRE

def FKGL(text):
    """FleschKincaid Grade Level
    Designed to indicate how difficult a reading passage is to understand. 
    The result is a number that corresponds with a U.S grade level."""
    words = len(text.split())
    syllables = syllable_count(text)
    sentences = sentence_count(text)

    FKGL = 0.39 * (words/sentences) + 11.8 * (syllables/words) - 15.59
    return FKGL

def CLI(text):
    """Coleman-Liau Index
    Designed to gauge the understandability of a text. 
    The output is the approximate U.S. grade level 
    thought necessary to comprehend the text."""
    characters = len(text)
    words = len(text.split())
    sentences = sentence_count(text)

    CLI = (5.89 * (characters/ words)) - (30 *(sentences/words)) - 15.8
    return CLI
'''
def GFI(text):
    """Gunning Fog Index"""
    GFI = GFI = 0.4 * (( words/ sentences) + 100 * (complex words/ words))
    return GFI'''
text  = 'A Turning machine is a device that manipulates symbols on a strip of tape according to a table of rules. Despite its simplicity, a Turing machine can be adapted to simulate the logic of any computer algorithm, and is particularly useful in explaining the functions of a CPU inside a computer. The "Turing" machine was described by Alan Turing in 1936, who called it an "a(utomatic)-machine". The Turing machine is not intended as a practical computing technology, but rather as a hypothetical device representing a computing machine. Turing machines help computer scientists understand the limits of mechaniacl computation.'

'''
print("ARI = " + str(ARI(text)))
print("FRE = " + str(FRE(text)))
print("FKGL = " + str(FKGL(text)))
print("CLI = " + str(CLI(text)))
'''