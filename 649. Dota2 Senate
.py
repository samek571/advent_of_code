class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        # Initialize a queue using deque with senators from the input string
        queue = collections.deque(senate)

        # Count the number of senators from each party
        radiant_count = senate.count('R')
        dire_count = len(senate) - radiant_count

        # Initialize the number of banned senators from each party to zero
        radiant_banned = dire_banned = 0

        # Loop until all senators from one party are banned
        while radiant_banned < radiant_count and dire_banned < dire_count:

            # Ban the senator if their party has already had a senator banned
            if queue.popleft() == 'R':
                if radiant_banned: radiant_banned -= 1
                
                else:
                    queue.append('R')
                    dire_banned += 1
           
           
            else:
                if dire_banned: dire_banned -= 1
                
                else:
                    queue.append('D')
                    radiant_banned += 1

        # Return the winner based on the number of remaining banned senators
        return 'Radiant' if dire_count == dire_banned else 'Dire'
