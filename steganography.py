from PIL import Image

def encode_text_to_image(image_path, output_path, message):
    img = Image.open(image_path)
    binary_msg = ''.join(format(ord(char), '08b') for char in message) + '11111110'  # EOF marker
    data = list(img.getdata())

    new_data = []
    msg_index = 0
    for pixel in data:
        if msg_index < len(binary_msg):
            if len(pixel) == 3:
                r, g, b = pixel
                r = (r & ~1) | int(binary_msg[msg_index])
                new_data.append((r, g, b))
            elif len(pixel) == 4:
                r, g, b, a = pixel
                r = (r & ~1) | int(binary_msg[msg_index])
                new_data.append((r, g, b, a))
            msg_index += 1
        else:
            new_data.append(pixel)

    img.putdata(new_data)
    img.save(output_path)
    print("Message encoded successfully!")

def decode_text_from_image(image_path):
    img = Image.open(image_path)
    data = list(img.getdata())

    binary_msg = ''
    for pixel in data:
        if len(pixel) == 3:
            r, g, b = pixel
        elif len(pixel) == 4:
            r, g, b, a = pixel
        binary_msg += str(r & 1)

    chars = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    message = ''
    for char in chars:
        if char == '11111110':
            break
        message += chr(int(char, 2))

    print("Decoded message:", message)

# --- RUN BELOW ---
# First, uncomment to encode
encode_text_to_image('input.png', 'output.png', 'Hello, this is secret!')

# Then later, comment the above and uncomment this to decode
decode_text_from_image('output.png')
