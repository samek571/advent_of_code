def maxProfitAssignment(difficulty, profit, worker) -> int:
    #apparently tu je chyba pri velkom inpute (56/57 passed)

    # penis=dict() #docasny dict
    # output=0
    #
    # #each difficulty gains the best profit
    # for i in range(len(difficulty)):
    #     if profit[i] not in penis.keys(): penis[profit[i]]=difficulty[i]
    #     else: penis[profit[i]]=min(difficulty[i], penis[profit[i]])
    #
    #
    # #sort hashmap by difficulty
    # hesmaba=dict()
    # for i in sorted(penis.keys()):#, reverse=True):
    #     hesmaba[i]=penis[i]
    #
    # #removing non worth diff:profit ratios
    # profit=list(hesmaba.keys())
    # difficulty=list(hesmaba.values())
    # n=len(profit)
    # i=1
    # while i!=n:
    #     if difficulty[i-1]>=difficulty[i] and profit[i-1]<=profit[i]:
    #         profit.remove(profit[i-1])
    #         difficulty.remove(difficulty[i-1])
    #         n-=1
    #         continue
    #     i+=1
    #
    # #sort workers by difficulty
    # worker.sort()
    #
    # #grinding
    # robosindex=len(worker)-1
    # i=1
    # while robosindex!=-1 and i!=len(profit)+1:
    #     if difficulty[-i]<=worker[robosindex]:
    #         output+=profit[-i]
    #         robosindex-=1
    #     else: i+=1
    #
    # print(difficulty,profit)
    # return output

    jobs = zip(difficulty, profit)
    jobs=sorted(jobs)

    output = i = best = 0
    for skill in sorted(worker):

        while i < len(jobs) and skill >= jobs[i][0]:
            best = max(best, jobs[i][1])
            i += 1

        output += best

    return output


print(maxProfitAssignment([13,37,58],[4,90,96], [34,73,45] ))
print(maxProfitAssignment([2,4,6,8,10], [10,40,30,40,50],[4,5,6,7]))
print(maxProfitAssignment([2,3,5,5,10], [10,40,30,40,50],[4,5,6,7]))
print(maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50],[4,5,6,7]))
print(maxProfitAssignment([85,47,57], [24,66,99], [40,25,25]))

'''
sort workers and assign profit to diff
sort diff:profit
iterate over diffs and if graph of profit isn't monotone (decreasing or increasing), make it that way
by cutting worse diff:profit ratios

'''