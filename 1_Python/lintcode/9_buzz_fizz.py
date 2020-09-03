class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    
    
    If n = 15, you should return:
    [
    "1", "2", "fizz",
    "4", "buzz", "fizz",
    "7", "8", "fizz",
    "buzz", "11", "fizz",
    "13", "14", "fizz buzz"
    ]

    If n = 10, you should return:
    [
    "1", "2", "fizz",
    "4", "buzz", "fizz",
    "7", "8", "fizz",
    "buzz"
    ]
    """
    def fizzBuzz(self, n):
        # write your code here
        result = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 != 0:
                result.append("fizz")
            elif i % 5 == 0 and i % 3 != 0:
                result.append("buzz")
            elif i % 3 == 0 and i % 5 == 0:
                result.append("fizz buzz")
            else:
                result.append(str(i))
        
        #return ["fizz" * (i % 3 == 0) +"buzz" * (i % 5 == 0) + str(i) * (i % 3 != 0 and i % 5 != 0) for i in range(1, n + 1)]
        
        return result
