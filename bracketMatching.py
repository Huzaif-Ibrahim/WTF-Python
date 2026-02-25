import stack 

def check_brackets(statement): 
    s = stack.Stack()
    for token in statement: 
        if token in "{[(": 
            s.push(token) 
        elif token in "}])": 
            if s.isEmpty(): 
                return False 
            else: 
                left = s.pop() 
                if (token == "}" and left != "{") or (token == "]" and left != "[") or (token == ")" and left != "("): 
                    return False 
    return s.isEmpty() 
  
stmt=input("Enter an expression:") 
res=check_brackets(stmt) 
if res==True: 
    print(f"{stmt} is having balanced parantheses") 
else: 
    print(f"{stmt} is not having balanced parantheses")