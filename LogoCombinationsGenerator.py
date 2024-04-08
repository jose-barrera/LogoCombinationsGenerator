import cv2
import numpy as np

from itertools import chain, combinations

"""Generator of combinations.

    This program generates all possible combinations of sizes 2 to n, from a set of n political parties logos,
    creating images for each and every combination.
    
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
    return chain.from_iterable(combinations(logos, r) for r in range(2, len(logos) + 1))


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
    logos: tuple
) -> str:
    """ Resizes an image to the specific height preserving the aspect ratio.

    Args:
        logos: Tuple with data of images to combine.

    Returns:
        Filename of the created image.
    """
    images = [adjust_height(cv2.imread(logo['filename'], cv2.IMREAD_UNCHANGED), 256) for logo in logos]
    filename = f'generated\\{"-".join([logo["name"] for logo in logos])}.png'
    combination_logo = np.hstack(images)
    cv2.imwrite(filename, combination_logo)
    return filename


if __name__ == '__main__':

    # logos_base is a tuple of dictionaries with source images data. Each dictionary contains the acronym for the
    # political party, and the path for the image file containing the logo. IMPORTANT: Tuple's order will define
    # the combining order when creating the new images.
    logos_base = (
        {'name': 'PP1', 'filename': 'base\\pp1.png'},
        {'name': 'PP2', 'filename': 'base\\pp2.png'},
        {'name': 'PP3', 'filename': 'base\\pp3.png'},
        {'name': 'PP4', 'filename': 'base\\pp4.png'},
        {'name': 'PP5', 'filename': 'base\\pp5.png'},
        {'name': 'PP6', 'filename': 'base\\pp6.png'},
        {'name': 'PP7', 'filename': 'base\\pp7.png'},
        {'name': 'PP8', 'filename': 'base\\pp8.png'}
    )

    for combination in combinator(logos_base):
        print(create_combination_logo(combination), ' ... DONE!')

    print('\nALL DONE!!')
