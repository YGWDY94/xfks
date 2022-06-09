
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import login


def get_html_list(browser):
    try:
        brocks = browser.find_element_by_class_name("film_focus_nav").find_elements_by_tag_name('li')
        print(len(brocks))
    except:
        home_page = "http://xfks-study.gdsf.gov.cn/study/index"
        browser.get(home_page)
        #    back_link = browser.find_element_by_link_text("年度学法")
        #    back_link.click()
        brocks = browser.find_element_by_class_name("film_focus_nav").find_elements_by_tag_name('li')
    #        print(len(brocks))

    #get each chapter's links
    url_address = []
    for i in brocks:
        i.click()
        #    print("CLICKED BROCK")
        #    time.sleep(1)
        links = browser.find_elements_by_link_text("进入学习")
        for link in links:
            #            print("GETTING URL")
            try:
                url = link.get_attribute('href')
                url_address.append(url)
            #            time.sleep(1)
            except:
                print("Error")


    html_links = []
    for url in url_address:
        browser.get(url)
        chapters = browser.find_elements_by_class_name("chapter")
        for chapter in chapters:
            elems = chapter.find_elements_by_tag_name("li")
            for elem in elems:
                if elem.find_element_by_class_name("sub_title").text == '获得0.5学分':
                    print(f"It had been studied \n")
                else:
                    html = elem.find_elements_by_tag_name("a")[0]
                    #            print(len(elem.find_elements_by_tag_name("a")))
                    if html.get_attribute("href") == None:
                        pass
                    else:
                        html_links.append(html.get_attribute("href"))
        time.sleep(1)
    return html_links

def to_study(browser):
    html_links = get_html_list(browser)
    page = 0
#    browser.get(url)
#    time.sleep(2)
    for html_link in html_links:
        browser.get(html_link)
        #                html_link.click()
        time.sleep(65)
        page += 1
        print(f"Turn to next page{page}")
#    print(f"Finished Chapter {i + 1}")
    print("Finished")

if __name__ == "__main__":
    browser = login.get_website('http://xfks-study.gdsf.gov.cn')
    print("请输入用户名")
    username = input()
    print("请输入密码")
    passwd = input()
    print("请输入验证码")
    key = input()
    login.login(username, passwd, key, browser)
#    browser, brocks = contents.get_brocks(browser)

#    html_links = get_html_list(browser)
    to_study(browser)

 #   contents.get_contents(browser, brocks)




