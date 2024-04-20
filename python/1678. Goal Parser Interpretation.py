class Solution:
    def interpret(self, command: str) -> str:

        # i, o = -1, ''
        # while i < len(command)-1:
        #     i+=1

        #     if command[i] == "G": o+="G"
        #     elif command[i] == "(" and command[i+1] == ")":
        #         i+=1
        #         o+="o"
        #     else: 
        #         i+=3
        #         o+="al"
        
        # return o

        return command.replace('()','o').replace('(al)','al')
