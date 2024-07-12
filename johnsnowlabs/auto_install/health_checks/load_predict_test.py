# Convert pdf to image
from johnsnowlabs import nlp


def run_test():
    # nlp.start()
    data = ["hello world", "I love apples"]
    model = nlp.load("<MODEL>")
    print("model loaded", model)

    df = model.predict(data)
    for c in df.columns:
        print(df[c])


if __name__ == "__main__":
    run_test()
