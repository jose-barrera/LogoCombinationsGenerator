import cv2
import numpy as np

from PIL import Image
from itertools import chain, combinations

"""Generator of combinations.

    This program generates all possible combinations of sizes 1 to n, from a set of n political parties logos,
    creating images for each and every combination. If selected, the images are generated in grayscale.
    
"""


def combinator(
    logos: tuple
) -> chain:
    """ Generates all possible n-size combination using all logos available.

    Args:
        logos: A tuple of dictionaries with logos' data.

    Returns:
        An object containing all possible combinations.
    """
    return chain.from_iterable(combinations(logos, r) for r in range(1, len(logos) + 1))


def adjust_height(
    image: np.ndarray,
    height: int
) -> np.ndarray:
    """ Resizes an image to the specific height preserving the aspect ratio.

    Args:
        image: The image to adjust.
        height: The desired height.

    Returns:
        An image with adjusted dimensions.
    """
    hh, ww = image.shape[1::-1]
    width = int(height * ww / hh)

    return cv2.resize(image, (height, width))


def create_combination_logo(
    logos: tuple,
    grayscale: bool
) -> str:
    """ Resizes an image to the specific height preserving the aspect ratio,
        and optionally converting to grayscale image.

    Args:
        logos: Tuple with data of images to combine.
        grayscale: Boolean flag to generate grayscale instead of color images.

    Returns:
        Filename of the created image.
    """
    images = [adjust_height(cv2.imread(logo['filename'], cv2.IMREAD_UNCHANGED), 256) for logo in logos]
    filename = f'generated\\{"-".join([logo["name"] for logo in logos])}.png'
    combination_logo = np.hstack(images)
    cv2.imwrite(filename, combination_logo)
    # Convert to grayscale if requested
    if grayscale:
        gray_image = Image.open(filename).convert('LA')
        gray_image.save(filename)

    return filename


if __name__ == '__main__':

    # logos_base is a tuple of dictionaries with source images data. Each dictionary contains the acronym for the
    # political party, and the path for the image file containing the logo. IMPORTANT: Tuple's order will define
    # the combining order when creating the new images.
    logos_base = (
        {'name': 'P1', 'filename': 'base\\p1.png'},
        {'name': 'P2', 'filename': 'base\\p2.png'},
        {'name': 'P3', 'filename': 'base\\p3.png'},
        {'name': 'P4', 'filename': 'base\\p4.png'},
        {'name': 'P5', 'filename': 'base\\p5.png'},
        {'name': 'P6', 'filename': 'base\\p6.png'},
        {'name': 'P7', 'filename': 'base\\p7.png'},
        {'name': 'P8', 'filename': 'base\\p8.png'}
    )

    for combination in combinator(logos_base):
        print(create_combination_logo(combination, True), ' ... DONE!')

    print('\nALL DONE!!')
