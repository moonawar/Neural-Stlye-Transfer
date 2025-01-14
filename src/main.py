from utils import *
from nst import stylize

if __name__ == '__main__':
    log('Selecting Content Image')
    content_path = select_file('Select content image')

    log('Selecting Style Image')
    style_path = select_file('Select style image')

    log('Loading images...')
    content_image = load_image(content_path)
    style_image = load_image(style_path)

    log('Stylizing images...')
    result = stylize(content_image, style_image)

    log('Saving result...')
    save_pil_image(result, 'result.jpg')

    log('Done!')