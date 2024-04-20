class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:

        while sx <= tx and sy <= ty:

            # if at any point we end up adding only the one to the second; its clear it can be done
            if (ty - sy) % tx == 0 and (tx - sx) % ty == 0: return True
            
            # more fancy way of stating that we can subtract one from another
            tx, ty = tx % ty, ty % tx
            
        return False
