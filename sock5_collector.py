from selenium import webdriver
import string
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time	
import datetime
from selenium.webdriver.common.by import By
import os

today = datetime.date.today()


# ------------------------------------------------------------------------------------------------------------------------
def website1():	
	f = open("sock5/{}.txt".format(today) , "w+")
	for i in range(1,6):
		driver.get('http://free-proxy.cz/en/proxylist/country/all/socks5/ping/all/{}'.format(i))
		trs = driver.find_elements(By.TAG_NAME, "tr") 
		count = 5
		for i in trs:
			try:
				tds = trs[count].find_elements(By.TAG_NAME, "td")
				f.write(tds[0].text + ":" + tds[1].text + "\n")
				count +=1 
			except:
				count += 1
	f.close()

# #-------------------------------------------------------------------------------------------------------------------------
def website2():
	f = open("sock5/{}.txt".format(today) , "w+")
	driver.get('https://www.proxy-list.download/SOCKS5')
	contents = driver.find_element_by_id('txta1').get_attribute('value')
	f.write(contents + "\n")
	f.close()

# #-------------------------------------------------------------------------------------------------------------------------
def website3():
	f = open("sock5/{}.txt".format(today) , "w+")
	driver.get('https://hidemyna.me/en/proxy-list/?type=5#list')
	time.sleep(12)
	trs = driver.find_elements(By.TAG_NAME, "tr") 
	count = 1
	for i in trs:
		try:
			tds = trs[count].find_elements(By.TAG_NAME, "td")
			f.write(tds[0].text + ":" + tds[1].text + "\n")
			count +=1
		except:
			count += 1

	driver.get('https://hidemyna.me/en/proxy-list/?type=5&start=64#list')
	time.sleep(12)
	trs = driver.find_elements(By.TAG_NAME, "tr") 
	count = 1
	for i in trs:
		try:
			tds = trs[count].find_elements(By.TAG_NAME, "td")
			f.write(tds[0].text + ":" + tds[1].text + "\n")
			count +=1
		except:
			count += 1

	driver.get('https://hidemyna.me/en/proxy-list/?type=5&start=128#list')
	time.sleep(12)
	trs = driver.find_elements(By.TAG_NAME, "tr") 
	count = 1
	for i in trs:
		try:
			tds = trs[count].find_elements(By.TAG_NAME, "td")
			f.write(tds[0].text + ":" + tds[1].text + "\n")
			count +=1
		except:
			count += 1
	f.close()

#-------------------------------------------------------------------------------------------------------------------------
def combo1():

	driver.get('http://www.vipsocks24.net/')

	elems = driver.find_elements_by_xpath("//a[@href]")
	print(elems[9].text)
	link1 = str(elems[9].get_attribute("href"))
	link2 = str(elems[21].get_attribute("href"))
	link3 = str(elems[33].get_attribute("href"))
	link4 = str(elems[45].get_attribute("href"))

	#===========================================================================================================

	driver.get(link1)
	elems1 = driver.find_elements_by_xpath("//a[@href]")

	driver.get(elems1[10].get_attribute("href"))

	time.sleep(10)
	os.system("sudo unzip /0x026f/Downloads/vipsocks.zip")
	time
	os.system("sudo rm /0x026f/Desktop/What\ is\ my\ IP.url")
	os.system("sudo rm /0x026f/Desktop/Strong\ VPN.url")


	with open("/0x026f/Desktop/vipsocks.txt") as f:
	    lines = f.readlines()
	    lines = [l for l in lines]
	    with open("sock5/{}.txt".format(today) , "a+") as f1:
	        f1.writelines(lines)
	        f1.close()



	os.system("sudo rm /0x026f/Desktop/vipsocks.txt")
	os.system("sudo rm /0x026f/Downloads/vipsocks.zip")
	time.sleep(2)
	# # ====================================================================================================
	# # for elem in elems:
	# #     print (elem.get_attribute("href"))
	# # ====================================================================================================
	driver.get(link2)
	elems2 = driver.find_elements_by_xpath("//a[@href]")

	driver.get(elems2[10].get_attribute("href"))

	# f.close()

	time.sleep(10)
	os.system("sudo unzip /0x026f/Downloads/vipsocks.zip")
	time
	os.system("sudo rm /0x026f/Desktop/What\ is\ my\ IP.url")
	os.system("sudo rm /0x026f/Desktop/Strong\ VPN.url")


	with open("/0x026f/Desktop/vipsocks.txt") as f:
	    lines = f.readlines()
	    lines = [l for l in lines]
	    with open("sock5/{}.txt".format(today) , "a+") as f1:
	        f1.writelines(lines)
	        f1.close()

	os.system("sudo rm /0x026f/Desktop/vipsocks.txt")
	os.system("sudo rm /0x026f/Downloads/vipsocks.zip")
	time.sleep(2)
	# # ====================================================================================================
	driver.get(link3)
	elems3 = driver.find_elements_by_xpath("//a[@href]")

	driver.get(elems3[10].get_attribute("href"))

	# f.close()

	time.sleep(10)
	os.system("sudo unzip /0x026f/Downloads/vipsocks.zip")
	time
	os.system("sudo rm /0x026f/Desktop/What\ is\ my\ IP.url")
	os.system("sudo rm /0x026f/Desktop/Strong\ VPN.url")


	with open("/0x026f/Desktop/vipsocks.txt") as f:
	    lines = f.readlines()
	    lines = [l for l in lines]
	    with open("sock5/{}.txt".format(today) , "a+") as f1:
	        f1.writelines(lines)
	        f1.close()

	os.system("sudo rm /0x026f/Desktop/vipsocks.txt")
	os.system("sudo rm /0x026f/Downloads/vipsocks.zip")

	return link4 

	#======================================================================================================
