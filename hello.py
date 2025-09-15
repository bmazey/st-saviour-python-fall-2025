class ElyceBrand:
    def __init__(self):
        self.name = "Elyce"
        self.tagline = "Code meets cosmos"
        self.values = ["Creativity", "Clarity", "Curiosity"]

    def launch(self):
        print(f"Welcome to {self.name} — {self.tagline}")
        print("Core values:")
        for value in self.values:
            print(f"- {value}")

if __name__ == "__main__":
    brand = ElyceBrand()
    brand.launch()