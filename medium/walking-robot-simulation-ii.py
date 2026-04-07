from typing import List

class Robot:
    # make it walk in a straight line then project it around the perimeter
    # stupid fucking question

    def __init__(self, width: int, height: int):
        self.perimeter = 2*(width-1) + 2*(height-1)
        self.steps = 0
        self.height = height-1
        self.width = width-1

    def step(self, num: int) -> None:
        self.steps = self.steps+num

    def getPos(self) -> List[int]:
        wrapped = self.steps%self.perimeter

        # south
        if wrapped >= self.perimeter-self.height:
            return [0, self.perimeter - wrapped]
        # west
        if wrapped >= self.width+self.height:
            return [2*self.width+self.height - wrapped, self.height]
        # north
        if wrapped >= self.width:
            return [self.width, wrapped-self.width]
        # east
        if wrapped >= 0:
            return [wrapped, 0]

    def getDir(self) -> str:
        # evil edge case
        if self.steps == 0:
            return "East"

        wrapped = self.steps%self.perimeter
        if wrapped == 0 or wrapped > self.perimeter-self.height:
            return "South"
        if wrapped > self.width+self.height:
            return "West"
        if wrapped > self.width:
            return "North"
        if wrapped > 0:
            return "East"

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()