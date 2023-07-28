# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


'''
1. keep set of visited tiles relatively to the starting point &
 change currpos accordingly by each rotation / move
2. go forward to meet the edge and do "ring" around the perimeter with each of them decreasing in radius

if we reach island then basically rings in reverse
'''

'''sexond sol is doing safe dfs'''

class Solution:
    def cleanRoom(self, robot):
        path = set()
        def dfs(x, y, dx, dy):
            # clean 
            robot.clean(); path.add((x, y))

            # next
            for _ in range(4):
                if (x + dx, y + dy) not in path and robot.move():
                    dfs(x + dx, y + dy, dx, dy)
                robot.turnLeft()
                dx, dy = -dy, dx

            # backtrack 
            robot.turnLeft(); robot.turnLeft()
            robot.move()
            robot.turnLeft(); robot.turnLeft()

        dfs(0, 0, 0, 1)
