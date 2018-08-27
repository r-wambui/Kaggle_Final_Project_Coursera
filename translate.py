""" 
	Convert the dataset to English language, Goslate require paid 
	premium on Google, therefore I decided to use mtranlate
"""
# import goslate
import pandas as pd
# gs = goslate.Goslate()

# shops_df = pd.read_csv("Future Sales/Data/shops.csv")

# not_en = shops_df["shop_name"] != "en"
# print(not_en)
# shops_df["shop_name"] = [gs.translate(row, "en") for row in shops_df["shop_name"]]
# shops_df.to_csv("shops_trans")


from mtranslate import translate
shops_df = pd.read_csv("Future Sales/Data/shops.csv")
shops_df["shop_name"] = [translate(row, "en", "auto") for row in shops_df["shop_name"]]
shops_df.to_csv("shop_trans.csv", index=False)
