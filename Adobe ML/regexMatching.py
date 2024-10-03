import re
def css_hex_color_code_matcher(input_text):
    # Remove comments from the input text
    modified_text = re.sub(r'/\*.*?\*/', '', input_text, flags = re.DOTALL)
    
    # Match hecadecimal color codes
    hex_color_codes = re.findall(r'#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})\b', modified_text)
    
    # Add the "#" back to the matched color codes
    hex_color_codes = ['#' + code for code in hex_color_codes]
    
    return modified_text, hex_color_codes

if __name__ == "__main__":
    input_text = """
    /* This is a comment */
    body {
    color: #ff5733;
    background-color: #abc;
    }
    /* Another comment */
    div {
    border-color: #123456;
    }
    """
    modified_text, hex_colors = css_hex_color_code_matcher(input_text)
    print("Modified Text:\n", modified_text)
    print("Hex Colors:", hex_colors)