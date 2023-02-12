# 배송비 데이터 파일 수정 및 재 업로드 -> DB 추가용도
import pandas as pd

df = pd.read_csv('./apps/data/DeliveryCostCorrected.csv')
df = df.melt(id_vars=['quantity'])
df = df.rename(columns={"variable":"country", "value":"cost"})
df.to_csv("./apps/data/CompletedDeliveryCost.csv")