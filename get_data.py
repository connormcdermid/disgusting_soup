import requests

def makeRequest() -> str:
    url = "https://isapp.viu.ca/XMLRequest/xmlrequest"
    headers = {
        'Accept': 'application/xml, text/xml, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': 'https://isapp.viu.ca/srs/timetable.htm',
        'Content-Type': 'application/x-www-form-urlencoded',
        'DbInstance': 'DEFAULT',
        'Origin': 'https://isapp.viu.ca',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Priority': 'u=0'
    }
    payload = {'xmlrequest':
                   "<Request>"
                   + "<Transactions>"
                   + "<GetTimetable>"
                   + "<TransactionID>"
                   + "GetTimetable"
                   + "</TransactionID>"
                   + "<FormID>timetable</FormID>"
                   + "<SessionID>ACAD/*</SessionID>"
                   + "<Campus>N</Campus>"
                   + "<ProgramArea>0005</ProgramArea>"
                   + "<CrsArea>0007</CrsArea>"
                   + "<CrsID/>"
                   "<CrsKeyword/>"
                   "<DeliveryMode/>"
                   "<ShowDescriptions/>"
                   "<ShowCancelledIntakes/>"
                   "<ShowContinuousIntake/>"
                   "<OperUnits>CTU</OperUnits>"
                   "<ShowInstructors>Y</ShowInstructors>"
                   "</GetTimetable>"
                   "</Transactions>"
                   "</Request>"}
    r = requests.post(url, headers=headers, data=payload)
    return r.text

if __name__ == '__main__':
    print(makeRequest())
