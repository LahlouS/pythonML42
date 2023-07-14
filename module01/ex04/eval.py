class Evaluator:

    @staticmethod
    def enumerate_evaluate(coefs, words):
        result = 0
        if len(coefs) != len(words) or not isinstance(coefs, list) or not isinstance(words, list):
            return -1
        try:
            for nupelt in enumerate(words, 0):
                if (isinstance(coefs[nupelt[0]], float) or isinstance(coefs[nupelt[0]], int)) and isinstance(nupelt[1], str):
                    result += coefs[nupelt[0]] * len(nupelt[1])
                else:
                    raise
            return result
        except:
            return -1



    @staticmethod
    def zip_evaluate(coefs, words):
        result = 0
        if len(coefs) != len(words) or not isinstance(coefs, list) or not isinstance(words, list):
            return -1
        try:
            for nupelt in zip(coefs, words):
                if (isinstance(nupelt[0], float) or isinstance(nupelt[0], int)) and isinstance(nupelt[1], str):
                    result += nupelt[0] * len(nupelt[1])
                else:
                    raise
            return result
        except:
            return -1

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1, 2, 1, 4, 1]

print(Evaluator().enumerate_evaluate(coefs, words))

words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]

print(Evaluator().zip_evaluate(coefs, words))