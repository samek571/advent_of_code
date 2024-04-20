class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        return (G - E) * (H - F) + (C - A) * (D - B) - (max(min(C, G)  -  max(E, A), 0) * max(min(D, H) - max(F, B), 0))

def main():
    sol = Solution()
    print(sol.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))

if __name__ == "__main__": main()