def combo2(link):

	time.sleep(2)

	driver.get(link)

	elems = driver.find_elements_by_xpath("//a[@href]")
	print(elems[9].text)
	link1 = str(elems[10].get_attribute("href"))
	link2 = str(elems[22].get_attribute("href"))
	link3 = str(elems[34].get_attribute("href"))

	#===========================================================================================================

	driver.get(link1)
	elems1 = driver.find_elements_by_xpath("//a[@href]")

	driver.get(elems1[10].get_attribute("href"))

	time.sleep(10)
	os.system("sudo unzip /0x026f/Downloads/vipsocks.zip")
	time
	os.system("sudo rm /0x026f/Desktop/What\ is\ my\ IP.url")
	os.system("sudo rm /0x026f/Desktop/Strong\ VPN.url")


	with open("/0x026f/Desktop/vipsocks.txt") as f:
	    lines = f.readlines()
	    lines = [l for l in lines]
	    with open("sock5/{}.txt".format(today) , "a+") as f1:
	        f1.writelines(lines)
	        f1.close()



	os.system("sudo rm /0x026f/Desktop/vipsocks.txt")
	os.system("sudo rm /0x026f/Downloads/vipsocks.zip")
	time.sleep(2)
	# # ====================================================================================================
	# # for elem in elems:
	# #     print (elem.get_attribute("href"))
	# # ====================================================================================================
	driver.get(link2)
	elems2 = driver.find_elements_by_xpath("//a[@href]")

	driver.get(elems2[10].get_attribute("href"))

	# f.close()

	time.sleep(10)
	os.system("sudo unzip /0x026f/Downloads/vipsocks.zip")
	time
	os.system("sudo rm /0x026f/Desktop/What\ is\ my\ IP.url")
	os.system("sudo rm /0x026f/Desktop/Strong\ VPN.url")


	with open("/0x026f/Desktop/vipsocks.txt") as f:
	    lines = f.readlines()
	    lines = [l for l in lines]
	    with open("sock5/{}.txt".format(today) , "a+") as f1:
	        f1.writelines(lines)
	        f1.close()

	os.system("sudo rm /0x026f/Desktop/vipsocks.txt")
	os.system("sudo rm /0x026f/Downloads/vipsocks.zip")
	time.sleep(2)
	# # ====================================================================================================
	driver.get(link3)
	elems3 = driver.find_elements_by_xpath("//a[@href]")

	driver.get(elems3[10].get_attribute("href"))

	# f.close()

	time.sleep(10)
	os.system("sudo unzip /0x026f/Downloads/vipsocks.zip")
	time
	os.system("sudo rm /0x026f/Desktop/What\ is\ my\ IP.url")
	os.system("sudo rm /0x026f/Desktop/Strong\ VPN.url")


	with open("/0x026f/Desktop/vipsocks.txt") as f:
	    lines = f.readlines()
	    lines = [l for l in lines]
	    with open("sock5/{}.txt".format(today) , "a+") as f1:
	        f1.writelines(lines)
	        f1.close()

	os.system("sudo rm /0x026f/Desktop/vipsocks.txt")
	os.system("sudo rm /0x026f/Downloads/vipsocks.zip")

if __name__ == '__main__':
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--incognito")
	driver = webdriver.Chrome(chrome_options=chrome_options)
	# website1()
	# website2()
	# website3()
	ret = combo1()
	combo2(ret)
