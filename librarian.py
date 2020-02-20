###### Reading Inputs ###############

# B,L,D are number of Books, Libraries and Days.
B,L,D = map(int,input().split())

# scores of B books
scores = list(map(int,input().split()))

libraries = []

for j in range(L):
    """
    # N is number of books in libray j
    # T is the number of days it takes to finish the 
        library signup process for library j
    # M is the number of books that can be shipped from
        library j to the scanning facility per day, once
        the library is signed up
    # P is the list of books present in library j
    """
    N,T,M = map(int, input().split())
    P = list(map(int,input().split()))
    # sort P based on scores( Descending order)
    P = sorted(P,reverse = True,key= lambda x: scores[x])
    libraries.append((N,T,M,P))
    
######################################
def rater(x):
    arr = libraries[x][3][:int(((libraries[x][1] + len(libraries[x][3])// D)-libraries[x][1] )*libraries[x][2])]
    sum_val = 0 
    for i in arr:
        sum_val += scores[sum_val]
    return sum_val

# sort libraries based on time to signup ( ascending order)
lib_ids = [i for i in range(len(libraries))]
lib_ids = sorted(lib_ids,key = rater)

# lets remove duplicates
ptrs = [0 for i in range(len(libraries))]
books_set = set()


x_lib = 0
while True:
    nothing_selected = True
    curr = ptrs[lib_ids[x_lib]]
    next =  curr + libraries[lib_ids[x_lib]][2]
    skip = 0
    while curr<len(libraries[lib_ids[x_lib]][3]) and curr < next+skip and curr<=D:
        if libraries[lib_ids[x_lib]][3][curr] not in books_set:
            books_set.add(libraries[lib_ids[x_lib]][3][curr])
            nothing_selected = False
        else:
            libraries[lib_ids[x_lib]][3][curr] = -1
            skip += 1
        ptrs[lib_ids[x_lib]]+=1
        curr += 1
    x_lib += 1
    if x_lib >= len(libraries):
        x_lib = 0
        if nothing_selected:
            break
    

# OUTPUT
ans = []
for i in lib_ids:
    final_book_list = []
    for j in libraries[i][3]:
        if j>=0:
            final_book_list.append(j)
    if len(final_book_list):
        ans.append((i,final_book_list))
    

# OUTPUT  
print(len(ans))
for i in ans:
    
    print(i[0],len(i[1]))
    print(*i[1])
    
