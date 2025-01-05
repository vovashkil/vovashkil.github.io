# This utility functions are used to print a text sourrounded by a border of boxes
# A multi-line text can be used as well, and padding can be specified
u_box1 = u"\u2588"
u_box2 = u"\u2593"
DEFAULT_CARD_HEIGHT = 20
DEFAULT_TEXT_LINE_LENGTH = 80
def print_boxed_line(text, card_width=DEFAULT_TEXT_LINE_LENGTH, padding = 0, center = True, bold = False):
    # space available for text
    text_space = card_width - 2

    # caluclate text length
    text_len = len(text)
    
    # if requested, add characters to make text bold (in terminals that support it)
    if bold:
        text = "\033[1m" + text + "\033[0m"
    
    # initialialize left padding to be left justified
    text_lpad = 1
    # if line should be centered, adjust the left_padding
    if center:      
        # left padding for text should be half of the difference between the full area and the text area
        text_lpad = (text_space - text_len) // 2
        
    # right padding should be total minus what we already used
    text_rpad = text_space - text_len - text_lpad
    
    # now just print everything
    print("".rjust(padding) + u_box1 + \
          "".rjust(text_lpad) + text + \
          "".rjust(text_rpad) + u_box1)

# This utility function prints an empty line with border on the right and left
def print_empty_line(padding, card_width):
    print("".rjust(padding) + u_box1 + " ".ljust(card_width - 2) + u_box1)

DEFAULT_CARD_HEIGHT = 20
DEFAULT_CARD_WIDTH = 35
def print_note_card(text, title = None, card_width=DEFAULT_CARD_WIDTH, card_height=DEFAULT_CARD_HEIGHT, padding = 0):
    # if padding was specified, reduce the width to accomodate
    if (padding > 0):
        card_width -= padding * 2
      
    # print carriage returns for padding on top
    for i in range(padding):
        print()
        
    # since text could be multipline, we start by splitting it
    text_list = text.split("\n")

    # calculate full text length depending on whether title was passed
    text_len = (len(text_list) + 3) if title else len(text_list)
    
    # calculate padding on top and bottom of box (do nothing if it's negative)
    pad_height = (card_height // 2) - text_len // 2
    if pad_height < 0:
        return

    # print top line
    print("".rjust(padding) + u_box1.rjust(card_width, u_box1))

    # if title was passed, print it
    if title:
        print_empty_line(padding, card_width)
        print_boxed_line(title, card_width, padding, center = True, bold = True)
        print_empty_line(padding, card_width)
        
    # print half height of blank lines with border
    for i in range(pad_height - 1):
        print_empty_line(padding, card_width)
        
    # print text lines left justified
    for text in text_list:
        print_boxed_line(text, card_width, padding, center = False)

    # print half height of blank lines with border
    for i in range(pad_height - 1):
        print_empty_line(padding, card_width)

    # print bottom line
    print("".rjust(padding) + u_box1.rjust(card_width, u_box1))

    # print carriage returns for padding on top
    for i in range(padding):
        print()