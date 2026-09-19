class BungeoppangShop:
    def __init__(self):
        self.display = {}
    def report(self):
        for k in self.display:
            print(k, self.display[k])
    def bake(self, filling):
        if filling in self.display:
            self.display[filling] = self.display[filling] + 1
        else:
            self.display[filling] = 1
        
    def sell(self, filling):
        if filling not in self.display:
            self.display[filling] = 0

        self.display[filling] = self.display[filling] - 1
        
        if self.display[filling] < 0:
            print(filling, "부족!")


log = [("bake", "팥"), ("bake", "슈크림"), ("sell", "팥"), ("report", None)]

shop = BungeoppangShop()

for action, value in log:
    if action == "bake":
        shop.bake(value)
    elif action == "sell":
        shop.sell(value)
    elif action == "report":
        shop.report()



