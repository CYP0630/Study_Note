class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        #num_1 = int(number % 10)
        #num_2 = int(number // 10 % 10)
        #num_3 = int(number // 100)
        
        tmp = str(number)
        tmp = tmp[::-1]
        return int(tmp)
        #return num_1 * 100 + num_2 * 10 + num_3

        
