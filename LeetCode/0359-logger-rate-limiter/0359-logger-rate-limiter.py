class Logger:

    def __init__(self):
        self.time = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.time:
            if self.time[message] <= timestamp:
                self.time[message] = timestamp+ 10
                return True
            else:
                return False
        else:
            self.time[message] = timestamp+10
            return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)