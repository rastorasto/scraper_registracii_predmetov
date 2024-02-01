import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from colorama import Fore, Style

username = input("Enter your username: ")
password = input("Enter your password: ")
os.system('cls' if os.name == 'nt' else 'clear')

course_codes_input = input("Enter the course codes separated by commas (leave empty to display all): ")
course_codes = [code for code in course_codes_input.upper().split(',') if code]


driver = webdriver.Safari()
driver.get("https://www.vut.cz/login")
log_user = driver.find_element(By.XPATH, '//*[@id="login7"]')
log_pass = driver.find_element(By.XPATH, '//*[@id="passwd7"]')
log_user.send_keys(username)
log_pass.send_keys((password), Keys.ENTER)

time.sleep(1)

while True:
    driver.get("https://www.vut.cz/studis/student.phtml?sn=individualni_plan_fit")
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    rows = soup.find_all('tr', class_=['pov_2_sel', 'pov_13', 'pov_3_sel'])
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in rows:
        course_code = row.select_one('b a').text.strip()
        course_name = row.select_one('td:nth-of-type(2) a').text.strip()[:30]
        #semester = row.select_one('td.center:nth-of-type(3)').text.strip()
        #season = row.select_one('td.center:nth-of-type(4)').text.strip()
        #exams = row.select_one('td.center:nth-of-type(5)').text.strip()
        #faculty = row.select_one('td.center:nth-of-type(6)').text.strip()
        #form = row.select_one('td.center:nth-of-type(7)').text.strip()
        points = row.select_one('td.center:nth-of-type(8)').text.strip()
        #print(f"{Fore.RED}{course_code:<10}\t{Fore.GREEN}{course_name:<20}\t{Fore.YELLOW}{semester:<10}\t{Fore.BLUE}{season:<10}\t{Fore.MAGENTA}{exams:<10}\t{Fore.CYAN}{faculty:<10}\t{Fore.WHITE}{form:<10}\t{Fore.GREEN}{points:<10}{Style.RESET_ALL}")
        if course_codes and course_code not in course_codes:
            continue
        points_parts = points.split('/')
        if len(points_parts) == 2 and points_parts[0] == points_parts[1]:  # Check if the points are full
            points_color = Fore.RED
        else:
            points_color = Fore.BLUE

        print(f"{Fore.RED}{course_code:<10}{Fore.GREEN}{course_name:<35}\t{points_color}{points}{Style.RESET_ALL}")
    time.sleep(3)