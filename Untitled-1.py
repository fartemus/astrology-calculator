# %%
pip install numpy


# %%
import numpy as np

zodiac_list = [
    'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
    'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
]

descriptor_list = [
    'Calm: Relaxed and untroubled',
    'Candid: Honest and straightforward',
    'Caring: Shows empathy and concern',
    'Cheerful: Happy and optimistic',
    'Compassionate: Feels and shows sympathy',
    'Creative: Imaginative and innovative',
    'Curious: Eager to learn and explore',
    'Daring: Bold and adventurous',
    'Earnest: Sincere and serious',
    'Easygoing: Relaxed and carefree',
    'Empathetic: Understands others feelings',
    'Energetic: Full of energy',
    'Faithful: Loyal and reliable',
    'Fearless: Unafraid and bold',
    'Generous: Willing to give freely',
    'Gracious: Courteous and kind',
    'Honest: Truthful and sincere',
    'Humorous: Funny and entertaining',
    'Intuitive: Understands instinctively',
    'Joyful: Full of happiness',
    'Just: Fair and righteous',
    'Kind: Caring and considerate',
    'Loyal: Faithful and reliable',
    'Magnanimous: Generous and forgiving',
    'Open-minded: Receptive to new ideas',
    'Optimistic: Positive outlook on life',
    'Passionate: Shows strong enthusiasm',
    'Philosophical: Thoughtful and wise',
    'Sincere: Genuine and honest',
    'Sociable: Enjoys social interactions',
    'Thoughtful: Considerate of others’ needs'
]

def astrology_calculator(month=None, day=None, city=None, state=None, hour=None, minute=None, am=None):
    rng = np.random.default_rng(12345)
    rints = rng.integers(low=0, high=31, size=11)
    rints2 = rng.integers(low=0, high=12, size=11)

    return print(
        f"Your sun sign is {zodiac_list[rints2[0]]} — this shows you are {descriptor_list[rints[0]]},\n"
        f"Your moon sign is {zodiac_list[rints2[1]]} — this shows you are {descriptor_list[rints[1]]},\n"
        f"Your rising sign is {zodiac_list[rints2[2]]} — this shows you are {descriptor_list[rints[2]]},\n"
        f"Your Mercury is in {zodiac_list[rints2[3]]} — this shows you are {descriptor_list[rints[3]]},\n"
        f"Your Venus is in {zodiac_list[rints2[4]]} — this shows you are {descriptor_list[rints[4]]},\n"
        f"Your Mars is in {zodiac_list[rints2[5]]} — this shows you are {descriptor_list[rints[5]]},\n"
        f"Your Jupiter is in {zodiac_list[rints2[6]]} — this shows you are {descriptor_list[rints[6]]},\n"
        f"Your Saturn is in {zodiac_list[rints2[7]]} — this shows you are {descriptor_list[rints[7]]},\n"
        f"Your Uranus is in {zodiac_list[rints2[8]]} — this shows you are {descriptor_list[rints[8]]},\n"
        f"Your Neptune is in {zodiac_list[rints2[9]]} — this shows you are {descriptor_list[rints[9]]},\n"
        f"Your Pluto is in {zodiac_list[rints2[10]]} — this shows you are {descriptor_list[rints[10]]}"
    )



