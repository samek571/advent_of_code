class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for c in letters:
            if c > target:
                return c
        return letters[0]

def main():
    sol = Solution()
    print(sol.nextGreatestLetter(letters = ["c","f","j"], target = "c"))

if __name__ == "__main__": main()