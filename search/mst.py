from PIL import Image, ImageFilter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pytesseract import *
import base64
import requests
from time import sleep
import random

class MST:
    Check=True  
    options = webdriver.ChromeOptions()                                      # open Chrome
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(executable_path=r"C:\Users\DELL\PycharmProjects\DutyProject\MST\search\chromedriver.exe", options=options) # Khai Báo biến browser từ  link chromedirve
    browser.set_window_size(1050,805)                                       #size chrome
    url= 'http://tracuunnt.gdt.gov.vn/tcnnt/mstdn.jsp'                     
    browser.get(url)                                                        # Mở trang chi cục thuế
    MaSoThue="0315151651"#"0313885914"#"0315151651"#"0313885914"#"0304685595"#"0304685595"#"0301219719"#       # Mã số thuế
    element=browser.find_element_by_name("mst").send_keys(MaSoThue)                  # input Mã số thuế 


    #Vòng lặp đọc captcha
    while Check==True:                                                             
        pytesseract.tesseract_cmd ='C:\\Users\\DELL\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
        screenshot_name = "\captcha.png"
        browser.save_screenshot(screenshot_name)    #lấy màn hình chrome vừa mở

        img = Image.open("\captcha.png")
        area = (820, 517, 965, 572)                 # tọa độ captcha từ màn hình chrome x,y,x1,y1
        cropped_img = img.crop(area)
        cropped_img.save('\captcha6.png')            #Lưu hình ảnh captcha về máy để đọc

        ###################################
        
        csvfilename="‪‪‪\captcha6.png"  # file captcha vừa lưu về máy
        csvfilename = csvfilename.strip('\u202a')   
        with open(csvfilename, "rb") as f:          #convert png sang text
            encoded_string= base64.b64encode(f.read())
        x=requests.post("http://ocr.pvssolution.com:3005/base64ocr",data={"img_base64":encoded_string,"type":"TEXT_DETECTION"})

        a=x.text.split(",")                 # Tách ra tìm description
        for i in range(10):
            if "description" in a =="":     #Nếu không có description thì CT vẫn chạy bình thường
                a=[0,1]
            
            for i in range(len(a)):
                if "description" in a[i]:           #Lấy thông tin trong description
                    t=a[i].split(":")
                    x=t[1][1:-3]                    # x là key captcha
                    x.replace("/","")               #Hạn chế sai captcha
                    x.replace(" ","")               
                    break
                else:                               #Nếu không đọc được file ảnh  gán captcha=123
                    x=123
        ################################
            
        element1=browser.find_element_by_name("captcha").send_keys(x)       # input captcha vừa đọc được 
        destination_page_link = browser.find_element_by_xpath("/html/body/div/div[1]/div[4]/div[2]/div[2]/div/div/div/form/table/tbody/tr[7]/td[2]/div/input[1]")
        destination_page_link.click()        #Nhấp chuột vào ô tra cứu
        sleep(random.randint(2,5))              #Đợi trang load
        
        # Điều kiện để thoát vòng lặp
            
        TT=browser.find_elements_by_xpath('//*[@id="tcmst"]/div[1]/h3')      
        for tt in TT:
            a=tt.text
            if "BẢNG THÔNG TIN TRA CỨU"  in a:         
                Check=False                                                         

        ########################

    T=browser.find_elements_by_xpath('//*[@id="tcmst"]/table/tbody/tr[2]/td[7]/a') # Tình trạng công ty
    company=browser.find_elements_by_xpath('//*[@id="tcmst"]/table/tbody/tr[2]/td[3]/a/b') #Tên công ty
    MST=browser.find_elements_by_xpath('//*[@id="tcmst"]/table/tbody/tr[2]/td[2]/a')                 # Thông tin mã số thuế
    
    for cpn in company:                                             #IN ra Tên Công Ty
        print("Tên công ty: "+cpn.text)
    for mst in MST:                                                 #In mã số thuế
        a=mst.text
        print("Mã số thuế: " +mst.text)
    for t in T:                                                      
        print("Tình trạng: "+t.text)

    #Lấy thông tin địa chỉ bị ẩn trong javascrip

    view=browser.page_source                  
    Address=view[6500:6600]
    Address=Address.split("=")
    Address=Address[1].split(">")
    Address=Address[0].split(":")
    DC=Address[1].split(":")
    dc=""
    for i in range(len(DC)):
        dc+=" " + DC[i]
    address=dc[2:-1]
    print("Địa chỉ công ty: "+address)

    #Đóng trình duyệt
    browser.close()         
        