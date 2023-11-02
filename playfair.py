def prepare_text(text):
    # Remove spaces and convert to uppercase
    text = text.replace(" ", "").upper()
    # Replace 'J' with 'I' (standard Playfair rule)
    text = text.replace("J", "I")
    return text

def create_playfair_matrix(key):
    # Create a Playfair matrix (5x5) using the given key
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = prepare_text(key)
    matrix = []
    for letter in key + alphabet:
        if letter not in matrix:
            matrix.append(letter)
    playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
    return playfair_matrix

def find_position(matrix, letter):
    # Find the position of a letter in the Playfair matrix
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j

def encrypt_digraph(matrix, digraph):
    # Encrypt a digraph using the Playfair cipher rules
    a, b = digraph[0], digraph[1]
    a_row, a_col = find_position(matrix, a)
    b_row, b_col = find_position(matrix, b)
    
    if a_row == b_row:
        return matrix[a_row][(a_col + 1) % 5] + matrix[b_row][(b_col + 1) % 5]
    elif a_col == b_col:
        return matrix[(a_row + 1) % 5][a_col] + matrix[(b_row + 1) % 5][b_col]
    else:
        return matrix[a_row][b_col] + matrix[b_row][a_col]

def playfair_encrypt(plaintext, key):
    plaintext = prepare_text(plaintext)
    matrix = create_playfair_matrix(key)
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        digraph = plaintext[i:i+2]
        if len(digraph) == 2:
            ciphertext += encrypt_digraph(matrix, digraph)
        else:
            # Handle odd-length plaintext by appending 'X' before encryption
            ciphertext += encrypt_digraph(matrix, digraph + 'X')
    return ciphertext

# Example usage
plaintext = "HELLO"
key = "KEYWORD"
ciphertext = playfair_encrypt(plaintext, key)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
