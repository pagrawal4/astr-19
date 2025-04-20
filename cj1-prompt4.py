class FavoriteAnimal:

    def __init__(self, name, arm_length = 2.5, leg_length = 5.2, num_eyes = 2, has_tail = True, is_furry = True):
        self.name = name
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry
    
    def print_features(self):
        print(f"The length of {self.name}'s arms is {self.arm_length}.")
        print(f"The length of {self.name}'s legs is {self.leg_length}.")
        print(f"The animal {self.name} has {self.num_eyes} eyes.")
        if self.has_tail:
            print(f"The animal {self.name} has a tail.")
        else:
            print(f"The animal {self.name} does not have a tail.")
        if self.is_furry:
            print(f"The animal {self.name} is furry.")
        else:
            print(f"The animal {self.name} is not furry.")

        
def main():
    my_animal = FavoriteAnimal("Kangaroo")
    my_animal.print_features()

if __name__ == "__main__":
    main()