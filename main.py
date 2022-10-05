# ©riz4d
import requests as req
from Config import API
def banner():
    banr=  '''
    %%   %%   %%%%    %%%%           %%%%%   %%  %%  %%   %%  %%%%%  
    %%% %%%  %%  %%  %%  %%          %%  %%  %%  %%  %%% %%%  %%  %% 
    %% % %%  %%%%%%  %%      %%%%%%  %%  %%  %%  %%  %% % %%  %%%%%  
    %%   %%  %%  %%  %%  %%          %%  %%  %%  %%  %%   %%  %%  %% 
    %%   %%  %%  %%   %%%%           %%%%%    %%%%   %%   %%  %%%%%
    
                                     Github : @riz4d/MAC-Dumb
    ................................................................  
                                                                  
       '''
    print(banr)
    
banner()
base_url='https://api.macaddress.io/v1?apiKey='
credsurl='https://api.macaddress.io/v1/credits?apiKey='
search_query='&output=json&search='

def guide():
    guid='''
    Step 1 - Go to https://macaddress.io/api
    Step 2 - Signup there
    Step 3 - Key is In 'documentation' section
    Step 4 - Copy and Paste it on <API> in Config file\n'''
    print(guid)
    
    
if API=='':
    print('Sorry!!\n\nAPI Is Missing')
    optn=str(input("Press 'Y' to get guide of API Key : "))
    if optn=='Y':
        guide()
    elif optn=='y':
        guide()
        
else:
    credit=credsurl+API
    cred_res=req.get(credit)
    cred_js=cred_res.json()
    print("    Free Plan\n    -------\n    Total Credits : 100/month\n    Available Credits : "+str(cred_js)+'\n\n')    
    mac_id=str(input('Enter The MAC : '))
    url=base_url+API+search_query+mac_id
    
    mac=req.get(url)
    
    mac_js=mac.json()

    
    oui=str(mac_js['vendorDetails']['oui'])
    ispriv=str(mac_js['vendorDetails']['isPrivate'])
    company=str(mac_js['vendorDetails']['companyName'])
    companyaddr=str(mac_js['vendorDetails']['companyAddress'])
    countrycode=str(mac_js['vendorDetails']['countryCode'])

    blockfound=str(mac_js['blockDetails']['blockFound'])
    borderlft=str(mac_js['blockDetails']['borderLeft'])
    borderrght=str(mac_js['blockDetails']['borderRight'])
    blocksize=str(mac_js['blockDetails']['blockSize'])
    assignment=str(mac_js['blockDetails']['assignmentBlockSize'])
    datecrtd=str(mac_js['blockDetails']['dateCreated'])
    dateupdated=str(mac_js['blockDetails']['dateUpdated'])

    searchtrm=str(mac_js['macAddressDetails']['searchTerm'])
    isvalid=str(mac_js['macAddressDetails']['isValid'])
    virtualmcn=str(mac_js['macAddressDetails']['virtualMachine'])
    app=str(mac_js['macAddressDetails']['applications'])
    transtype=str(mac_js['macAddressDetails']['transmissionType'])
    admtype=str(mac_js['macAddressDetails']['administrationType'])
    wireshrknts=str(mac_js['macAddressDetails']['wiresharkNotes'])
    comment=str(mac_js['macAddressDetails']['comment'])

    mac_vendor="\n\n    Vendor Data's\n    -------------\n\nOUI : "+oui+"\nIsPrivate : "+ispriv+"\nCompany Name : "+company+"\nCompanyAddress : "+companyaddr+"\nCountry Code : "+countrycode
    mac_blockdt="\n\n    Block Details\n    ------------\n\nBlockFound : "+blockfound+"\nBorderLeft : "+borderlft+"\nBorderRight : "+borderrght+"\nBlockSize : "+blocksize+"\nAssignment BlockSize : "+assignment+"\nDate Created : "+datecrtd+"\nDate Updated : "+dateupdated
    mac_data="\n\n    MAC Address Details\n    -------------------\n\nSearchTerm : "+searchtrm+"\nIsValid : "+isvalid+"\nVirtual Machine : "+virtualmcn+"\Application's : "+app+"\nTransmission Type : "+transtype+"\nAdministration Type : "+admtype+"\nWireshark Notes : "+wireshrknts+"\vComment"+comment

    print(mac_data)
    print(mac_vendor)
    print(mac_blockdt)
