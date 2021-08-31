weight = 41.5

#Ground shipping formatted to two decimal points
def ground_shipping(weight):
  if weight <= 2:
    cost = (weight * 1.50) + 20.00
  elif weight <= 6:
    cost = (weight * 3.00) + 20.00
  elif weight <= 10:
    cost = (weight * 4.00) + 20.00
  elif weight > 10:
    cost = (weight * 4.75) + 20.00
  return cost
ground_shipping_cost = "{:.2f}".format(ground_shipping(weight))
print("Ground shipping: $" + ground_shipping_cost)

#Premium shipping formatted to two decimal points
##Written as a formula to account for a flat fee potentially changing to a weight-based rate later
cost_ground_premium = 125.00
def premium_shipping(weight):
  return cost_ground_premium
premium_shipping_cost = "{:.2f}".format(premium_shipping(weight))
print("Ground premium: $" + premium_shipping_cost)

#Drone shipping formatted to two decimal points
def drone_shipping(weight):
  if weight <= 2:
    cost = weight * 4.50
  elif weight <= 6:
    cost = weight * 9.00
  elif weight <= 10:
    cost = weight * 12.00
  elif weight > 10:
    cost = weight * 14.25
  return cost
drone_shipping_cost = "{:.2f}".format(drone_shipping(weight))
print("Drone shipping: $" + drone_shipping_cost)

#Tell customer which cost is cheapest - Option 1
def cheapest(weight):
  costs = []
  costs.append(ground_shipping_cost)
  costs.append(premium_shipping_cost)
  costs.append(drone_shipping_cost)
  best = min(costs)
  return best
print("Your best price: $" + str(cheapest(weight)))

#Tell customer which method is cheapest - Option 2
if ground_shipping_cost < premium_shipping_cost and ground_shipping_cost < drone_shipping_cost:
  print("Ground Shipping is your best bet! It'll cost you " + "$" + str(ground_shipping_cost) + ".")
elif premium_shipping_cost < ground_shipping_cost and premium_shipping_cost < drone_shipping_cost:
  print("Ground premium is your best bet! It'll cost you " + "$" + str(premium_shipping_cost) + ".")
elif drone_shipping_cost < ground_shipping_cost and drone_shipping_cost < premium_shipping_cost:
  print("Drone shipping is your best bet! It'll cost you " + "$" + str(drone_shipping_cost) + ".")
