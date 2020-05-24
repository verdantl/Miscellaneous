from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import random, requests, bs4, time, webbrowser


def csc148sectiontabs(sect: int) -> list:
    """Opens tabs in the given section of the CSC148 notes offered at the
    University of Toronto.
    Valid as of April 2020.
    """
    print('Searching...')
    res = requests.get(
        'https://www.teach.cs.toronto.edu/~csc148h/winter/notes/')
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    sects = soup.select('h2')
    parsed = soup.select('#' + sects[sect - 1].get('id'))[0].find_next_sibling()

    carrot_soup = bs4.BeautifulSoup(str(parsed), 'html.parser')
    links = carrot_soup.select('a')
    titles = []
    for i in range(len(links)):
        url = 'https://www.teach.cs.toronto.edu/~csc148h/winter/notes/' + \
              links[i].get('href')
        titles.append(links[i].getText())
        print('Opening', url)
        webbrowser.open(url)
    return titles


def random_2048_player(lag: int) -> None:
    """Plays 2048 randomly in a new window and makes moves with a lag speed
    depending on the value of lag."""

    browser = webdriver.Chrome()
    browser.get('https://gabrielecirulli.github.io/2048/')

    element = browser.find_element_by_tag_name('body')

    for i in range(100):
        move = random.choice([Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT])

        element.send_keys(move)

        time.sleep(lag)


def reddit_post_locator(browser: webdriver) -> None:
    pass


def reddit(subreddit: str, keyword: str, upvote_cutoff: int,
           comment_cutoff: int, criteria: str, timing: str) -> dict:
    """Returns a compiled number of reddit links and their descriptions
    that match the criteria.
    Up to date as of April 2020. Virtually a clone of reddit.
    """
    chrome_options = webdriver.ChromeOptions()

    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option('prefs', prefs)

    browser = webdriver.Chrome(options=chrome_options)

    keywords = keyword.split()

    url = 'https://www.reddit.com/r/' + subreddit + '/search/?q=' + \
          '%20'.join(keywords) + '&restrict_sr=1&sort=' + criteria + \
          '&sort=' + timing

    browser.get(url)
    browser.implicitly_wait(10)
    upvotes = browser.find_elements_by_class_name('_1rZYMD_4xY3gRcSS3p8ODO')
    comments = browser.find_elements_by_class_name('FHCV02u6Cp2zYL0fhQPsO')
    links = browser.find_elements_by_class_name('_eYtD2XCVieq6emjKBH3m')

    upvote_list, comments_list, title_list, links_list = [], [], [], []
    for i in range(len(upvotes)):
        if i % 2 == 0:
            upvote_list.append(int(upvotes[i].get_attribute("innerHTML")))

    for num in comments:
        comments_list.append(
            reddit_number_conversion(num.get_attribute("innerHTML")))

    for link in links:
        title_list.append(
            reddit_html_conversion(link.get_attribute('innerHTML')))

    for title in title_list:
        browser.find_element_by_link_text(title).click()
        links_list.append(browser.current_url)
        browser.back()

    nums = {}
    for i in range(min(30, len(upvote_list))):
        nums[i] = [upvote_list[i], comments_list[i], title_list[i],
                   links_list[i]]

    for post in range(len(nums)):
        if nums[post][0] < upvote_cutoff or nums[post][1] < comment_cutoff:
            nums.pop(post)

    return nums


    # for reddit_post in nums:
    # nums[reddit_post][3] + ', at' + nums[reddit_post][2]
    # no error is raised

    # upvotes = soup.select('._1rZYMD_4xY3gRcSS3p8ODO')
    # comments = soup.select('.FHCV02u6Cp2zYL0fhQPsO')
    # links = soup.select('.SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE')
    # # TODO use selenium to simulate browser, work on later
    #
    # upvote_nums = reddit_number_conversion(upvotes)
    # comment_nums = reddit_number_conversion(comments)
    # link_lst = []
    # for link in links:
    #     url = 'https://www.reddit.com' + link.get('href')
    #     link_lst.append(url)
    #
    # if len(nums) == 0:
    #     return None
    #
    # for link in range(len(nums)):
    #     site = requests.get(nums[link][2])
    #
    #     subsoup = bs4.BeautifulSoup(site.text, 'html.parser')
    #     title = subsoup.select('._eYtD2XCVieq6emjKBH3m')
    #     nums[link].append(title[0].getText())
    #
    # for reddit_post in nums:
    #     return nums[reddit_post][3] + ', at' + nums[reddit_post][2]


def reddit_number_conversion(string: str) -> int:
    """Converts the numeric value in string to an integer.
    Precondition: there is only one number in string
    """
    num = ''
    for char in string:
        if char.isnumeric():
            num += char

    return int(num)


def reddit_html_conversion(string: str) -> str:
    """Converts html to the text inside string, and gets rid of the '&amp' that
    come with the '&' character.

    Precondition: There are no tag characters '<' or '> in the actual text."""
    converted = ''
    tag = False
    for char in string:
        if char == '<':
            tag = False
        elif char == '>':
            tag = True
        elif tag:
            converted += char
    if '&amp;' in converted:
        converted = converted.replace('&amp;', '&')

    return converted


# div class is _1rZYMD_4xY3gRcSS3p8ODO for upvotes
# span class is FHCV02u6Cp2zYL0fhQPsO for comments
# class for links is SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE
# title class is _eYtD2XCVieq6emjKBH3m
if __name__ == '__main__':
    print(csc148sectiontabs(7))
    #random_2048_player(1)
    #print(reddit('UofT', 'cs post', 10, 0, 'new', 'all'))

    # sub = str(input('Which subreddit would you like to visit?'))
    # key = input('Which keyword would you like to input?')
    # up = input('What is the minimum number of upvotes?')
    # comm = input('What is the minimum number of comments?')
    # crit = input('How would you like to sort the results? '
    #              'Your choices are: relevance, top, new, or comments.')
    # timing = input('From when? The past hour, day, week, year, or all?')
    # print(reddit(sub, str(key), int(up), int(comm), str(crit), str(timing)))
