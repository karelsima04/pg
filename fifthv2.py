
import sys

jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name, header_length):
    
    with open(file_name, "rb") as f:
        data = f.read(header_length)


    return data


def is_jpeg(file_name):
    
    header = read_header(file_name, len())
    


def is_gif(file_name):
    
    header = read_header(file_name, len())
    

   
    


def is_png(file_name):

    header = read_header(file_name, len(png_header))
    
    
    


def print_file_type(file_name):
    
    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')


if __name__ == '__main__':
    # přidej try-catch blok, odchyť obecnou vyjímku Exception a vypiš ji
    file_name = sys.argv[1]
    print_file_type(file_name)
