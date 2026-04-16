userAuth = [("magesh", "test123"), ("kumar", "welcome123"), ("dhanvith", "family123")]

# Sort by value
orderByUserName = sorted(userAuth, key=lambda t: t[0])
print(orderByUserName)

userAuthMap = [{"username": "magesh", "password": "test123"}, {"username": "kumar", "password": "welcome123"},
               {"username": "dhanvith", "password": "family123"}]
# Sort by Key
userAuthMap.sort(key=lambda k: k["password"])
print(userAuthMap)
