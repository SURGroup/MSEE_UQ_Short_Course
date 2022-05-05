class PythonModel:
    def __init__(self, samples=None):
        list1=[]
        for x in samples:
            y=x**2
            list1.append(y)
        self.qoi=list1