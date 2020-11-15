# N strings and Q queries

# If all elements of N were the same length, Hash maps could be used
# But lengths are different, so a tree needs to be used

class node:
    def __init__(self, val):
        self.d = {}

head = node(None)

def add_char(c,s,curr, i, l):
    if c not in curr.d:
        curr.d[c] = node(1)
    if l==i+1:
        print("Added Successfully: " + s)
        return
    add_char(s[i+1], s, curr.d[c], i+1, l)


def add_strings(N):
    for str in N:
        print("Adding a new string to tree:", str)
        if len(str) == 0:
            pass
        else:
            add_char(str[0], str, head, 0, len(str))


def does_string_have_prefix(str):
    current_d = head.d
    for c in str:
        if c in current_d:
            current_d=current_d[c].d
        elif current_d=={}:
            print("Yay to:", str)
            return True
        else:
            print("Nay to:", str)
            return False

def check_for_all_strings(Q):
    for S in Q:
        print("___________________________________\nTesting for str:", S)
        does_string_have_prefix(S)


if __name__=="__main__":
    N = ["il", "mis", "de", "pro", "im", "pre"]
    Q = ["illogical", "premature", "proactive", "demonetise", "disease", "impatient", "impossible", "BlahBlahBlah"]
    print("CREATING THE TREE\n__________________________")
    add_strings(N)
    print("___________________________________________________________\n\n")
    check_for_all_strings(Q)


