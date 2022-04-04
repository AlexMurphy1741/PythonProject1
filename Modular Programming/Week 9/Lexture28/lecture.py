class MyFirstClass: # creating our own data type
    def __init__(self, i_value):...

    def say_hi(self):...

    def __str__(self):
        return f"i = {self.i}"


def main():
    #create an instance of a class i.e. create an object