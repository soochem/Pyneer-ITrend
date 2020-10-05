# Inflearn pandas L1
# Author : Sumin

import pandas as pd

data_frame = pd.read_csv('data/friend_list.csv')
print(data_frame)
print(data_frame.head(2)) #2개만 보겠다
data_frame.tail(2) #2개만 보겠다
print(type(data_frame.name)) #type이 series -> column, df는 series의 집합체

list_temp = [1,2,3]
s1 = pd.core.series.Series([1,2,3])
s2 = pd.core.series.Series(['one', 'two', 'three'])
df = pd.DataFrame(data=dict(num=s1, word=s2))
print(df)

print("Scraping captions...")
captions = []
time.sleep(10)
for post_num in range(number):
    sys.stdout.write("\033[F")
    print("Scraping captions {} / {}".format(post_num + 1, number))
    # self._driver.implicitly_wait(5)

    if post_num == 0:  # Click on the first post
        # Chrome
        # self._driver.find_element_by_class_name('_ovg3g').click()
        time.sleep(40)
        self._driver.find_element_by_class_name('_bz0w').click()
        self._driver.find_element_by_class_name('_bz0w').click()
        print("Find the first page!!")
        time.sleep(10)

        if number != 1:  #
            WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, CSS_RIGHT_ARROW)
                )
            )

    elif number != 1:  # Click Right Arrow to move to next post
        url_before = self._driver.current_url
        self._driver.find_element_by_css_selector(
            CSS_RIGHT_ARROW).click()

        # Wait until the page has loaded
        try:
            time.sleep(10 + randrange(5))
            WebDriverWait(self._driver, 10).until(
                url_change(url_before))

        except TimeoutException:
            self.download_and_save('./data/', 'tags', 'photos')
            print("Time out in caption scraping at number {}".format(post_num))
            break

    # Parse caption
    try:
        time_element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "time"))
        )
        caption = time_element.find_element_by_xpath(
            TIME_TO_CAPTION_PATH).text
    except NoSuchElementException:  # Forbidden
        self.download_and_save('./data/', 'tags', 'photos')
        print("Caption not found in the {} photo".format(post_num))
        caption = ""

    temp_caption = caption.replace('\n', ' ')
    captions.append(temp_caption)

print(captions)
self.data['captions'] = captions