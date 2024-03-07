def get_array_input(): #get array input
    n = int(input(""))
    return [int(input("")) for i in range(n)] #return array which got input for user

def calculate(arr,result): #calculate proper cage for cats
   removePair = lambda arr: arr[2:] #function that return array which pop 1st and 2nd element already
   Recur = lambda arr,result: calculate(arr,result)#function call recursively
   pop = lambda : arr[1:] #function that return array which pop 1st already
   if len(arr) == 0 or len(arr) == 1: #check remain cat if there's is no cat to compare in current array
        return result #return the final result
   elif arr[0] == arr[1]:#compare if 1st and 2nd cat are equal
        arr = removePair(arr)
        return Recur(arr, result)  
   else: # if 1st & 2nd cat are not equal
        if result < arr[0]: #if current cage size is smaller than current cat
         result = arr[0]
         arr = pop()
         return Recur(arr, result)
        else: #if current cage size is bigger than current cat
            result = arr[0]
            arr = pop()
            return Recur(arr, result)
arr = get_array_input()
result = 0
Ans = calculate(arr,result) #start the function
print ("here is your answer: ",Ans)  # print the final Answer
