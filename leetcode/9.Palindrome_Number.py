# Time : O(log10(x))
# Space: O(1)
def isPalindrome(self, x: int) -> bool:
    if x==0:
        return True
    digit=0
    val=0
    temp=x
    if x<0:
        return False
    else:
        while(x!=0):
        val=x%10
        digit=digit*10+val
        x=x//10
        if (temp==digit):
            return True
        else:
            return False
