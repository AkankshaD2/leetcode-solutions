from bisect import bisect_left, bisect_right
class Solution(object):
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)
        pos = [[] for _ in range(26)]
        for i, ch in enumerate(word1):
            pos[ord(ch) - ord('a')].append(i)
        exact = [-1] * (m + 1)
        exact[m] = n
        limit = n
        for j in range(m - 1, -1, -1):
            arr = pos[ord(word2[j]) - ord('a')]
            k = bisect_left(arr, limit) - 1
            if k < 0:
                exact[j] = -1
                limit = -1
            else:
                exact[j] = arr[k]
                limit = exact[j]
        almost = [-1] * (m + 1)
        almost[m] = n
        for j in range(m - 1, -1, -1):
            limit = almost[j + 1]
            arr = pos[ord(word2[j]) - ord('a')]
            k = bisect_left(arr, limit) - 1
            match_index = arr[k] if k >= 0 else -1
            mismatch_index = exact[j + 1] - 1
            almost[j] = max(match_index, mismatch_index)
        ans = []
        prev = -1
        used_mismatch = False

        for j in range(m):
            target = ord(word2[j]) - ord('a')
            arr = pos[target]
            k = bisect_right(arr, prev)
            if k < len(arr):
                match_index = arr[k]
            else:
                match_index = -1
            mismatch_index = -1
            if not used_mismatch:
                best = n
                for c in range(26):
                    if c == target:
                        continue
                    arr = pos[c]
                    k = bisect_right(arr, prev)
                    if k < len(arr):
                        best = min(best, arr[k])
                if best != n:
                    mismatch_index = best
            chosen = -1
            if used_mismatch:
                if match_index != -1 and exact[j + 1] > match_index:
                    chosen = match_index
            else:
                if match_index != -1 and almost[j + 1] > match_index:
                    chosen = match_index
                if mismatch_index != -1 and exact[j + 1] > mismatch_index:
                    if chosen == -1 or mismatch_index < chosen:
                        chosen = mismatch_index
                        used_mismatch = True
            if chosen == -1:
                return []
            ans.append(chosen)
            prev = chosen
        return ans