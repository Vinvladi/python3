import math

# Переменные
a1 = 10.61 #tigercat cooldown(Plane)
a2 = 11.17 #curtiss cooldown(Plane)
a3 = 11.91 #junkers cooldown(Plane)
k1 = 4 #tigercat numberof(Plane)
k2 = 3 #curtiss numberof(Plane)
k3 = 3 #junkers numberof(Plane)
Reload = 188
StatBonus = 0.00 #0.04 = 0.26 уменьшение
LaunchCooldown = ((a1*k1+a2*k2+a3*k3)/(k1+k2+k3))*2.2*math.sqrt(200/(Reload*(1+StatBonus)+100))+0.1
LaunchCooldown2 = ((a1*k1+a2*k2)/(k1+k2))*2.2*math.sqrt(200/(Reload*(1+StatBonus)+100))+0.1
print (LaunchCooldown2)