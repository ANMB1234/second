from sample import TrainingKnownSample


valid={"sepal_length" : "5.1","sepal_width":"3.5","petal_length":"1.4","petal_width":"0.2",
       "species" : "Iris-setosa"}

rks=TrainingKnownSample.from_dict(valid)
