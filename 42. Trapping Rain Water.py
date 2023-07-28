class Solution:
    def trap(height) -> int:
        """
        najdeme si najvyssi element
        iterujeme postupne height a porovnavame dve susedne ci je [i]>[i+1], ak ano tak spustime while cyklus a znacime si
        {kolko pozicii sme isli, suma hodnoty kazdej pozicii} ak natrafime na [i]<=[i+x] stopneme while cyklus a spravime
        output+= (height[i]*kolkopozicii sme isli - suma hodnoty kazdej pozicii) nasledne i+=kolkopos sme isli

        Ak natrafime na najvyssi bar a je jediny tak vysoky tak ideme toto iste len odzadu. Ak je ich viac najvacsej vysky
        tak spravime to iste co doteraz len medzi nimi. K tomu poslednemu ideme tiez odzadu.

        """
        #najvyssi element + pozicia posledneho
        highest=height[0]
        position=0
        for y in range (len(height)):
            # if height[y]==highest:
            #     position+=1
            if height[y] >= highest:
                position=y
                highest=height[y]

        print(highest, position)

        #handling pica cases
        if len(height)<3:
            return 0

        #z lava po posledny najvyssi element
        output=0
        i=0
        while len(height)>i+1:
            if i>=position:
                break

            if height[i] > height[i+1]:

                k=1
                sum_of_blacks=0
                while height[i] > height[i + k]:
                    sum_of_blacks+=height[i+k]
                    k+=1

                    if i+k>=len(height):
                        break

                if not len(height)-i==k:
                    output += (height[i] * (k-1) - sum_of_blacks)
                i+=k
                continue
            i+=1

        #z druhej strany
        i=len(height)-1 #12
        while i > position:
            if height[i]>height[i-1]:

                k=1
                sum_of_blacks=0
                while height[i]>height[i-k]:

                    sum_of_blacks += height[i - k]
                    k += 1

                    if i - k == position:
                        break

                output += (height[i] * (k-1) - sum_of_blacks)
                i-=k
                continue
            i-=1

        return output

    print(trap([4,0,6]))
    print(trap([3, 2, 1, 2, 1]))
    print(trap([1,0,2,1,0,1,3,2,3,1,2]))
