import subprocess
from datetime import datetime, timedelta
import os

current_date = datetime.now()
previous_day = current_date - timedelta(days=1)
formatted_date = previous_day.strftime("%d-%b-%Y")
SubCatDict = {"SEQ_LC" :"Large Cap","SEQ_LMC" :"Large & Mid Cap","SEQ_MLC" :"Multi Cap","SEQ_MC" :"Mid Cap","SEQ_SC" :"Small Cap","SEQ_VAL" :"Value","SEQ_ELSS" :"ELSS","SEQ_CONT" :"Contra","SEQ_DIVY" :"Dividend Yield","SEQ_FOC" :"Focused","SEQ_FC" :"Flexi Cap","SEQ_SCTH" :"Sectoral / Thematic","SDT_LND" :"Long Duration","SDT_MLD" :"Medium to Long Duration","SDT_MD" :"Medium Duration","SDT_SD" :"Short Duration","SDT_LWD" :"Low Duration","SDT_USD" :"Ultra Short Duration","SDT_LIQ" :"Liquid","SDT_MM" :"Money Market","SDT_OVNT" :"Overnight","SDT_DB" :"Dynamic Bond","SDT_CB" :"Corporate Bond","SDT_CR" :"Credit Risk","SDT_BPSU" :"Banking and PSU","SDT_FL" :"Floater","SDT_FMP" :"FMP","SDT_GL" :"Gilt","SDT_GL10CD" :"Gilt with 10 year constant duration","SHY_AH" :"Aggressive Hybrid","SHY_BH" :"Balanced Hybrid","SHY_CH" :"Conservative Hybrid","SHY_EQS" :"Equity Savings","SHY_AR" :"Arbitrage","SHY_MAA" :"Multi Asset Allocation","SHY_DAABA" :"Dynamic Asset Allocation or Balanced Advantage","SSO_CHILD" :"Children's","SSO_RETR" :"Retirement","SOTH_IXETF" :"Index Funds/ ETFs","SOTH_FOFS" :"FoFs (Overseas/Domestic)"}

try:
    SubCatDict = {"SEQ_LC" :"Large Cap","SEQ_LMC" :"Large & Mid Cap","SEQ_MLC" :"Multi Cap","SEQ_MC" :"Mid Cap","SEQ_SC" :"Small Cap","SEQ_VAL" :"Value","SEQ_ELSS" :"ELSS","SEQ_CONT" :"Contra","SEQ_DIVY" :"Dividend Yield","SEQ_FOC" :"Focused","SEQ_FC" :"Flexi Cap","SEQ_SCTH" :"Sectoral / Thematic","SDT_LND" :"Long Duration","SDT_MLD" :"Medium to Long Duration","SDT_MD" :"Medium Duration","SDT_SD" :"Short Duration","SDT_LWD" :"Low Duration","SDT_USD" :"Ultra Short Duration","SDT_LIQ" :"Liquid","SDT_MM" :"Money Market","SDT_OVNT" :"Overnight","SDT_DB" :"Dynamic Bond","SDT_CB" :"Corporate Bond","SDT_CR" :"Credit Risk","SDT_BPSU" :"Banking and PSU","SDT_FL" :"Floater","SDT_FMP" :"FMP","SDT_GL" :"Gilt","SDT_GL10CD" :"Gilt with 10 year constant duration","SHY_AH" :"Aggressive Hybrid","SHY_BH" :"Balanced Hybrid","SHY_CH" :"Conservative Hybrid","SHY_EQS" :"Equity Savings","SHY_AR" :"Arbitrage","SHY_MAA" :"Multi Asset Allocation","SHY_DAABA" :"Dynamic Asset Allocation or Balanced Advantage","SSO_CHILD" :"Children's","SSO_RETR" :"Retirement","SOTH_IXETF" :"Index Funds/ ETFs","SOTH_FOFS" :"FoFs (Overseas/Domestic)"}
    print("Formatted Date:", formatted_date)
    directory_name ="data/"+formatted_date
    if not os.path.exists(directory_name):
        # Create the directory
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    else:
        print(f"Directory '{directory_name}' already exists.")

    for SubCat in SubCatDict:
        print("SubCat: ", SubCat, " -> value: ",SubCatDict[SubCat])
        category = SubCat[0:3]
        if (category=="SOT"):
            category = "SOTH"
        print(category)
        curl_command = [
            "curl",
            "https://www.valueresearchonline.com/downloads/amfi-performance-xls/?source_url=%2Famfi%2Ffund-performance-data%2F%3Fend-type%3D1%26primary-category%3D"+category+"%26category%3D"+SubCat+"%26amc%3DALL%26nav-date%3D"+formatted_date,
            "-H", "authority: www.valueresearchonline.com",
            "-H", 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            "-H", 'accept-language: en-IN,en-GB;q=0.9,en;q=0.8,en-US;q=0.7',
            "-H", 'referer: https://www.valueresearchonline.com/amfi/fund-performance',
            "-H", 'sec-ch-ua: "Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
            "-H", 'sec-ch-ua-mobile: ?0',
            "-H", 'sec-ch-ua-platform: "macOS"',
            "-H", 'sec-fetch-dest: iframe',
            "-H", 'sec-fetch-mode: navigate',
            "-H", 'sec-fetch-site: same-origin',
            "-H", 'sec-fetch-user: ?1',
            "-H", 'upgrade-insecure-requests: 1',
            "-H", 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
            "--compressed",
            "--output", directory_name+"/"+SubCat+".xls"
        ]
        result = subprocess.run(curl_command, check=True)
        print("Curl command executed successfully for sub category: ",SubCat)
except subprocess.CalledProcessError as e:
    print("Error executing curl command:", e)
