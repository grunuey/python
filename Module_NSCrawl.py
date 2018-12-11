# 한국 지표 크로링 함수
def KS_Scraping():
	import requests
	import json

	Korea_Stock = ['KOSPI','KOSDAQ','KPI200','FUT']
	Site_Front = 'https://m.stock.naver.com/api/json/'
	Site_Back = '&pageSize='
	View_Value = '365'

	Site_Middle = 'sise/dailySiseIndexListJson.nhn?code='

	i = 0

	while i < len(Korea_Stock):
		url = Site_Front + Site_Middle + Korea_Stock[i] + Site_Back + View_Value
		String = requests.get(url).text

		Front_Clear = String.replace('{"resultCode":"success","result":{"siseList":','')
		Back_Clear = Front_Clear.replace('}}','')

		Result_Data = json.loads(Back_Clear)

		i += 1
		
		for data in Result_Data:
			print(data['dt'],data['cd'],data['ncv'])


# 해외 지표 크로링 함수
def WS_Scraping():
	import requests
	import json

	World_Stock = ['NII@NI225','TWS@TI01','MYI@KLSE','SHS@000002','SHS@000003','SHS@000001','INI@BSE30','IDI@JKSE','HSI@HSI','HSI@HSCE','HSI@HSCC','NAS@SOX','SPI@SPX','NAS@NDX','NAS@IXIC','DJI@DJI','DJI@DJT','BRI@BVSP','STX@SX5E','XTR@DAX30','RUI@RTSI','LNS@FTSE100','ITI@FTSEMIB','PAS@CAC40']
	Site_Front = 'https://m.stock.naver.com/api/json/'
	Site_Back = '&pageSize='
	View_Value = '365'

	Site_Middle = 'world/worldIndexDay.nhn?symbol='

	i = 0

	while i < len(World_Stock):
		url = Site_Front + Site_Middle + World_Stock[i] + Site_Back + View_Value
		String = requests.get(url).text

		Front_Clear = String.replace('{"resultCode":"success","result":{"worldIndexDay":','')
		Back_Clear = Front_Clear.replace('}}','')

		Result_Data = json.loads(Back_Clear)

		i += 1
		
		for data in Result_Data:
			print(data['dt'],data['cd'],data['ncv'])