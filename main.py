from module.coupling import test
from module.coupling import Coupling

if __name__ == "__main__":
    shib = Coupling()
    print(test())
    print(shib.__dict__)
    print(shib.lat)
    print(shib.shiba)