class animal:

    def __init__(self, name, arm_length = 2.5, leg_length = 5.2, eyes = 2, tail = True, furry = True):
        self.name = name
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.numberofeyes = eyes
        self.tail = tail
        self.furry = furry
    
    def print_features(self):
        print(f"The length of {self.name}'s arms is {self.arm_length}.")
        print(f"The length of {self.name}'s legs is {self.leg_length}.")
        print(f"The animal {self.name} has {self.numberofeyes} eyes.")
        if self.tail:
            print(f"The animal {self.name} has a tail.")
        else:
            print(f"The animal {self.name} does not have a tail.")
        if self.furry:
            print(f"The animal {self.name} is furry.")
        else:
            print(f"The animal {self.name} is not furry.")

        
def main():
    my_animal = animal("animal1")
    my_animal.print_features()

if __name__ == "__main__":
    main()