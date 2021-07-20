class Solution:
    def findMinOverrideSubString(self, source, target) :
        # write code here
        d,d0 = {},{}
        count0,count1 = 0,0
        def check(l,r):
            for i in range(len(target)):
                print('target[i]:',target[i])
                while l<=r and target[i]!=source[l]:
                    print(source[i])
                    l+=1
                if l>r:
                    return False
            return True

        for i in range(len(target)):
            if target[i] in d:
                d[target[i]]+=1
            else:
                count0 += 1
                d[target[i]] = 1
        l,res,l0 = 0,len(source),0
        print(count0,d)
        flag = False
        for i in range(len(source)):
            print(i,source[i])
            if source[i] in d0:
                d0[source[i]] += 1
            else:
                d0[source[i]] = 1
            if source[i] in d:
                if d0[source[i]] == d[source[i]]:
                    count1 += 1
            print('count1:',count1)

            if count0==count1:
                print('ji')
                while count1 == count0:
                    print('jin')
                    if source[l] in d:
                        if d0[source[l]]==d[source[l]]:
                            if check(l,i):
                                flag = True
                                if i-l+1<res:
                                    res = i-l+1
                                    l0 = l
                                    print(res,l0)
                            count1 -= 1
                    d0[source[l]] -= 1
                    l += 1
                    print(l,res,l0)
        return source[l0:l0+res] if flag else 'kong'
A = Solution()
print(A.findMinOverrideSubString('adfdbdbbdgcd','bcd'))