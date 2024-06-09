#!/bin/env python3

import argparse

def format_shellcode(shellcode):
    # Remove all double quotes and newlines, then split by '\x'
    shellcode = shellcode.replace('"', '').replace('\n', '')
    shellcode = shellcode.strip()
    
    # Split the string by '\x' and filter out empty strings
    bytes_list = shellcode.split('\\x')
    bytes_list = [byte for byte in bytes_list if byte]  # Filter out any empty strings
    
    formatted_shellcode = 'unsigned char rawShellcode[] = {\n\t'
    # Add '0x' prefix to each byte and join with commas
    for i, byte in enumerate(bytes_list):
        formatted_shellcode += f'0x{byte}, '
        # Add a newline and tab every 16 bytes
        if (i + 1) % 16 == 0:
            formatted_shellcode = formatted_shellcode.rstrip(', ') + ',\n\t'
    
    formatted_shellcode = formatted_shellcode.rstrip(', \n\t') + '\n};\n'
    return formatted_shellcode

def main():
    parser = argparse.ArgumentParser(description='Format raw shellcode into C array format.')
    parser.add_argument('input_file', help='File containing raw shellcode')
    parser.add_argument('-o', '--output', help='Output file to save formatted shellcode', default=None)
    
    args = parser.parse_args()
    
    with open(args.input_file, 'r') as file:
        raw_shellcode = file.read()

    formatted_shellcode = format_shellcode(raw_shellcode)
    
    if args.output:
        with open(args.output, 'w') as file:
            file.write(formatted_shellcode)
    else:
        print(formatted_shellcode)

if __name__ == '__main__':
    main()

