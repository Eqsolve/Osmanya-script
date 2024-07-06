# Define the mapping from Somali Latin script to Osmanya script
somali_to_osmanya = {
    'B': '𐒁', 'T': '𐒂', 'J': '𐒃', 'X': '𐒄', 'KH': '𐒅',
    'D': '𐒆', 'R': '𐒇', 'S': '𐒈', 'SH': '𐒉', 'DH': '𐒊',
    'C': '𐒋', 'G': '𐒌', 'F': '𐒍', 'Q': '𐒎', 'K': '𐒏',
    'L': '𐒐', 'M': '𐒑', 'N': '𐒒', 'W': '𐒓', 'H': '𐒔',
    'Y': '𐒕', 'A': '𐒖', 'E': '𐒗', 'I': '𐒘', 'O': '𐒙',
    'U': '𐒚', 'AA': '𐒛', 'EE': '𐒜', 'II': '𐒘𐒘', 'OO': '𐒝',
    'UU': '𐒚𐒚', '0': '𐒠', '1': '𐒡', '2': '𐒢', '3': '𐒣',
    '4': '𐒤', '5': '𐒥', '6': '𐒦', '7': '𐒧', '8': '𐒨',
    '9': '𐒩', '10': '𐒡𐒠'
}

# Function to convert Somali Latin script to Osmanya script
def convert_to_osmanya(text):
    # Sort keys by length to handle multi-character keys like 'KH', 'SH', 'DH', etc.
    sorted_keys = sorted(somali_to_osmanya.keys(), key=len, reverse=True)
    for key in sorted_keys:
        text = text.replace(key, somali_to_osmanya[key])
    return text

# Main loop
def main():
    while True:
        # Prompt the user for input
        somali_text = input("Enter Somali Latin words (or type 'exit' to quit): ")
        if somali_text.lower() == 'exit':
            break
        
        # Convert and print the result
        osmanya_text = convert_to_osmanya(somali_text.upper())
        print(f"Osmanya script: {osmanya_text}")

# Run the script
if __name__ == "__main__":
    main()
