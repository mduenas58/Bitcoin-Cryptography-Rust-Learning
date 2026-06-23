Write a python program that allows you to "crack" ciphertexts generated using a Vigenere-like cipher, where byte-wise XOR is used instead of addition modulo 26. Specifically, the ciphertext: 

F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1EC
E77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C3
3FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CBB4DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47
EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831
B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF2D730B84CDF3FF
7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5
D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794

Here is a complete Python program that will crack the ciphertext you provided. 

This code uses the **exact same method** you'd use to break a Vigenère cipher, but it works on **bytes (0–255)** instead of letters (A–Z). Since XOR is used, we can treat each position of the repeating key as a single-byte XOR cipher and crack it using frequency analysis.

### How the program works (step-by-step):
1. **Decodes the hex** into raw bytes.
2. **Finds the key length** by calculating the average "Hamming distance" (number of differing bits) between blocks of ciphertext. The correct key length will have the *smallest* average distance.
3. **Splits the ciphertext** into columns based on the key length. (e.g., if the key is 5 bytes long, column 0 holds every 5th byte, column 1 holds every 5th byte starting at index 1, etc.)
4. **Cracks each column** by trying all 256 possible single-byte keys (0x00 to 0xFF). For each attempt, it scores the decrypted text based on how many English letters and spaces appear. The byte that gives the highest score is that position of the key.
5. **Assembles the full key** and decrypts the entire message.
6. **Prints** the recovered key and the plaintext.

```python
import binascii
import string
from collections import Counter

# --- The ciphertext you provided ---
CIPHER_HEX = """
F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1EC
E77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C3
3FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CBB4DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47
EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831
B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF2D730B84CDF3FF
7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5
D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794
"""

def hamming_distance(b1, b2):
    """Count how many bits are different between two bytes objects."""
    return sum(bin(x ^ y).count('1') for x, y in zip(b1, b2))

def find_key_lengths(data, max_len=40):
    """
    Use average normalized Hamming distance to guess the most likely key lengths.
    Returns the top 5 candidates sorted from best to worst.
    """
    scores = {}
    for key_len in range(2, max_len + 1):
        # Take the first 10 blocks (or fewer if data is short) to keep it fast
        blocks = [data[i:i+key_len] for i in range(0, len(data), key_len) 
                  if len(data[i:i+key_len]) == key_len]
        if len(blocks) < 2:
            continue
        
        total_dist = 0
        pairs = 0
        # Compare only the first 10 blocks to avoid O(n^2) slowdown
        for i in range(min(len(blocks), 10)):
            for j in range(i + 1, min(len(blocks), 10)):
                total_dist += hamming_distance(blocks[i], blocks[j]) / key_len
                pairs += 1
        
        scores[key_len] = total_dist / pairs if pairs > 0 else float('inf')
    
    # Return the key lengths with the smallest average distances
    return sorted(scores, key=scores.get)[:5]

def score_plaintext(byte_data):
    """
    Score a piece of decrypted data.
    Rewards letters (A-Z, a-z) and spaces.
    Penalizes weird control characters heavily.
    """
    score = 0
    for b in byte_data:
        if 65 <= b <= 90 or 97 <= b <= 122:  # A-Z or a-z
            score += 1
        elif b == 32:  # space
            score += 1
        elif 32 <= b <= 126:  # printable punctuation/digits
            score += 0.2
        else:  # non-printable, control chars, etc.
            score -= 10
    return score

def crack_single_byte_xor(column_bytes):
    """
    Given a list of bytes that were all XORed with the same single byte,
    find the most likely key byte by trying all 256 possibilities.
    """
    best_key = 0
    best_score = -1
    for key_byte in range(256):
        decrypted = bytes([b ^ key_byte for b in column_bytes])
        sc = score_plaintext(decrypted)
        if sc > best_score:
            best_score = sc
            best_key = key_byte
    return best_key

def main():
    # 1. Clean the hex string and convert to bytes
    hex_clean = ''.join(CIPHER_HEX.split())
    ciphertext = bytes.fromhex(hex_clean)
    print(f"[+] Ciphertext length: {len(ciphertext)} bytes")

    # 2. Guess the key length
    candidates = find_key_lengths(ciphertext)
    print(f"[+] Most likely key lengths: {candidates}")

    # 3. Try each candidate key length and pick the best overall
    best_overall_score = -1
    best_key = None
    best_plaintext = None

    for key_len in candidates:
        print(f"[+] Trying key length: {key_len}")
        
        # Crack each column to build the full key
        key_bytes = bytearray()
        for col in range(key_len):
            # Extract every 'key_len'-th byte starting at 'col'
            column_data = ciphertext[col::key_len]
            key_byte = crack_single_byte_xor(column_data)
            key_bytes.append(key_byte)
        
        # Decrypt the full ciphertext with this key
        key = bytes(key_bytes)
        plaintext = bytes([ciphertext[i] ^ key[i % len(key)] for i in range(len(ciphertext))])
        
        # Score the full plaintext
        full_score = score_plaintext(plaintext)
        if full_score > best_overall_score:
            best_overall_score = full_score
            best_key = key
            best_plaintext = plaintext

    # 4. Print the results
    print("\n" + "=" * 50)
    print(f"[+] Recovered Key: {best_key.hex().upper()}")
    print(f"[+] Key (as ASCII, if printable): {best_key.decode('utf-8', errors='replace')}")
    print("\n" + "=" * 50)
    print("[+] Decrypted Plaintext:")
    print("-" * 50)
    print(best_plaintext.decode('utf-8', errors='replace'))

if __name__ == "__main__":
    main()
```

### What output you can expect:
When you run this, the program will:

1. Guess the key length (it will likely be **7**).
2. Recover the key (which will look like a hex string, e.g., `F9...`, but since it's XORed over bytes, it might contain non-printable characters—though it often turns out to be an English word or phrase like `"SECRET"` or similar).
3. Print the fully decrypted English plaintext.

### Important note:
This script assumes the plaintext is standard English text (using spaces and letters). Because your ciphertext is very long, the frequency analysis will be **highly accurate**, and it should recover the key perfectly on the first try.

Go ahead and run it! Once you see the output, you'll have successfully broken a real repeating-key XOR cipher—the exact same technique used to crack the famous "Vigenère" cipher, but extended to all 256 bytes! 🚀