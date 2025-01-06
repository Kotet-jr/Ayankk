import itertools
import string

class PasslistGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = '!@#$%^&*()_+-='
    
    def generate_custom_passlist(self, 
                                  min_length=6, 
                                  max_length=12, 
                                  use_lowercase=True, 
                                  use_uppercase=True, 
                                  use_digits=True, 
                                  use_symbols=True):
        # Tentukan set karakter yang akan digunakan
        char_set = ''
        if use_lowercase:
            char_set += self.lowercase
        if use_uppercase:
            char_set += self.uppercase
        if use_digits:
            char_set += self.digits
        if use_symbols:
            char_set += self.symbols
        
        # Buka file untuk menulis passlist
        with open('custom_passlist.txt', 'w') as f:
            for length in range(min_length, max_length + 1):
                for password in itertools.product(char_set, repeat=length):
                    pwd = ''.join(password)
                    f.write(pwd + '\n')
        
        print(f"Custom passlist telah dibuat")
    
    def generate_pattern_based_passlist(self, base_words, 
                                        add_numbers=True, 
                                        add_symbols=True):
        passlist = []
        
        # Generate password dari base words
        for word in base_words:
            # Variasi kapitalisasi
            passlist.append(word)
            passlist.append(word.capitalize())
            passlist.append(word.upper())
            
            # Tambahkan angka
            if add_numbers:
                for i in range(10):
                    passlist.append(word + str(i))
                    passlist.append(str(i) + word)
            
            # Tambahkan simbol
            if add_symbols:
                symbols = ['!', '@', '#', '$', '%']
                for symbol in symbols:
                    passlist.append(word + symbol)
                    passlist.append(symbol + word)
        
        # Tulis ke file
        with open('pattern_passlist.txt', 'w') as f:
            for pwd in passlist:
                f.write(pwd + '\n')
        
        print("Pattern-based passlist telah dibuat")

# Contoh penggunaan
generator = PasslistGenerator()

# Generate passlist kustom
generator.generate_custom_passlist(
    min_length=6, 
    max_length=8, 
    use_lowercase=True, 
    use_uppercase=True, 
    use_digits=True, 
    use_symbols=True
)

# Generate passlist berbasis pola
base_words = ['password', 'admin', 'test', 'welcome']
generator.generate_pattern_based_passlist(base_words)
