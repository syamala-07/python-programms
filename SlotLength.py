#two durations that sums to SlotLength
def findTaskPairForSlot(taskDuratons,SlotLength):
    for i in range(len(taskDuratons)):
        for j in range(i+1,len(taskDuratons)):
            if taskDurations[i]+taskDurations[j] == SlotLength:
                return[i,j]
    return[-1,-1]
taskDurations = [1, 3, 4, 6, 8]
SlotLength = 10
result = findTaskPairForSlot(taskDurations, SlotLength)
print(result)