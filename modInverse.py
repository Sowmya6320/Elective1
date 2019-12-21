# Euclidean's GCD to find GCD of 2numbers
def egcd(a,b):
	if b == 0:
		return a
	else:
		return egcd(b,a%b)

# To calculate Modular Inverse
def mod_inv(a,b,x1,x2,y1,y2):
	gcd = egcd(a,b)
	if gcd == 1:	
		if b == 0:
			return x1 , y1
		else:
			x = (x1 - ((a/b)*x2))
			y = (y1 - ((a/b)*y2))
			return mod_inv(b,a%b,x2,x,y2,y)
	else:
		print "mod_inv_doesn't_exist"

print mod_inv(53947,56211,1,0,0,1)%b
print mod_inv(19385,43159,1,0,0,1)%b
