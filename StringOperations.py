from functools import partial

class StringOperations:
    """
    Clase para realizar operaciones simples en cadenas de texto.
    """

    def capitalize_text(self, text):
        return text.capitalize()

    def replace_substring(self, text, old, new):
        return text.replace(old, new)
    
    # Implementar los métodos de la clase StringOperations.
string_operations = StringOperations()

# Crear versiones especializadas usando functools.partial
capitalize_first_word = partial(string_operations.capitalize_text)
replace_spaces_with_underscore = partial(string_operations.replace_substring, old=" ", new="_")
# Ejemplos de uso
def main():
    text = "hola mundo"
    
    # Usando capitalize_first_word
    print(capitalize_first_word(text))  # Output: "Hola mundo"
    
    # Usando replace_spaces_with_underscore
    print(replace_spaces_with_underscore(text))  # Output: "hola_mundo"

if __name__ == "__main__":
    main()