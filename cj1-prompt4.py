class animal:

    def __init__(self):
        # Sample values, change later
        self.arm_length = 2.5
        self.leg_length = 5.2
        self.numberofeyes = 2
        self.tail = True
        self.furry = True
    
    def print_features(self):
        print(f"The length of the animal's arms is {self.arm_length}.")
        print(f"The length of the animal's legs is {self.leg_length}.")
        print(f"The animal has {self.numberofeyes} eyes.")
        if self.tail == True:
            print(f"The animal has a tail.")
        else:
            print(f"The animal does not have a tail.")
        
        
def main():
    my_animal = animal()
    my_animal.print_features()

if __name__ == "__main__":
    main()