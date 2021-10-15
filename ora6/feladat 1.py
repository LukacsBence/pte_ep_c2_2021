km_h = 1000
h_s = 3600
try:
speed_km_h = float(input("Kérem adja meg a sebességet: \n"))
speed_m_s = speed_km_h * km_h / h_s
print(f"A {km_h})
except:
print("Sajnálom, de nem tudom átváltani.")