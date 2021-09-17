electric_clock= 25 #A
voltage= 230 #V
performance= electric_clock*voltage # W
bulb= 5 * 30 #W
ac= 1500 #W
washing_machine= 1200 #w
iron= 2000 #w
electric_usage=(bulb+ac+washing_machine+iron)
print("A megszakító nem kapcsol le, ha bekapcsoljuk a vasalót:", performance>electric_usage)
