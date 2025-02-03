class Huffman():
    def __init__(self, data):
        self.data = data
        self.unique_data = Huffman.unique(self.data)
        self.probabilities_data = Huffman.probabilities(self.data)
        self.code_dict = self.dict_code(self.unique_data, self.binary_huffman(self.probabilities_data))

    # Count of unique letters
    @classmethod
    def unique(cls, data: str) -> list:
        s = sorted(list(set(data)))
        return s
    
    # Count probabilities of unique letters
    @classmethod
    def probabilities(cls, data: str) -> list:
        probabilities = []
        for j in range(len(data)):
            count = 0
            for letter in data:
                if data[j] == letter:
                    count += 1
            probabilities.append(count/len(data))
        return probabilities
    

    # Function for encode data with Huffman code
    def encode_Huffman(self, data: str, code_dict: dict) -> str:
        encode = ""
        for letter in data:
            if letter in code_dict:
                encode += code_dict[letter]
        return encode
    # Return dict for code
    def dict_code(self, unique, code):
        return dict(zip(unique, code))


    # Calculate code dict for Huffman code
    def binary_huffman(self, probabilities_data: float) -> list:

        if len(probabilities_data) > 2:
            sorted_probs_with_indices = sorted(enumerate(probabilities_data), key=lambda x: x[1], reverse=True)
            sorted_probs = [prob for i, prob in sorted_probs_with_indices]
            idx = [i for i, prob in sorted_probs_with_indices]
            
            prob_without_last = sorted_probs[:-1]
            prob_without_last[-1] = sorted_probs[-2] + sorted_probs[-1]
            prob_without_last_str = [str(p) for p in prob_without_last]

            old_code = self.binary_huffman(prob_without_last_str)

            new_code = old_code[:-1] + [old_code[-1] + '0', old_code[-1] + '1']

            code1 = [None] * len(probabilities_data)
            for i in range(len(probabilities_data)):
                code1[idx[i]] = new_code[i]

        elif len(probabilities_data) == 2:
            code1 = ['0', '1']
        else:
            raise ValueError("Codding don't nedded")
        
        return code1


    
    def decode_Huffman(self, code_table, s):
        decoded = ''
        while len(s) > 0:
            i = 0
            acc = ''
            while i < len(s):
                current_char = s[i]
                acc += current_char
                if acc in code_table.values():
                    new_dict = dict(zip(code_table.values(), code_table.keys()))
                    acc = new_dict[acc]
                    i += 1
                    break
                i += 1
            s = s[i:]
            decoded += acc
        return decoded


if __name__ == '__main__':
    # Example
    data = "abcd"
    huff = Huffman(data)

    unique_data = huff.unique_data
    print(f"Unique elements of data: {unique_data}")

    probabilities_data = huff.probabilities_data
    print(f"Probabilities of data: {probabilities_data}")
    
    code = huff.binary_huffman(probabilities_data)
    print(f"Binary code of data: {code}")

    code_dict = huff.dict_code(unique_data, code)
    print(f"Dictionary of our code: {code_dict}")

    encoded_data = huff.encode_Huffman(data, code_dict)
    print(f"Encoded data: {encoded_data}")

    decoded_data = huff.decode_Huffman(code_dict, encoded_data)
    print(f"Decoded data: {decoded_data}")