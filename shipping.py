weight = 41.5
cost = ""
#Ground Shipping
flat_charge = 20.00
if weight <= 2: 
  cost= 1.50 * weight + flat_charge 
  
elif weight > 2 and weight <= 6:
  cost = 3.00 * weight + flat_charge
  
elif weight > 6 and weight <= 10:
  cost = 4.00 * weight + flat_charge
 
elif weight > 10:
  cost = 4.75 * weight + flat_charge
  
print("Ground Shipping: $", cost)

#Ground Shipping Premium:
cost_premium = 125.00
print("Ground Shipping Premium:","$",cost_premium)

#Drone Shipping
cost_drone =""
if weight <= 2:
  cost_drone= 4.50* weight
elif weight >2 and weight <=6:
  cost_drone=9.00* weight
elif weight > 6 and weight <=10:
  cost_drone=12.00*weight
else: cost_drone = 14.25 * weight

print("Drone Shipping:$",cost_drone)

# Cheapest method of shipping a 4.8 pound package = GROUND SHIPPING, it'd cost exactly $34.4
# Cheapest method of shipping a 41.5 pound package = GROUND SHIPPING PREMIUM, it'd cost exactly $125.0