class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        answer = ""
        carry = 0
        while i >= 0 or j >= 0 :

                if i < 0 :
                    digit1 = 0
                else:
                    digit1 = int(a[i])

                if j < 0 :
                    digit2 = 0
                else:
                    digit2 = int(b[j])

                total = digit1 + digit2 + carry

                result = total % 2

                carry = total // 2

                

                answer = str(result) + answer
                

                i -=1
                j -=1

        if carry == 1:
            answer = str(carry)+answer


        return answer

        