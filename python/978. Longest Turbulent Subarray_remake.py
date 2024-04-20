def maxTurbulenceSize(arr):
    if len(arr) ==1:
        return 1
    elif len(arr) == 2:
        if arr[0]!=arr[1]:
            return 2
        else:
            return 1

    output=0
    i=0
    counter=1
    variable=0 #-1 expecting lower, 0idgaf, 1expecting higher

    while len(arr)>i+1:
        if variable==0 and arr[i]!=arr[i+1]:    #idgaf and want to gaf
            if counter > output:
                output = counter

            if arr[i]>arr[i+1]:
                variable=1
            else:
                variable=-1

            i+=1
            counter+=1
            continue

        elif arr[i]==arr[i+1]:      #alt.break -> idgaf
            if counter > output:
                output = counter
            counter=1
            variable=0
            i+=1
            continue

        if variable!=-1:    #expecting higher
            if arr[i]>arr[i+1]: #not fulfilled
                if counter>output:
                    output=counter
                variable=0
                counter=1
                continue

            else:
                variable=-1
                counter+=1
            i+=1
            continue

        elif variable!=1:   #expecting lower
            if arr[i]<arr[i+1]:
                if counter>output:
                    output=counter
                variable=0
                counter=1
                continue
            else:
                variable=1
                counter+=1

            i+=1
            continue

    if counter > output:
        return counter
    return output

print(maxTurbulenceSize([1,0,0,1,0,1,1,0,1]))
print(maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))
print(maxTurbulenceSize([3,2,1,1])) #2 decreasing with equal at the end
print(maxTurbulenceSize([3,2,1,0])) #2 decreasing with not equal at the end
print(maxTurbulenceSize([4,8,12,16])) #2 ascending only
print(maxTurbulenceSize([4,8,12,12])) #2 ascending only with equal at the end

print(maxTurbulenceSize([0,1,0,1,1,0,1,0,1,0])) #6 second alt larger than first, not broken at the end
print(maxTurbulenceSize([0,1,0,1,1,0,1,0,1,0,0])) #6 second alt larger than first, broken at the end
print(maxTurbulenceSize([0,1,0,0])) #3 shortest alt on start, broken at the end
print(maxTurbulenceSize([0,1,0])) #3 shortest alt on start, not broken at the end
print(maxTurbulenceSize([4,2,10,7,8])) #5 never breaks alterning
print(maxTurbulenceSize([0,0,1,0,1,0,1])) #6 first3 are shit
print(maxTurbulenceSize([0,0])) #1 shortest non alt.
print(maxTurbulenceSize([0,1])) #2 shortest alt
print(maxTurbulenceSize([1])) #1 one digit
'''
na zaciatku porovname dve susedne, ak su roznej velkosti ok ideme dalej inak i+=1
mame output a counter, ak je counter viac ako output tak sa prepise aby sme returnli vzdy to vacsie
ak su 100 or 011 nastava problem a i+=len(arr) ako aj porovnanie countera a outputu
ak je to 101 alevo 010 i+=1 and counter+=1
'''

