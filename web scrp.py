from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

class web_scrap:
    def WebScrap(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        url = "https://www2.1212.mn/tablesdata1212.aspx?ln=En&tbl_id=DT_NSO_1400_001V1&GH1_select_all=0&GH1SingleSelect=&YearM_select_all=0&YearMSingleSelect=&YearY_select_all=0&YearYSingleSelect=&viewtype="
        driver.get(url)
        driver.find_element_by_xpath("//a[@id='Select_All_GH1']").click()
        driver.find_element_by_xpath("//a[@id='Select_All_YearM']").click()
        driver.find_element_by_id("viewtype-checkbox-table").click()
        driver.find_element_by_xpath("//a[@id='filters']").click()
        
        webtable_df = pd.read_html(driver.find_element_by_xpath("//table[@id='tableStatDiv']"))[0]
        # The pandas read_html() function is a quick and convenient way to turn an HTML table into a pandas DataFrame
        print(webtable_df)
        # webtable_df.to_csv('FOREIGN TRADE TURNOVER, EXPORTS and IMPORTS, BALANCE, by month (cumulative) and year.csv')
    
    def WebScrap0(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        url = "https://www2.1212.mn/tablesdata1212.aspx?tbl_id=dt_nso_0400_025v1&ln=en"
        driver.get(url)
        driver.find_element_by_xpath("//a[@id='Select_All_ISCO']").click()
        driver.find_element_by_xpath("//a[@id='Select_All_gender']").click()
        driver.find_element_by_xpath("(//a[@id='Select_All_YearQ'])[1]").click()
        driver.find_element_by_id("viewtype-checkbox-table").click()
        driver.find_element_by_xpath("//a[@id='filters']").click()
        
        webtable_df = pd.read_html(driver.find_element_by_xpath("//table[@id='tableStatDiv']").get_attribute('outerHTML'))[0]
        print(webtable_df)
        webtable_df.to_csv('MONTHLY AVERAGE WAGES AND SALARIES, by occupation and gender, quarter, year.csv')

web = web_scrap()

web.WebScrap()   
# web.WebScrap0()