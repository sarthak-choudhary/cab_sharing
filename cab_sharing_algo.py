import gc

class cablisting():
    def __init__(self,id,starting,ending):
        self.id = id
        self.start = starting
        self.end = ending 
        self.timeperiod =[]
        self.group = None
        
        for x in range(self.start,self.end+1,1):
            self.timeperiod.append(x)

    def __lt__(self,other):
        return self.start < other.start

    def __le__(self,other):
        return self.start < other.start or self.start==other.start

    def __eq__(self,other):
        return self.start == other.start

    def __gt__(self,other):
        return self.start > other.start
    
    def __ge__(self,other):
        return self.start > other.start or self.start==other.start

# create a usr in this manner usr = cablisting(id,starting time,ending time)
p5 = cablisting(5,5,8)

p1 = cablisting(1,3,7)

p2 = cablisting(2,3,8)

# p7 = cablisting(7,6,9)

# p8 = cablisting(8,6,8)

# p3 = cablisting(3,3,6)

# p6 = cablisting(6,5,9)

# p4 = cablisting(4,4,6)

# p9 = cablisting(9,7,9)

plist = []

#put all the cablisting objects in plist
for obj in gc.get_objects():
    if isinstance(obj,cablisting):
        plist.append(obj)

#QuickSort begins 
def partition(arr,low,high):
    i = ( low - 1)
    pivot = arr[high]


    for j in range(low ,high):


        if arr[j] <= pivot :


            i = i+1
            arr[i],arr[j] = arr[j],arr[i]


    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)


def quickSort(arr,low,high):
    if low < high :


        pi = partition(arr,low,high)



        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)


n = len(plist)
quickSort(plist,0,n-1)
# got the sorted list of cablisting objects 

#to find the intersection between sets of timeperiod of variable users
#groups are assigned group numbers individual returns the list of members in a single group
def findingset(*args):

    # print(args[0])
    # print(args[0][0])

    intersect = args[0][0].timeperiod

    for p in args[0]:
        intersect = list(set(intersect) & set(p.timeperiod))

    return intersect
    


#main logic for grouping people
def grouping(members):

    group_no = 1

    #if there are total less than 4 
    if len(members) < 4:
        group = [x for x in members]    #put all members in a single 

        common_time = len(findingset(group))

        if common_time > 0:
            for x in group:
                x.group = group_no
                group_no = group_no + 1

        elif common_time == 0: #if there is no intersection btween existing users<4
            if len(members) == 3:
                comb1 = [members[0],members[1]]
                comb2 = [members[1],members[2]]
                comb3 = [members[0],members[2]]

                if len(findingset(comb1))>len(findingset(comb2)) and len(findingset(comb1))>len(findingset(comb3)):
                    for x in comb1:
                        group = comb1
                        x.group = group_no
                    
                    group_no = group_no + 1

                elif len(findingset(comb2))>len(findingset(comb1)) and len(findingset(comb2))>len(findingset(comb3)):
                    for x in comb2:
                        group = comb2
                        x.group = group_no

                    group_no = group_no + 1

                elif len(findingset(comb3))>len(findingset(comb2)) and len(findingset(comb3))>len(findingset(comb1)):
                    for x in comb3:
                        group = comb3
                        x.group = group_no

                    group_no = group_no + 1

            elif len(members) == 2:
                comb = [members[0],members[1]]

                if len(findingset(comb)) > 0:
                    for x in comb:
                        group = commb
                        x.group = group_no
                    
                    group_no = group_no + 1
                else:
                    group = [] 

    if len(members) >= 4 :
        group = []

        pointer = 0

        for a in range(4):
            group.append(members[pointer])
            a = a + 1
            pointer = pointer + 1

        for turn in range(len(members)-4) :
            common_time = len(findingset(group))

            prev_group = group

            if common_time > 0:
                bottleneck = 0
                for x in range(4): 
                    if group[x].timeperiod[-1] == findingset(group)[-1]:
                        bottleneck = bottleneck +1

                if bottleneck < 2:
                    for x in range(4): 
                        if group[x].timeperiod[-1] == findingset(group)[-1]:
                            group.pop(x)
                            group.append(members[pointer])
                            pointer = pointer + 1

                    if len(findingset(group)) <= common_time:
                        group = prev_group
                    
                    elif len(findingset(group)) == 0:
                        group = prev_group
                        break

            turn = turn + 1

        for p in group:
            p.group = group_no


    return group


cab = grouping(plist)

for x in cab:
    print(x.id)
