import fileinput
import re

def main():
    for line in fileinput.input():
        itens = line.split(';')
        operation = itens[0]
        argument  = itens[1]
        name      = itens[2].replace('\r', '').replace('\n', '')
        
        # Split
        if operation == 'S': 
            name  = name.replace('()', '')
            words = re.findall('[a-zA-Z][^A-Z]*', name)
            words = [word.lower() for word in words]

            print(' '.join(words))
            
        # Combine
        else:
            words = name.split(' ')
            
            # Variable
            if argument == 'V':
                words = [words[0].lower()] + [word[0].upper() + word[1:] for word in words[1:]]
                
            # Class
            elif argument == 'C':
                words = [word[0].upper() + word[1:] for word in name.split(' ')]
                
            # Method
            else:
                words = [words[0].lower()] + [word[0].upper() + word[1:] for word in words[1:]]
                words.append('()')
                
            print (''.join(words))
            
    
if __name__=="__main__":
    main()