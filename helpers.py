from urllib import response
import requests as req
import os

KEY = os.getenv("SECRET_TOKEN")
STORE = os.getenv("STORE_NAME")
INVENTORYLOCATION = 55834411176
H = {"X-Shopify-Access-Token":os.getenv("SECRET_TOKEN"),
    "Content-Type":"application/json"} 

#function to get the inventory level at a location
def get_inventory_at_location(inventoryid,locationid):
    response = req.get("https://"+STORE+"/admin/api/2022-10/inventory_levels.json?inventory_item_ids="+str(inventoryid)+"&location_ids="+str(locationid),headers=H)
    print(response.text)
    print("info")

#function to update inventory amount at a location
def change_inventory_at_location(quantity,inventoryid,locationid):
    data = {
        "location_id":str(locationid),
        "inventory_item_id":str(inventoryid),
        "available":str(quantity)
    }
    response = req.post("https://"+STORE+"/admin/api/2022-10/inventory_levels/set.json",json=data,headers=H)
    print(response.text)
    print("changed")

def get_inventory_id(variant_id):
    print("https://"+STORE+"/admin/api/2022-10/variants/"+str(variant_id)+".json")
    response = req.get("https://"+STORE+"/admin/api/2022-10/variants/"+str(variant_id)+".json",headers=H)
    res = response.json()
    id = res["variant"]["inventory_item_id"]
    return id

def get_variant_id(sku):
    count = 1
    id = ''
    response = req.get("https://"+STORE+"/admin/api/2022-10/variants.json?limit=250",headers=H)
    res = response.json()
    for item in res["variants"]:
        if item["sku"] == str(sku): 
            id = item["id"]
    while response is not None and id == '':
        print(count)
        count += 1
        response = req.get(response.links["next"]["url"],headers=H)
        res = response.json()
        for item in res["variants"]:
            if item["sku"] == str(sku): 
                id = item["id"]
            
    return id
     
def update_virtual_inventory(sku,quant):
    variantid = get_variant_id(sku)
    inventoryid = get_inventory_id(variantid)
    change_inventory_at_location(quant,inventoryid,INVENTORYLOCATION)