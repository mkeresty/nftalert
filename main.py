from __future__ import print_function

import json
import discord
import requests
import time

global oldaddy 

global oldsoladdy

oldsoladdy=['start', '0xold']

oldaddy=['start']

async def timer():
    while True:
        print('trying...')
        await get_nft(oldaddy)
        time.sleep(60)
        await get_sol_nft(oldsoladdy)
        time.sleep(60)
    return()

async def get_sol_nft(oldsoladdy):

    new_nft_url="https://public-api.solscan.io/account/transactions?account=cndyAnrLdpjq1Ssp1z8xxDsB8dxe7u4HL5Nxi2K5WXZ&limit=3"
    response = requests.get(new_nft_url)
    response = response.json()

    hash = response[2]['txHash']

    print(hash)

    if hash not in oldsoladdy:

        oldsoladdy.append(hash)


        hash_url = "https://public-api.solscan.io/transaction/"+hash


        hash_response = requests.get(hash_url)

        hash_response = hash_response.json()

        #print(hash_response)

        if hash_response['parsedInstruction'][-1]['type'] == 'mintNft':
            nft_addy = hash_response['parsedInstruction'][-1]['params']['Mint']
            print(nft_addy)


            meta_url = "https://api-mainnet.magiceden.dev/v2/tokens/"+nft_addy


            meta_response = requests.get(meta_url)

            print(meta_response.status_code)

            if meta_response.status_code == 200:
                print("true")


                meta_response = meta_response.json()

                name = meta_response['name']

                print(name)

                image = meta_response['image']

                update = meta_response['updateAuthority']

                solscan = "https://solscan.io/token/" + nft_addy
                
                await solnftalert(name, image, update, solscan)
                return()

        else:
            print("not mint event")



async def get_nft(oldaddy):

    url = "https://api.opensea.io/api/v1/collections?offset=0&limit=1"

    headers = {
        "Accept": "application/json",
        "X-API-KEY": ""
    }

    response = requests.request("GET", url, headers=headers)
    jsonfy=response.json()

    rep = jsonfy['collections'][0]
    #print(rep)
    print(rep['slug'])

    if len(rep['primary_asset_contracts']) > 0:
        addy= str(rep['primary_asset_contracts'][0]['address'])
        nft_url='https://opensea.io/collection/'+str(rep['slug'])
        slug=str(rep['slug'])
        print(addy, url)

        if addy != oldaddy[-1]:
            oldaddy.append(addy)
            await nftalert(addy, nft_url, slug)
            return()


# async def get_token(oldaddy):


#     response = requests.get('https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock=14341644&toBlock=latest&address=0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f&topic0=0x0d3648bd0f6ba80134a33ba9275ac585d9d315f0ad8355cddefde31afa28d0e9&apikey=')
#     jsonfy=response.json()

#     no1= '0x0d3648bd0f6ba80134a33ba9275ac585d9d315f0ad8355cddefde31afa28d0e9'
#     no2= '0x000000000000000000000000c02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'

#     x = jsonfy['result'][-1]['topics']

#     addy='null'
#     for i in x:
#         if i != no1 and i != no2:
#             addy = i
#             addy= addy[26:]
#             addy='0x'+addy

#             print('addy', addy)
#             print('old', oldaddy[-1])
#             #print('list',oldaddy)

#             if addy != oldaddy[-1]:
#                 oldaddy.append(addy)

#                 # print(oldaddy)

#                 # print(addy)
#                 await get_token_data(addy)

#                 return()

# async def get_token_data(addy):
#     w3 = Web3(Web3.HTTPProvider(''))

#     addy = addy
#     tokencontract='null'
#     contract='null'
#     token_name='null'
#     token_symbol='null'
#     etherscan_url='null'

#     print('about to get token data')

#     tokencontract = w3.toChecksumAddress(addy)

#     abi2 = [{"constant":True,"inputs":[],"name":"mintingFinished","outputs":[{"name":"","type":"bool"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":False,"type":"function"},{"constant":False,"inputs":[],"name":"unpause","outputs":[{"name":"","type":"bool"}],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"mint","outputs":[{"name":"","type":"bool"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":False,"type":"function"},{"constant":True,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":False,"type":"function"},{"constant":False,"inputs":[],"name":"finishMinting","outputs":[{"name":"","type":"bool"}],"payable":False,"type":"function"},{"constant":False,"inputs":[],"name":"pause","outputs":[{"name":"","type":"bool"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_releaseTime","type":"uint256"}],"name":"mintTimelocked","outputs":[{"name":"","type":"address"}],"payable":False,"type":"function"},{"constant":True,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":False,"type":"function"},{"anonymous":False,"inputs":[{"indexed":True,"name":"to","type":"address"},{"indexed":False,"name":"value","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":False,"inputs":[],"name":"MintFinished","type":"event"},{"anonymous":False,"inputs":[],"name":"Pause","type":"event"},{"anonymous":False,"inputs":[],"name":"Unpause","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"owner","type":"address"},{"indexed":True,"name":"spender","type":"address"},{"indexed":False,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"from","type":"address"},{"indexed":True,"name":"to","type":"address"},{"indexed":False,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]

#     contract = w3.eth.contract(tokencontract, abi= abi2)

#     token_name= contract.functions.name().call()

#     token_symbol = contract.functions.symbol().call()

#     etherscan_url = 'https://etherscan.io/address/'+addy

#     print(token_name, token_symbol, etherscan_url)

#     #await tokenalert(token_name, token_symbol, etherscan_url)
    
#     return()



TOKEN =""

client = discord.Client()

# @client.event
# async def tokenalert(token_name, token_symbol, etherscan_url):
#     channel = client.get_channel()
#     print(channel)
#     print('preparing to send alert...')
#     embed2 = discord.Embed(title = str(token_name), description= token_symbol +': created on Uniswap!', url = str(etherscan_url), color = 0xffd800 )
    
#     print(embed2)
#     await channel.send(embed = embed2)
#     return()

@client.event
async def nftalert(addy, nft_url, slug):
    channel = client.get_channel()
    print(channel)
    print('preparing to send alert...')
    embed2 = discord.Embed(title = str(slug), description='NFT Contract: ' +str(addy) + ' created!', url = str(nft_url), color = 0xffd800 )
    
    print(embed2)
    await channel.send(embed = embed2)
    return()


@client.event
async def solnftalert(name, image, update, solscan):
    channel = client.get_channel()
    print(channel)
    print('preparing to send alert...')
    embed2 = discord.Embed(title = str(name)+" minted!", description='Update Authority: ' +str(update), url = str(solscan), color = 0xffd800 )
    
    print(embed2)
  
    embed2.set_image(url=image)
    await channel.send(embed = embed2)
    return()



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await timer()




client.run(TOKEN)



