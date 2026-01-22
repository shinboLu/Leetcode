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

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        dirs = [[0,1], [1, 0], [0, -1], [-1, 0]]
        visited = set()

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def bt(x, y, cur_dir_idx):
            robot.clean()
            visited.add((x,y))

            for i in range(4): 
                next_dir_idx = (cur_dir_idx + i) % 4
                dx, dy = dirs[next_dir_idx]
                nx, ny = x+dx, y+dy

                if (nx, ny) not in visited and robot.move():
                    bt(nx, ny, next_dir_idx)
                    go_back()
                robot.turnLeft()
        bt(0, 0, 0)