from collections import Counter

class Solution:
    def longestPalindrome(self, words) -> int:
        # we hashmap them all, store in hashmap as word:number of occurence
        hashmap = Counter(words)
        
        answer = 0
        mid_flag = False
        
        for word, count_of_the_word in hashmap.items():
            # 1st case in which the 2digit word is palindrome
            # if we get even number of little palindromes we gucci
            # otherwise we need to cap it at even by not using all of them except the last one 
            # (so like 15 gets capped at 14) and if there is more cases like this;
            # (13, 7, 41, 3) we use (12, 6, 40, 2) but +1 since one can be in the middle
            # (the +1 is handled by flag)
            if word[0] == word[1]:
                if count_of_the_word % 2 == 0:
                    answer += count_of_the_word
                else:
                    answer += count_of_the_word - 1
                    mid_flag = True

            # 2nd case is a pair of non-palindrome words
            # we need to look for it reversed buddy and we are similarly capped
            # at the lower valued one, so like if "ls":3 and "sl":8 we go with 3 only
            # but times 2 because the word consists of 2 chars
            elif word[0] < word[1]:
                answer += 2 * min(count_of_the_word, hashmap[word[1] + word[0]])

        # if we got odd number of palindrom words at least once
        if mid_flag:
            answer += 1

        # times 2 because each word has its complementary number
        return 2 * answer