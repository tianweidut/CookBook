

class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here
        bcnt = sum([1 for i in string if i == ' '])
        
        r = [] * (length + bcnt * 2)
        for i in string:
            if i == ' ':
                r.extend(list('%20'))
            else:
                r.append(i)
                
        return len(r)


if __name__ == "__main__":
    print Solution().replaceBlank("hello world", 11)
