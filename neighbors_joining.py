
def main(n, d, node_list=None, dic = None):    
    if dic == None:
        dic = {}
    if node_list == None:
        node_list = list(range(n))

    if n == 2:
        if node_list[0] not in dic.keys():
            dic[node_list[0]]={}
        if node_list[1] not in dic.keys():
            dic[node_list[1]]={}
        dic[node_list[0]][node_list[1]]=d[0][1]
        dic[node_list[1]][node_list[0]]=d[0][1]
         
        return dic
    else:
        d2 = neighborjoinmat(n, d)
        min_ele = findminelement(n, d2) # this return a list of 2 integers for i, j
        i = min_ele[0]
        j = min_ele[1]
        diff = (sum(d[i]) - sum(d[j]))/(n-2)
        limb_i = (d[i][j] + diff)/2
        limb_j = (d[i][j] - diff)/2

        add_row = [(d[k][i] + d[k][j] - d[i][j])/2 for k in range(n)] + [0]
        d.append(add_row)
    
        for l in range(n):
            d[l].append(add_row[l])
        
        #keep track of the node--column
        m = node_list[-1] +1
        node_list.append(m)
        
        # remove i, j col
        [ab.pop(max(i,j)) for ab in d]
        [ab.pop(min(i,j)) for ab in d]
        # remove i, j row
        d.remove(d[max(i,j)])
        d.remove(d[min(i,j)])
        

        node_i = node_list[i]
        node_j = node_list[j]
        node_list.remove(node_i)
        node_list.remove(node_j)
    
        
        if node_i not in dic.keys():
            dic[node_i]={}
        if node_j not in dic.keys():
            dic[node_j]={}
        if m not in dic.keys():
            dic[m]={}
        dic[node_i][m]=limb_i
        dic[node_j][m]=limb_j
        dic[m][node_i]=limb_i
        dic[m][node_j]=limb_j

        main(n-1, d, node_list, dic)
        return dic



def neighborjoinmat(n, matr):
    matr2 = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                new_dis = (n-2)* matr[i][j] - sum(matr[i]) - sum(matr[j])
                matr2[i][j]= new_dis
    return matr2

def findminelement(n, matri):
    min_value = matri[0][0]
    for i in range(n):
        for j in range(i,n):
            if matri[i][j]< min_value:
                min_value = matri[i][j]
                position = [i,j]
    return position



# this file must only include function definitions
# comment out code you may have for testing before submitting your code:
with open('rosalind_ba7e.txt') as f:
    n = int(f.readline())
    d = []
    for i in range(n):
        d.append([int(t) for t in f.readline().split()])
t = main(n, d)
for key in t:
    for node in t[key]:
        print(str(key)+"->" + str(node)+":" +str(t[key][node]))
        
